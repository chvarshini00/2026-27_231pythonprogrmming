print("===== STUDENT PERFORMANCE TREND ANALYSIS =====")


n = int(input("Enter number of students: "))
s = int(input("Enter number of subjects: "))
e = int(input("Enter number of examinations: "))

subjects = []

for i in range(s):
    subject = input("Enter subject name: ")
    subjects.append(subject)


exams = []

for i in range(e):
    exam = input("Enter examination name: ")
    exams.append(exam)

students = []

for i in range(n):

    print("\nEnter details for Student", i + 1)

    name = input("Student name: ")

    marks = {}

    for subject in subjects:

        print("\nEnter marks for", subject)

        subject_marks = []

        for exam in exams:

            while True:
                score = float(
                    input("Enter marks in " + exam + ": ")
                )

                if 0 <= score <= 100:
                    subject_marks.append(score)
                    break
                else:
                    print("Invalid marks! Enter between 0 and 100.")

        marks[subject] = subject_marks

    students.append({
        "name": name,
        "marks": marks
    })

print("\n========== PERFORMANCE REPORT ==========")

for student in students:

    print("\nStudent Name:", student["name"])

    total_marks = 0
    total_subjects = 0

    weak_subjects = []

    for subject in subjects:

        scores = student["marks"][subject]

        average = sum(scores) / len(scores)

        total_marks += sum(scores)
        total_subjects += len(scores)

        print("\nSubject:", subject)
        print("Examination Marks:", scores)
        print("Subject Average:", round(average, 2))

    
        if average < 40:
            weak_subjects.append(subject)

        for j in range(1, len(scores)):

            difference = scores[j] - scores[j - 1]

            if difference > 0:
                print(
                    exams[j - 1], "to", exams[j],
                    ": Improvement of", round(difference, 2)
                )

            elif difference < 0:
                print(
                    exams[j - 1], "to", exams[j],
                    ": Decline of", round(abs(difference), 2)
                )

            else:
                print(
                    exams[j - 1], "to", exams[j],
                    ": No change"
                )

    overall_average = total_marks / total_subjects

    if overall_average >= 90:
        classification = "Excellent"

    elif overall_average >= 75:
        classification = "Very Good"

    elif overall_average >= 60:
        classification = "Good"

    elif overall_average >= 40:
        classification = "Average"

    else:
        classification = "Poor"

   
    print("\n---------- FINAL STUDENT REPORT ----------")

    print("Overall Average:", round(overall_average, 2))
    print("Performance Classification:", classification)

    if weak_subjects:
        print("Consistently Weak Subjects:", weak_subjects)
    else:
        print("Consistently Weak Subjects: None")

    print("------------------------------------------")

print("\nStudent performance analysis completed.")
