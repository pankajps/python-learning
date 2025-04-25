import os

def generate_tree(root_dir, prefix=""):
    entries = os.listdir(root_dir)
    entries = sorted(e for e in entries if not e.startswith(".") and e != "README.md")
    tree = []

    for idx, entry in enumerate(entries):
        path = os.path.join(root_dir, entry)
        connector = "├── " if idx < len(entries) - 1 else "└── "
        tree.append(prefix + connector + entry)

        if os.path.isdir(path):
            extension = "│   " if idx < len(entries) - 1 else "    "
            tree.extend(generate_tree(path, prefix + extension))

    return tree

if __name__ == "__main__":
    structure = generate_tree("/root/python_practice")
    print("```\n" + "\n".join(structure) + "\n```")

