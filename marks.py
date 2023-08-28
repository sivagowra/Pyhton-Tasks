import csv

with open('marks.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    header = None
    marks = []
    for row in spamreader:
        if not header:
            header = row
            header.append("Total")
        else:
            student = row[1:]
            student = [int(n.strip()) for n in student]
            student.append(sum(student))
            student.insert(0, row[0])

            marks.append(student)

    sorted_marks = sorted(marks, key=lambda row: row[6], reverse=True)
    topper = sorted_marks[0]
    print("Total Topper: ", topper[0])
    
    print("Subject-wise toppers:")
    for subject_index in range(1, 6):
        subject_name = header[subject_index]
        subject_toppers = sorted(marks, key=lambda row: row[subject_index], reverse=True)
        subject_topper = subject_toppers[0]
        print(f"{subject_name} Topper: {subject_topper[0]} - Marks: {subject_topper[subject_index]}")
