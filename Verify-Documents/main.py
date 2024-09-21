import hashlib
import json
import os


def generate_hash(value):
    return hashlib.sha256(value).hexdigest()


def save_json(data):
    with open("hashes.json", "w") as f:
        json.dump(data, f, indent=2)


def read_json():
    with open("hashes.json", "rb") as f:
        return json.load(f, parse_int=1)


def hash_files():
    num_of_files = os.listdir("Documents")
    file_data = {}

    for _, value in enumerate(num_of_files):
        with open(f"Documents/{value}", "rb") as f:
            data = f.read()
        file_data[value] = generate_hash(data)

    if not file_data:
        return "The files are empty"

    return file_data


def save_hashes():
    file_data = hash_files()
    save_json(file_data)

    return file_data


def check_hashes():
    saved_hashes = read_json()
    if not saved_hashes:
        return "No saved hashes found."

    current_hashes = hash_files()
    if not current_hashes:
        return "No files found to hash."

    altered_files = [file for file in saved_hashes if saved_hashes.get(file) != current_hashes.get(file)]
    missing_files = set(saved_hashes.keys()) - set(current_hashes.keys())
    new_files = set(current_hashes.keys()) - set(saved_hashes.keys())

    messages = []
    if altered_files:
        messages.append(f"Altered files: {', '.join(altered_files)}")
    if missing_files:
        messages.append(f"Missing files: {', '.join(missing_files)}")
    if new_files:
        messages.append(f"New files: {', '.join(new_files)}")

    return "Files are not altered." if not messages else " | ".join(messages)


print(save_hashes())
# print(check_hashes())
