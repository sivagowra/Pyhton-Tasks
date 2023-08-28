import json
student_data = [
    {"name": "siva", "english": 78, "telugu": 88, "tamil": 98, "kannada": 56, "hindi": 87},
    {"name": "nara", "english": 54, "telugu": 67, "tamil": 87, "kannada": 89, "hindi": 90},
    {"name": "mani", "english": 65, "telugu": 78, "tamil": 98, "kannada": 67, "hindi": 56}
]
for student in student_data:
    total_marks = sum(student[subject] for subject in student if subject != "name")
    student["total_marks"] = total_marks
class_topper = max(student_data, key=lambda x: x["total_marks"])

subject_toppers = {}
for subject in student_data[0]:
    if subject != "name":
        subject_toppers[subject] = max(student_data, key=lambda x: x[subject])
json_data = json.dumps(student_data, indent=4)
print(json_data)
print("Class Topper Name:", class_topper["name"])

print("Subject Toppers:")
for subject, topper in subject_toppers.items():
    print(f"{subject.capitalize()} Topper Name:", topper["name"])

