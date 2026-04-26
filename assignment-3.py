import os
import csv

filename = "global_university_students_performance_habits_10000.csv"


def check_files():
    print("Checking file...")

    if not os.path.exists(filename):
        print(f"Error: {filename} not found. Please download the file from LMS.")
        return False

    print(f"File found: {filename}")

    print("Checking output folder...")

    if not os.path.exists("output"):
        os.makedirs("output")
        print("Output folder created: output/")
    else:
        print("Output folder already exists: output/")

    return True


def load_data(filename):
    print("Loading data...")

    students = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                students.append(row)

        print(f"Data loaded successfully: {len(students)} students")
        return students

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found. Please check the filename.")
        return []

    except Exception as error:
        print(f"Error: Something went wrong while loading data: {error}")
        return []


def preview_data(students, n=5):
    print(f"First {n} rows:")
    print("-" * 30)

    for student in students[:n]:
        print(
            student["student_id"],
            "|",
            student["age"],
            "|",
            student["gender"],
            "|",
            student["country"],
            "| GPA:",
            student["GPA"]
        )

    print("-" * 30)



def analyse_gpa(students):
    gpas = []
    high_gpa_count = 0

    for student in students:
        try:
            gpa = float(student["GPA"])
            gpas.append(gpa)

            if gpa > 3.5:
                high_gpa_count += 1

        except ValueError:
            print(f"Warning: could not convert value for student {student['student_id']} — skipping row.")
            continue

    avg_gpa = sum(gpas) / len(gpas)
    max_gpa = max(gpas)
    min_gpa = min(gpas)

    avg_gpa = round(avg_gpa, 2)

    result = {
        "total_students": len(students),
        "average_gpa": avg_gpa,
        "max_gpa": max_gpa,
        "min_gpa": min_gpa,
        "high_performers": high_gpa_count
    }

    return result


def lambda_map_filter(students):
    high_gpa = list(filter(lambda s: float(s["GPA"]) > 3.8, students))
    print(f"Students with GPA > 3.8 : {len(high_gpa)}")

    gpa_values = list(map(lambda s: float(s["GPA"]), students))
    print(f"GPA values (first 5) : {gpa_values[:5]}")

    hard_workers = list(filter(lambda s: float(s["study_hours_per_day"]) > 4, students))
    print(f"Students studying > 4 hrs : {len(hard_workers)}")


if check_files():
    students = load_data(filename)
    preview_data(students)

    result = analyse_gpa(students)

    print("-" * 30)
    print("GPA Analysis")
    print("-" * 30)
    print(f"Total students : {result['total_students']}")
    print(f"Average GPA : {result['average_gpa']}")
    print(f"Highest GPA : {result['max_gpa']}")
    print(f"Lowest GPA : {result['min_gpa']}")
    print(f"Students GPA>3.5 : {result['high_performers']}")
    print("-" * 30)

    print("-" * 30)
    print("Lambda / Map / Filter")
    print("-" * 30)
    lambda_map_filter(students)
    print("-" * 30)

    load_data(filename)
    load_data("wrong_file.csv")