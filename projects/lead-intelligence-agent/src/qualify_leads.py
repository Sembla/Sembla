from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
from typing import List

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "leads.csv"
OUTPUT = ROOT / "output" / "qualified_leads.csv"
REPORT = ROOT / "output" / "latest_report.md"

TRAINING_DATA = [
    ("quero saber preço do curso e começar essa semana", "hot"),
    ("tenho interesse e quero falar com consultor hoje", "hot"),
    ("preciso melhorar minha oratória para uma apresentação urgente", "hot"),
    ("quero matrícula para o próximo mês", "hot"),
    ("gostaria de entender como funciona o curso", "warm"),
    ("qual a duração e os horários disponíveis", "warm"),
    ("vi no instagram e queria mais informações", "warm"),
    ("tenho curiosidade sobre os módulos", "warm"),
    ("só estou pesquisando opções para o futuro", "cold"),
    ("estou comparando escolas sem previsão de começar", "cold"),
    ("talvez no ano que vem", "cold"),
    ("não tenho interesse agora", "cold"),
]

PRIORITY_SCORE = {"hot": 90, "warm": 60, "cold": 25}


@dataclass
class Lead:
    lead_id: str
    name: str
    source: str
    message: str


def build_model() -> Pipeline:
    texts, labels = zip(*TRAINING_DATA)
    model = Pipeline(
        [
            ("tfidf", TfidfVectorizer(ngram_range=(1, 2), strip_accents="unicode")),
            ("classifier", LogisticRegression(max_iter=500, random_state=42)),
        ]
    )
    model.fit(texts, labels)
    return model


def load_leads() -> List[Lead]:
    with INPUT.open(encoding="utf-8", newline="") as file:
        return [Lead(**row) for row in csv.DictReader(file)]


def main() -> None:
    model = build_model()
    leads = load_leads()
    texts = [lead.message for lead in leads]
    labels = model.predict(texts)
    probabilities = model.predict_proba(texts)
    classes = list(model.classes_)

    rows = []
    for lead, label, probability_row in zip(leads, labels, probabilities):
        confidence = float(probability_row[classes.index(label)])
        score = PRIORITY_SCORE[label] + round((confidence - 0.33) * 15)
        score = max(0, min(100, score))
        action = (
            "contact_now"
            if label == "hot"
            else "follow_up_today"
            if label == "warm"
            else "nurture"
        )
        rows.append(
            {
                "lead_id": lead.lead_id,
                "name": lead.name,
                "source": lead.source,
                "message": lead.message,
                "classification": label,
                "priority_score": score,
                "confidence": f"{confidence:.3f}",
                "recommended_action": action,
            }
        )

    rows.sort(key=lambda row: row["priority_score"], reverse=True)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    with OUTPUT.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    counts = {key: sum(row["classification"] == key for row in rows) for key in PRIORITY_SCORE}
    report = [
        "# Lead Intelligence Agent — Latest Run",
        "",
        f"Processed **{len(rows)}** leads.",
        "",
        f"- Hot: **{counts['hot']}**",
        f"- Warm: **{counts['warm']}**",
        f"- Cold: **{counts['cold']}**",
        "",
        "## Top priorities",
        "",
    ]
    for row in rows[:3]:
        report.append(
            f"- **{row['name']}** ({row['source']}) — "
            f"{row['classification'].upper()} · score {row['priority_score']} · "
            f"action `{row['recommended_action']}`"
        )

    REPORT.write_text("\n".join(report) + "\n", encoding="utf-8")
    print(f"Processed {len(rows)} leads -> {OUTPUT}")


if __name__ == "__main__":
    main()
