from analytics import FileManager, DataLoader, ResultSaver, Report
from analytics.analyser import GpaAnalyser, CountryAnalyser

filename = "global_university_students_performance_habits_10000.csv"

fm = FileManager(filename)

if not fm.check_file():
    print("Stopping program.")
    exit()

fm.create_output_folder()

dl = DataLoader(filename)
dl.load()
dl.preview()

print("-" * 30)
print("Running all analysers:")
print("-" * 30)

analysers = [
    GpaAnalyser(dl.students),
    CountryAnalyser(dl.students)
]

for analyser in analysers:
    print(analyser)
    analyser.analyse()
    analyser.print_results()

saver = ResultSaver(analysers[0].result, "output/result.json")
report = Report(analysers[0], saver)
report.generate()