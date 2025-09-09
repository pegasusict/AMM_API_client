import os
import sys

GRAPHQL_DIR = os.path.join(os.path.dirname(__file__), "..", "gql")
INIT_FILE = os.path.join(GRAPHQL_DIR, "__init__.py")


def update_init() -> bool:
    """Update gql/__init__.py with constants for all .graphql files.
    Returns True if file was changed, False otherwise.
    """
    files = [f for f in os.listdir(GRAPHQL_DIR) if f.endswith(".graphql")]
    files.sort()

    lines = [
        '"""Auto-generated: exposes all GraphQL files as constants."""',
        "import os",
        "",
        "BASE_DIR = os.path.dirname(__file__)",
        "",
    ]

    for filename in files:
        const_name = filename.replace(".graphql", "").upper()
        lines.append(f'{const_name} = os.path.join(BASE_DIR, "{filename}")')

    content = "\n".join(lines) + "\n"

    old_content = ""
    if os.path.exists(INIT_FILE):
        with open(INIT_FILE, "r", encoding="utf-8") as f:
            old_content = f.read()

    if old_content != content:
        with open(INIT_FILE, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ Updated {INIT_FILE} with {len(files)} GraphQL files.")
        return True
    return False


if __name__ == "__main__":
    changed = update_init()
    sys.exit(1 if changed else 0)  # pre-commit fails if changes were made
