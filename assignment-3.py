import os
import csv
import json

filename = "global_university_students_performance_habits_10000.csv"

print("Checking file...")

if not os.path.exists(filename):
    print(f"Error: {filename} not found. Please download the file from LMS.")
    exit()

print(f"File found: {filename}")

print("Checking output folder...")

if not os.path.exists("output"):
    os.makedirs("output")
    print("Output folder created: output/")
else:
    print("Output folder already exists: output/")


# Task A2 — Read CSV and Preview Data

students = []

with open(filename, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        students.append(row)

print(f"Total students: {len(students)}")

print("First 5 rows:")
print("-" * 30)

for student in students[:5]:
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


# Task A3 — GPA Analysis

gpas = []
high_gpa_count = 0

for student in students:
    gpa = float(student["GPA"])
    gpas.append(gpa)

    if gpa > 3.5:
        high_gpa_count += 1

avg_gpa = sum(gpas) / len(gpas)
max_gpa = max(gpas)
min_gpa = min(gpas)

avg_gpa = round(avg_gpa, 2)

print("-" * 30)
print("GPA Analysis")
print("-" * 30)
print(f"Total students : {len(students)}")
print(f"Average GPA : {avg_gpa}")
print(f"Highest GPA : {max_gpa}")
print(f"Lowest GPA : {min_gpa}")
print(f"Students GPA>3.5 : {high_gpa_count}")
print("-" * 30)


# Task A4 — Save Results to JSON and Print Summary

result = {
    "analysis": "GPA Statistics",
    "total_students": len(students),
    "average_gpa": avg_gpa,
    "max_gpa": max_gpa,
    "min_gpa": min_gpa,
    "high_performers": high_gpa_count
}

with open("output/result.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=4)

print("=" * 30)
print("ANALYSIS RESULT")
print("=" * 30)
print(f"Analysis : {result['analysis']}")
print(f"Total students : {result['total_students']}")
print(f"Average GPA : {result['average_gpa']}")
print(f"Highest GPA : {result['max_gpa']}")
print(f"Lowest GPA : {result['min_gpa']}")
print(f"High performers : {result['high_performers']}")
print("=" * 30)
print("Result saved to output/result.json")