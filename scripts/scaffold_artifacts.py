#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as _dt
import sys
from pathlib import Path


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _write_text(path: Path, content: str, *, force: bool) -> None:
    if path.exists() and not force:
        raise FileExistsError(f"Refusing to overwrite existing file: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def _render(template: str, mapping: dict[str, str]) -> str:
    rendered = template
    for key, value in mapping.items():
        rendered = rendered.replace(f"{{{{{key}}}}}", value)
    return rendered


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description="Generate a standard agent/LLM delivery artifact pack from skill templates."
    )
    parser.add_argument("--out", required=True, help="Output directory to write files into.")
    parser.add_argument("--project", default="TBD", help="Project name.")
    parser.add_argument("--client", default="TBD", help="Client/company name.")
    parser.add_argument("--vendor", default="TBD", help="Delivery/vendor name.")
    parser.add_argument(
        "--version", default="0.1", help="Version string for generated artifacts."
    )
    parser.add_argument(
        "--date",
        default=_dt.date.today().isoformat(),
        help="Date string (default: today).",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite files if they already exist.",
    )
    args = parser.parse_args(argv)

    skill_root = Path(__file__).resolve().parents[1]
    templates_dir = skill_root / "assets" / "templates"
    if not templates_dir.is_dir():
        print(f"ERROR: templates directory not found: {templates_dir}", file=sys.stderr)
        return 2

    out_dir = Path(args.out).expanduser().resolve()
    mapping = {
        "PROJECT_NAME": args.project,
        "CLIENT_NAME": args.client,
        "VENDOR_NAME": args.vendor,
        "VERSION": args.version,
        "DATE": args.date,
    }

    template_paths = sorted(p for p in templates_dir.glob("*.md") if p.is_file())
    if not template_paths:
        print(f"ERROR: no templates found in {templates_dir}", file=sys.stderr)
        return 2

    wrote = 0
    for template_path in template_paths:
        rendered = _render(_read_text(template_path), mapping)
        out_path = out_dir / template_path.name
        _write_text(out_path, rendered, force=args.force)
        wrote += 1

    print(f"[OK] Wrote {wrote} files to {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

