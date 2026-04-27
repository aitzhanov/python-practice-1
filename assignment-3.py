import os
import csv
import json

filename = "global_university_students_performance_habits_10000.csv"


class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        print("Checking file...")

        if os.path.exists(self.filename):
            print(f"File found: {self.filename}")
            return True
        else:
            print(f"Error: {self.filename} not found. Please download the file from LMS.")
            return False

    def create_output_folder(self, folder="output"):
        print("Checking output folder...")

        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Output folder created: {folder}/")
        else:
            print(f"Output folder already exists: {folder}/")



class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        print("Loading data...")

        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    self.students.append(row)

            print(f"Data loaded successfully: {len(self.students)} students")
            return self.students

        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found. Please check the filename.")
            return []

    def preview(self, n=5):
        print(f"First {n} rows:")
        print("-" * 30)

        for student in self.students[:n]:
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



class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        gpas = []
        high_gpa_count = 0

        for student in self.students:
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

        self.result = {
            "total_students": len(self.students),
            "average_gpa": avg_gpa,
            "max_gpa": max_gpa,
            "min_gpa": min_gpa,
            "high_performers": high_gpa_count
        }

        return self.result

    def print_results(self):
        print("-" * 30)
        print("GPA Analysis")
        print("-" * 30)
        print(f"Total students : {self.result['total_students']}")
        print(f"Average GPA : {self.result['average_gpa']}")
        print(f"Highest GPA : {self.result['max_gpa']}")
        print(f"Lowest GPA : {self.result['min_gpa']}")
        print(f"Students GPA>3.5 : {self.result['high_performers']}")
        print("-" * 30)



class ResultSaver:
    def __init__(self, result, output_path):
        self.result = result
        self.output_path = output_path

    def save_json(self):
        try:
            with open(self.output_path, "w", encoding="utf-8") as f:
                json.dump(self.result, f, indent=4)

            print(f"Result saved to {self.output_path}")

        except Exception as error:
            print(f"Error: could not save result: {error}")



fm = FileManager(filename)

if not fm.check_file():
    print("Stopping program.")
    exit()

fm.create_output_folder()

dl = DataLoader(filename)
dl.load()
dl.preview()

analyser = DataAnalyser(dl.students)
analyser.analyse()
analyser.print_results()

saver = ResultSaver(analyser.result, "output/result.json")
saver.save_json()