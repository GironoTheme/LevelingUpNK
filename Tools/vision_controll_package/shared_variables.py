from pathlib import Path
import os

name_of_window = 'NIGHT CROWS'


def find_file(file_name):
    drives = [f"{chr(drive)}:\\" for drive in range(ord('A'), ord('Z') + 1) if os.path.exists(f"{chr(drive)}:\\")]
    for drive in drives:
        for root_path in Path(drive).rglob(file_name):
            return root_path


path_to_pytesseract = find_file('tesseract.exe')

