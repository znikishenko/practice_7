INPUT_FILE = "students.csv"
OUTPUT_FILE = "result.txt"

math_sum = 0
python_sum = 0
english_sum = 0

students_count = 0
best_student = ""
best_average = 0

with open(INPUT_FILE) as f:
    next(f)

    for line in f:
        line = line.strip()
        name, math, python, english = line.split(",")

        math = float(math)
        python = float(python)
        english = float(english)

        math_sum += math
        python_sum += python
        english_sum += english

        students_count += 1

        student_average = (math + python + english) / 3

        if student_average > best_average:
            best_average = student_average
            best_student = name

        math_average = math_sum / students_count
        python_average = python_sum / students_count
        english_average = english_sum / students_count

    result = f"""Середній бал по класу:
    math: {math_average:.1f}
    python: {python_average:.1f}
    english: {english_average:.1f}

    Найкращий студент: {best_student} ({best_average:.1f})
    """

    with open(OUTPUT_FILE, "w") as f:
            f.write(result)

    print(result)

