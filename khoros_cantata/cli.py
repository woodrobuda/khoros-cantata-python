"""Simple command-line entry point for the Python-native Khoros tools."""





from __future__ import annotations
import argparse
import json
from pathlib import Path
from .workspace_runtime import HistoricalWorkspaceParser, WorkspaceExecutor, example_registry
from .phase21_numeric import run_phase21_checks, inventory, corpus_available, ROOT


def cmd_inspect(path: Path) -> int:
    """Read a workspace and print its main building blocks."""
    ws = HistoricalWorkspaceParser().parse(path)
    print(f"Glyphs: {len(ws.glyphs)}")
    print(f"Connections: {len(ws.connections)}")
    print(f"Variables: {len(ws.variables)}")
    for g in ws.glyphs:
        print(f"  {g.ident}: {g.toolbox}:{g.oname}  command={g.command!r}")
    return 0


def cmd_run(path: Path) -> int:
    """Run a workspace with the native operator registry."""
    hws = HistoricalWorkspaceParser().parse(path)
    ws = WorkspaceExecutor(example_registry()).execute(hws)
    print(f"Workspace completed: {path}")
    print(f"Nodes: {len(ws.nodes)}")
    return 0


def cmd_check() -> int:
    """Run the Phase 21 numerical compatibility checks."""
    results = run_phase21_checks()
    print(json.dumps(results, indent=2, default=str))
    skipped = sum(r["status"] == "SKIP" for r in results)
    if skipped:
        print(f"note: {skipped} check(s) skipped: historical corpus not found at {ROOT} (set KHOROS_SOURCE_ROOT)")
    return 0 if all(r["status"] in ("PASS", "SKIP") for r in results) else 1


def cmd_inventory() -> int:
    """Show the recovered historical DATAMANIP test inventory."""
    if not corpus_available():
        print(f"historical corpus not found at {ROOT}; set KHOROS_SOURCE_ROOT to enable the inventory")
        print(json.dumps({"available": False}, indent=2))
        return 0
    summary, _ = inventory()
    print(json.dumps(summary.__dict__, indent=2))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Python-native Khoros/Cantata compatibility tools")
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("inspect", help="show the contents of a workspace")
    p.add_argument("workspace", type=Path)
    p.set_defaults(func=lambda a: cmd_inspect(a.workspace))
    p = sub.add_parser("run", help="run a supported workspace")
    p.add_argument("workspace", type=Path)
    p.set_defaults(func=lambda a: cmd_run(a.workspace))
    sub.add_parser("check", help="run the Phase 21 numerical checks").set_defaults(func=lambda a: cmd_check())
    sub.add_parser("inventory", help="show the historical test inventory").set_defaults(func=lambda a: cmd_inventory())
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
