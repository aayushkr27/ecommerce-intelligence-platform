
from pathlib import Path
import re
import shutil
import sys

ROOT = Path(__file__).resolve().parent
SCRIPTS = ROOT / "scripts"
BACKUP = ROOT / "scripts_backup_before_reorganization"

# Files that should remain directly inside scripts/
KEEP_IN_ROOT = {
    "load_staging.py",
    "inventory_scripts.py",
    "organize_scripts.py",
    "project_paths.py",
}

def classify(filename):
    name = filename.lower()

    if "final" in name and "audit" in name:
        return "final_audits"

    if "profile" in name or "profiling" in name:
        return "profiling"

    if name.startswith(("01_profile", "02_inspect", "03_inspect")):
        return "profiling"

    investigation_terms = (
        "investigate", "anomal", "duplicate", "mismatch",
        "discrepanc", "high_price", "zero_freight",
        "zero_payment", "zip_variability",
    )
    if any(term in name for term in investigation_terms):
        return "investigations"

    return "quality_checks"


def main():
    apply_changes = "--apply" in sys.argv

    if not SCRIPTS.is_dir():
        raise FileNotFoundError(f"Scripts folder not found: {SCRIPTS}")

    folders = [
        "profiling",
        "quality_checks",
        "investigations",
        "final_audits",
    ]

    for folder in folders:
        (SCRIPTS / folder).mkdir(exist_ok=True)

    plans = []

    # Only classify Python files directly inside scripts/.
    for source in sorted(SCRIPTS.glob("*.py")):
        if source.name in KEEP_IN_ROOT:
            continue

        destination_folder = classify(source.name)
        destination = SCRIPTS / destination_folder / source.name

        if destination.exists():
            print(f"SKIP: destination already exists: {destination}")
            continue

        content = source.read_text(encoding="utf-8-sig")

        # Update the common project-root expression for a script
        # moved one level deeper.
        updated = re.sub(
            r"(?m)^(PROJECT_DIR\s*=\s*Path\(__file__\)"
            r"\.resolve\(\))\.parent\.parent\b",
            r"\1.parents[2]",
            content,
        )

        # Warn if the script uses __file__ but its paths need review.
        if "__file__" in content and updated == content:
            print(f"REVIEW PATHS: {source.name}")

        plans.append((source, destination, updated))

    print("\nPLANNED MOVES")
    for source, destination, updated in plans:
        changed = updated != source.read_text(encoding="utf-8-sig")
        print(
            f"{source.name} -> {destination.parent.name}/"
            f"{destination.name}"
            f"{' [path updated]' if changed else ''}"
        )

    if not apply_changes:
        print("\nDRY RUN ONLY: no Python files were moved.")
        print("Review the plan. If it looks correct, run:")
        print("python organize_scripts.py --apply")
        return

    if BACKUP.exists():
        raise FileExistsError(
            f"Backup already exists: {BACKUP}\n"
            "Rename it or choose another backup name before proceeding."
        )

    # Back up the complete scripts folder before modifying anything.
    shutil.copytree(SCRIPTS, BACKUP)

    moved = []

    try:
        for source, destination, updated in plans:
            if updated != source.read_text(encoding="utf-8-sig"):
                source.write_text(updated, encoding="utf-8")

            shutil.move(str(source), str(destination))
            moved.append((source, destination))

    except Exception:
        print("\nAn error occurred. Restoring the scripts folder...")
        if SCRIPTS.exists():
            shutil.rmtree(SCRIPTS)
        shutil.copytree(BACKUP, SCRIPTS)
        raise

    print(f"\nCompleted: {len(moved)} Python files moved.")
    print(f"Backup saved at: {BACKUP}")
    print("Review the folders and test important scripts before deleting the backup.")


if __name__ == "__main__":
    main()
