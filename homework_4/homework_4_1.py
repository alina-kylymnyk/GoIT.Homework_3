from pathlib import Path

file_path = Path("salary_file.txt")


def total_salary(path):
    total = 0
    developers = 0

    try:
        with open("salary_file.txt", "r", encoding="utf-8") as file:
            for line in file:
                developer, salary_str = line.strip().split(",")
                salary = int(salary_str)
                total += salary

                developers += 1

        if developers > 0:
            average = total / developers
        else:
            average = 0
        return total, average

    except FileNotFoundError:
        print("File is not found")
    except Exception:
        print(f"The error {Exception} occurred")


total_salary, average_salary = total_salary("path/to/salary_file.txt")
print(f"Загальна сума заробітної плати: {total_salary}, Середня заробітна плата: {average_salary}")
