"""Create a reproducible ZIP release without repository metadata or caches."""

from __future__ import annotations

import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "releases" / "project-universal-global-ai-skills.zip"
EXCLUDED_PARTS = {".git", "__pycache__", ".pytest_cache", "node_modules", "dist", "build"}
EXCLUDED_NAMES = {".env", ".env.local"}


def main() -> None:
    OUTPUT.parent.mkdir(exist_ok=True)
    if OUTPUT.exists():
        OUTPUT.unlink()
    included = 0
    with zipfile.ZipFile(OUTPUT, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in ROOT.rglob("*"):
            if not path.is_file() or path == OUTPUT:
                continue
            if any(part in EXCLUDED_PARTS for part in path.parts):
                continue
            if path.name in EXCLUDED_NAMES or path.suffix in {".pyc", ".tmp"}:
                continue
            archive.write(path, path.relative_to(ROOT))
            included += 1
    print(f"Packaged {included} files into {OUTPUT}")


if __name__ == "__main__":
    main()
