import argparse
import shutil
from datetime import datetime
from pathlib import Path


parser = argparse.ArgumentParser(description="Sort files by extension")
parser.add_argument("directory", help="Directory to sort files by extension")
args = parser.parse_args()

directory_path = Path(args.directory)

if not directory_path.exists():
    print(f"Directory {directory_path} does not exist!")
    exit(1)

for file_ in directory_path.iterdir():
    if file_.is_file():
        ext = file_.suffix[1:]

        if ext:
            target_folder = directory_path / ext
            target_folder.mkdir(exist_ok=True)

            base_name = file_.stem
            timestamp = datetime.now().strftime("%Y-%m-%d")
            new_name = f"{base_name}_{timestamp}{file_.suffix}"

            shutil.move(str(file_), str(target_folder / new_name))

print("Files sorted by extension")