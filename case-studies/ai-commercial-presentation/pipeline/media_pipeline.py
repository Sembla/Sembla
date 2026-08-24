#!/usr/bin/env python3
"""Prepare human-reviewed media for an AI project-presentation case study.

The pipeline removes embedded metadata, optimizes images, creates a silent
720p video, generates a GIF preview and writes a machine-readable report.

Important: this program does not detect or redact confidential information
visible inside an image. Visual anonymization requires human review before the
files are provided to this pipeline.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Sequence


OUTPUT_FILENAMES = {
    "layout": "layout-conceitual-sanitizado.png",
    "visual": "visualizacao-comercial-ia.jpg",
    "video": "tour-virtual-ia.mp4",
    "preview": "tour-preview.gif",
    "report": "processing-report.json",
}


@dataclass(frozen=True)
class Toolchain:
    image_command: tuple[str, ...]
    ffmpeg: str
    ffprobe: str


def discover_toolchain() -> Toolchain:
    """Return the required local executables or raise a clear error."""
    magick = shutil.which("magick")
    convert = shutil.which("convert")
    ffmpeg = shutil.which("ffmpeg")
    ffprobe = shutil.which("ffprobe")

    missing: list[str] = []
    if not (magick or convert):
        missing.append("ImageMagick (magick or convert)")
    if not ffmpeg:
        missing.append("ffmpeg")
    if not ffprobe:
        missing.append("ffprobe")
    if missing:
        raise RuntimeError("Missing required tools: " + ", ".join(missing))

    return Toolchain(
        image_command=(magick or convert,),
        ffmpeg=ffmpeg,
        ffprobe=ffprobe,
    )


def output_paths(output_dir: Path) -> dict[str, Path]:
    return {key: output_dir / name for key, name in OUTPUT_FILENAMES.items()}


def build_layout_command(toolchain: Toolchain, source: Path, target: Path) -> list[str]:
    """Build the metadata-removal and PNG optimization command."""
    return [
        *toolchain.image_command,
        str(source),
        "-strip",
        "-resize",
        "1600x1600>",
        "-colorspace",
        "sRGB",
        "-define",
        "png:compression-level=9",
        str(target),
    ]


def build_visual_command(toolchain: Toolchain, source: Path, target: Path) -> list[str]:
    """Build the metadata-removal and JPEG optimization command."""
    return [
        *toolchain.image_command,
        str(source),
        "-strip",
        "-resize",
        "1600x1600>",
        "-colorspace",
        "sRGB",
        "-sampling-factor",
        "4:2:0",
        "-quality",
        "88",
        str(target),
    ]


def build_video_command(toolchain: Toolchain, source: Path, target: Path) -> list[str]:
    """Build a silent, metadata-free, GitHub-friendly 720p MP4 command."""
    video_filter = (
        "scale=1280:720:force_original_aspect_ratio=decrease:flags=lanczos,"
        "pad=1280:720:(ow-iw)/2:(oh-ih)/2:color=black"
    )
    return [
        toolchain.ffmpeg,
        "-y",
        "-hide_banner",
        "-loglevel",
        "error",
        "-i",
        str(source),
        "-map",
        "0:v:0",
        "-map_metadata",
        "-1",
        "-an",
        "-vf",
        video_filter,
        "-c:v",
        "libx264",
        "-preset",
        "medium",
        "-crf",
        "23",
        "-pix_fmt",
        "yuv420p",
        "-movflags",
        "+faststart",
        str(target),
    ]


def build_preview_command(toolchain: Toolchain, source: Path, target: Path) -> list[str]:
    """Build an optimized animated GIF preview command."""
    preview_filter = (
        "fps=8,scale=720:-1:flags=lanczos,split[s0][s1];"
        "[s0]palettegen=max_colors=96:stats_mode=diff[p];"
        "[s1][p]paletteuse=dither=bayer:bayer_scale=5:diff_mode=rectangle"
    )
    return [
        toolchain.ffmpeg,
        "-y",
        "-hide_banner",
        "-loglevel",
        "error",
        "-i",
        str(source),
        "-filter_complex",
        preview_filter,
        "-loop",
        "0",
        str(target),
    ]


def run_command(command: Sequence[str], dry_run: bool = False) -> None:
    print("$", subprocess.list2cmdline(list(command)))
    if not dry_run:
        subprocess.run(command, check=True)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def probe_media(ffprobe: str, path: Path) -> dict[str, object]:
    command = [
        ffprobe,
        "-v",
        "error",
        "-show_entries",
        "format=duration:stream=codec_name,codec_type,width,height,r_frame_rate",
        "-of",
        "json",
        str(path),
    ]
    completed = subprocess.run(command, check=True, capture_output=True, text=True)
    return json.loads(completed.stdout)


def file_record(ffprobe: str, path: Path) -> dict[str, object]:
    return {
        "name": path.name,
        "size_bytes": path.stat().st_size,
        "sha256": sha256_file(path),
        "media": probe_media(ffprobe, path),
    }


def ensure_inputs(paths: Sequence[Path]) -> None:
    missing = [str(path) for path in paths if not path.is_file()]
    if missing:
        raise FileNotFoundError("Input files not found: " + ", ".join(missing))


def ensure_outputs_available(paths: Sequence[Path], overwrite: bool) -> None:
    existing = [str(path) for path in paths if path.exists()]
    if existing and not overwrite:
        raise FileExistsError(
            "Output files already exist. Use --overwrite to replace them: "
            + ", ".join(existing)
        )


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Package human-reviewed AI presentation media for GitHub."
    )
    parser.add_argument("--layout", required=True, type=Path, help="Sanitized conceptual layout")
    parser.add_argument("--visual", required=True, type=Path, help="AI-generated commercial visual")
    parser.add_argument("--video", required=True, type=Path, help="AI-generated source video")
    parser.add_argument("--output", required=True, type=Path, help="Output directory")
    parser.add_argument("--overwrite", action="store_true", help="Replace existing outputs")
    parser.add_argument("--dry-run", action="store_true", help="Print commands without executing them")
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    inputs = [args.layout, args.visual, args.video]
    ensure_inputs(inputs)
    toolchain = discover_toolchain()

    destinations = output_paths(args.output)
    generated = [
        destinations["layout"],
        destinations["visual"],
        destinations["video"],
        destinations["preview"],
        destinations["report"],
    ]
    ensure_outputs_available(generated, args.overwrite)

    if not args.dry_run:
        args.output.mkdir(parents=True, exist_ok=True)

    commands = [
        build_layout_command(toolchain, args.layout, destinations["layout"]),
        build_visual_command(toolchain, args.visual, destinations["visual"]),
        build_video_command(toolchain, args.video, destinations["video"]),
        build_preview_command(toolchain, destinations["video"], destinations["preview"]),
    ]
    for command in commands:
        run_command(command, dry_run=args.dry_run)

    if args.dry_run:
        return 0

    report = {
        "pipeline": "ai-presentation-media-packaging-v1",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "security_boundary": (
            "Visual anonymization is a human-review step completed before this pipeline. "
            "Metadata removal does not redact visible confidential information."
        ),
        "inputs": {
            "layout": args.layout.name,
            "visual": args.visual.name,
            "video": args.video.name,
        },
        "outputs": [
            file_record(toolchain.ffprobe, destinations["layout"]),
            file_record(toolchain.ffprobe, destinations["visual"]),
            file_record(toolchain.ffprobe, destinations["video"]),
            file_record(toolchain.ffprobe, destinations["preview"]),
        ],
    }
    destinations["report"].write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Report: {destinations['report']}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (FileNotFoundError, FileExistsError, RuntimeError, subprocess.CalledProcessError) as error:
        print(f"Error: {error}", file=sys.stderr)
        raise SystemExit(1) from error
