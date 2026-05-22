from pathlib import Path
import shutil
import logging

downloads_path = Path.home() / "Downloads"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="organize_folders.log",
    encoding="utf-8",
)
logger = logging.getLogger(__name__)

categories = {
    "PDF": {".pdf"},
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
    "Documents": {".doc", ".docx", ".odt", ".txt"},
    "Spreadsheets": {".xls", ".xlsx", ".csv"},
    "Presentations": {".ppt", ".pptx"},
    "Code": {".py", ".js", ".ts", ".java", ".c", ".cpp", ".cs"},
    "Music": {".mp3", ".wav", ".flac"},
    "Videos": {".mp4", ".mkv", ".mov", ".avi"},
    "Executables": {".exe", ".msi", ".bat", ".cmd", ".ps1", ".app", ".bin"},
}

logger.info("Organizing downloads folder: %s", downloads_path)

for folder_name in categories:
    folder_path = downloads_path / folder_name
    folder_path.mkdir(exist_ok=True)
    logger.debug("Ensured folder exists: %s", folder_path)

files = list(downloads_path.iterdir())

for file in files:
    if not file.is_file():
        logger.debug("Skipped non-file entry: %s", file.name)
        continue

    ext = file.suffix.lower()
    destination_folder = None

    for folder_name, extensions in categories.items():
        if ext in extensions:
            destination_folder = downloads_path / folder_name
            break

    if destination_folder is None:
        logger.info("No category for file, skipping: %s", file.name)
        continue

    destination = destination_folder / file.name
    try:
        shutil.move(str(file), str(destination))
        logger.info("Moved %s: %s", folder_name, file.name)
    except FileExistsError:
        logger.warning("File name conflict, destination already exists: %s", file.name)
    except PermissionError as e:
        if "被另一個處理程序使用" in str(e) or "being used" in str(e):
            logger.warning("File is in use, cannot move: %s", file.name)
        else:
            logger.error("Permission denied, cannot move: %s", file.name)
    except Exception as e:
        logger.error("Unexpected error moving %s: %s", file.name, str(e))