from pathlib import Path
import shutil

downloads_path = Path.home() / "Downloads"

categories = {
    "PDF": {".pdf"},
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
    "Documents": {".doc", ".docx", ".odt"},
    "Spreadsheets": {".xls", ".xlsx", ".csv"},
    "Presentations": {".ppt", ".pptx"},
    "Code": {".py", ".js", ".ts", ".java", ".c", ".cpp", ".cs"},
    "Music": {".mp3", ".wav", ".flac"},
    "Videos": {".mp4", ".mkv", ".mov", ".avi"},
    "Executables": {".exe", ".msi", ".bat", ".cmd", ".ps1", ".app", ".bin"},
}

for folder_name in categories:
    (downloads_path / folder_name).mkdir(exist_ok=True)

files = list(downloads_path.iterdir())

for file in files:
    if not file.is_file():
        continue

    ext = file.suffix.lower()
    destination_folder = None

    for folder_name, extensions in categories.items():
        if ext in extensions:
            destination_folder = downloads_path / folder_name
            break

    if destination_folder is None:
        continue

    destination = destination_folder / file.name
    shutil.move(str(file), str(destination))
    print(f"Moved {folder_name}: {file.name}")