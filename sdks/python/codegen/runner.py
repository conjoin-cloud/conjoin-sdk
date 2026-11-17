from __future__ import annotations

import shutil
from pathlib import Path

from codegen.render import render_all


def main() -> None:
    counts = render_all()
    _remove_bytecode_caches()
    for spec_file, operation_count in counts.items():
        print(f"{spec_file}: {operation_count} operations")


def _remove_bytecode_caches() -> None:
    cache_dir = Path(__file__).resolve().parent / "__pycache__"
    if cache_dir.exists():
        shutil.rmtree(cache_dir)
