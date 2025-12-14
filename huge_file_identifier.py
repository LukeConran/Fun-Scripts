import os
from pathlib import Path

def huge_file_identifier(folder, size_threshold):
    folder = Path(folder)
    large_files = []

    for folder_name, subfolders, filenames in os.walk(folder):
        folder_name = Path(folder_name)
        for filename in filenames:
            file_path = folder_name / filename
            if file_path.stat().st_size > size_threshold:
                large_files.append(file_path)

    return large_files

if __name__ == "__main__":
    p = Path('/mnt/c/Users/stlso/Pictures')
    size_limit = 30 * 1024 * 1024
    large_files = huge_file_identifier(p, size_limit)
    print(f"Files larger than {size_limit / (1024 * 1024)} MB:")
    for file in large_files:
        print(file)