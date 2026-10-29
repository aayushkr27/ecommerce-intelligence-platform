
from pathlib import Path
import ast

ROOT = Path(__file__).resolve().parent
SCRIPTS = ROOT / "scripts"

for path in sorted(SCRIPTS.rglob("*.py")):
    try:
        source = path.read_text(encoding="utf-8-sig")
        tree = ast.parse(source)

        docstring = ast.get_docstring(tree) or "No module description"
        functions = [
            node.name for node in tree.body
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        ]

        print(f"\n{'=' * 60}")
        print("FILE:", path.relative_to(ROOT))
        print("PURPOSE:", docstring.splitlines()[0])
        print("FUNCTIONS:", ", ".join(functions) or "None")

    except Exception as exc:
        print(f"\nFILE: {path.name}")
        print("ERROR:", exc)
