from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from media_pipeline import (  # noqa: E402
    Toolchain,
    build_layout_command,
    build_preview_command,
    build_video_command,
    ensure_inputs,
    ensure_outputs_available,
    output_paths,
    sha256_file,
)


class MediaPipelineTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tools = Toolchain(
            image_command=("convert",),
            ffmpeg="ffmpeg",
            ffprobe="ffprobe",
        )

    def test_output_names_are_deterministic(self) -> None:
        paths = output_paths(Path("dist"))
        self.assertEqual(paths["video"], Path("dist/tour-virtual-ia.mp4"))
        self.assertEqual(paths["report"], Path("dist/processing-report.json"))

    def test_layout_command_removes_metadata(self) -> None:
        command = build_layout_command(self.tools, Path("in.png"), Path("out.png"))
        self.assertIn("-strip", command)
        self.assertIn("png:compression-level=9", command)

    def test_video_command_removes_audio_and_metadata(self) -> None:
        command = build_video_command(self.tools, Path("in.mp4"), Path("out.mp4"))
        self.assertIn("-an", command)
        self.assertIn("-map_metadata", command)
        self.assertIn("1280:720", " ".join(command))

    def test_preview_uses_controlled_palette(self) -> None:
        command = build_preview_command(self.tools, Path("in.mp4"), Path("out.gif"))
        joined = " ".join(command)
        self.assertIn("palettegen", joined)
        self.assertIn("max_colors=96", joined)

    def test_sha256_file(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.txt"
            path.write_bytes(b"applied-ai")
            self.assertEqual(
                sha256_file(path),
                "51b79ff50e545c7d31139400a4ad2f304f396ecabe6da9b722914e88f90e2d90",
            )

    def test_missing_input_is_rejected(self) -> None:
        with self.assertRaises(FileNotFoundError):
            ensure_inputs([Path("file-that-does-not-exist.png")])

    def test_existing_output_requires_overwrite(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "existing.gif"
            path.write_bytes(b"gif")
            with self.assertRaises(FileExistsError):
                ensure_outputs_available([path], overwrite=False)
            ensure_outputs_available([path], overwrite=True)


if __name__ == "__main__":
    unittest.main()
