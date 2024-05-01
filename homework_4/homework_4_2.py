from pathlib import Path
from pprint import pprint

file_path = Path("cats_file.txt")


def get_cats_info(path):
    try:
        with open("cats_file.txt", "r", encoding="utf-8") as file:
            cats_info = []

            for line in file:
                cat_id, name, age = line.strip().split(",")
                cat = {
                    "id": cat_id,
                    "name": name,
                    "age": age

                }
                cats_info.append(cat)
        return cats_info

    except FileNotFoundError:
        print("File is not found")
    except Exception:
        print(f"The error {Exception} occurred")


cats_info = get_cats_info(file_path)
# print(cats_info)
pprint(cats_info)



