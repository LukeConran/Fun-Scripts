import zipfile, os
from pathlib import Path
import shutil

def backup_to_zip(folder):
    folder = Path(folder)

    number = 1
    while True:
        zip_filename = Path(folder.parts[-1] + '_' +str(number) + '.zip')
        if not zip_filename.exists():
            break
        number = number + 1

    # Do stuff
    print(f'Creating {zip_filename}...')
    backup_zip = zipfile.ZipFile(zip_filename, 'w')

    for folder_name, subfolders, filenames in os.walk(folder):
        folder_name = Path(folder_name)
        if '.venv' in folder_name.parts:
            continue
        print(f'Adding files in folder {folder_name}...')

        for filename in filenames:
            if '.zip' in filename:
                continue
            file_path = folder_name / filename
            print(f'Adding file {filename}...')
            backup_zip.write(file_path, arcname=file_path.relative_to(folder))

    backup_zip.close()

    os.makedirs(Path.cwd() / 'backups', exist_ok=True)
    shutil.move(str(zip_filename), Path.cwd() / 'backups' / zip_filename.name)
    print("Done.")

p = Path.cwd()
# print(p)
backup_to_zip(p)

