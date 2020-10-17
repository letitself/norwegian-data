import glob

print("---")
for yaml_file in glob.glob("data/*.yml"):
    with open(yaml_file, "r") as f:
        for i, line in enumerate(f.read().splitlines()):
            if i == 1:
                record = line.split()[-1]
                print(f"{record}:")
            if i > 1:
                print(f"  {line}")
