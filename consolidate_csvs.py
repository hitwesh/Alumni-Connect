import os
root = r"C:\Users\hites\Downloads\InnovationProject-main"
inner = os.path.join(root, "InnovationProject-main")
for name in ["alumni_dataset.csv", "users.csv"]:
    root_path = os.path.join(root, name)
    bak_path = root_path + ".bak"
    if os.path.exists(root_path):
        if os.path.exists(bak_path):
            print(f"Backup already exists: {bak_path}")
        else:
            os.rename(root_path, bak_path)
            print(f"Moved {root_path} -> {bak_path}")
    else:
        print(f"No root file: {root_path}")

print('\nRoot directory listing:')
for f in os.listdir(root):
    print(' -', f)

print('\nInner directory listing:')
for f in os.listdir(inner):
    print(' -', f)
