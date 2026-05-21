from pathlib import Path

downloads_path = Path.home() / "Downloads"

files = list(downloads_path.iterdir())

for file in files:
    ext = file.suffix.lower()

    if ext == ".pdf":
        print("PDF:", file.name)

    elif ext in {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"}:
        print("圖片:", file.name)

    elif ext in {".zip", ".rar", ".7z", ".tar", ".gz"}:
        print("壓縮檔:", file.name)

    elif ext in {".doc", ".docx", ".odt"}:
        print("文件檔:", file.name)

    elif ext in {".xls", ".xlsx", ".csv"}:
        print("試算表:", file.name)

    elif ext in {".ppt", ".pptx"}:
        print("簡報檔:", file.name)

    elif ext in {".py", ".js", ".ts", ".java", ".c", ".cpp", ".cs"}:
        print("程式檔:", file.name)

    elif ext in {".mp3", ".wav", ".flac"}:
        print("音樂檔:", file.name)

    elif ext in {".mp4", ".mkv", ".mov", ".avi"}:
        print("影片檔:", file.name)

    elif ext in {".exe", ".msi", ".bat", ".cmd", ".ps1", ".app", ".bin"}:
        print("執行檔:", file.name)

    else:
        print("其他檔案:", file.name)