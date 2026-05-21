from pathlib import Path

downloads_path = Path.home() / "Downloads"

files = list(downloads_path.iterdir())

for file in files:
    print(file.name)