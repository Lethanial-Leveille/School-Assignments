import os
from collections import defaultdict
import matplotlib.pyplot as plt


# ---------- load students ---------- #

def load_students(path="data/students.txt"):
    """
    students.txt lines look like:
    174Michael Potter
    564Robert Wheeler

    First 3 chars = id, rest = name.
    """
    students_by_name = {}
    students_by_id = {}

    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                student_id = line[:3]
                name = line[3:].strip()
                if not name:
                    continue
                students_by_name[name] = student_id
                students_by_id[student_id] = name
    except FileNotFoundError:
        print("Could not find", path)
        exit(1)

    return students_by_name, students_by_id


# ---------- load assignments ---------- #

def load_assignments(path="data/assignments.txt"):
    """
    assignments.txt is in blocks of 3 lines:
    Quiz 1
    60807
    25
    Quiz 2
    99909
    25
    ...
    """
    assignments_by_name = {}
    assignments_by_id = {}

    try:
        with open(path, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("Could not find", path)
        exit(1)

    if len(lines) % 3 != 0:
        print("assignments.txt format is not groups of 3 lines")
        # still try to read what we can

    for i in range(0, len(lines) - 2, 3):
        name = lines[i].strip()
        assignment_id = lines[i + 1].strip()
        points_str = lines[i + 2].strip()

        try:
            points = float(points_str)
        except ValueError:
            continue

        assignments_by_name[name] = {"id": assignment_id, "points": points}
        assignments_by_id[assignment_id] = {"name": name, "points": points}

    return assignments_by_name, assignments_by_id


# ---------- load submissions ---------- #

def load_submissions():
    """
    Each file in data/submissions has lines like:
    132|68047|76

    student_id | assignment_id | percent
    """
    submissions_by_student = defaultdict(list)
    submissions_by_assignment = defaultdict(list)

    submissions_dir = os.path.join("data", "submissions")
    submissions_file = os.path.join("data", "submissions.txt")

    def read_one_file(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    parts = [p.strip() for p in line.split("|")]
                    if len(parts) < 3:
                        continue
                    student_id, assignment_id, percent_str = parts[0], parts[1], parts[2]
                    try:
                        percent = float(percent_str)
                    except ValueError:
                        continue
                    submissions_by_student[student_id].append((assignment_id, percent))
                    submissions_by_assignment[assignment_id].append(percent)
        except FileNotFoundError:
            pass

    # case 1: directory of text files
    if os.path.isdir(submissions_dir):
        for filename in os.listdir(submissions_dir):
            if filename.endswith(".txt"):
                full_path = os.path.join(submissions_dir, filename)
                read_one_file(full_path)
    # case 2: single big file
    elif os.path.isfile(submissions_file):
        read_one_file(submissions_file)
    else:
        print("Could not find submissions data")
        exit(1)

    return submissions_by_student, submissions_by_assignment


# ---------- option 1: student grade ---------- #

def handle_student_grade(students_by_name, assignments_by_id, submissions_by_student):
    name = input("What is the student's name: ").strip()

    if name not in students_by_name:
        print("Student not found")
        return

    student_id = students_by_name[name]
    submissions = submissions_by_student.get(student_id, [])

    if not submissions:
        print("0%")
        return

    total_points_earned = 0.0
    total_points_possible = 0.0

    for assignment_id, percent in submissions:
        info = assignments_by_id.get(assignment_id)
        if not info:
            continue
        points = info["points"]
        total_points_possible += points
        total_points_earned += (percent / 100.0) * points

    if total_points_possible == 0:
        print("0%")
        return

    grade_percent = round((total_points_earned / total_points_possible) * 100)
    print(f"{grade_percent}%")


# ---------- option 2: assignment stats ---------- #

def handle_assignment_stats(assignments_by_name, submissions_by_assignment):
    name = input("What is the assignment name: ").strip()

    if name not in assignments_by_name:
        print("Assignment not found")
        return

    assignment_id = assignments_by_name[name]["id"]
    scores = submissions_by_assignment.get(assignment_id, [])

    if not scores:
        print("Assignment not found")
        return

    min_score = round(min(scores))
    max_score = round(max(scores))
    avg_score = round(sum(scores) / len(scores))

    print(f"Min: {min_score}%")
    print(f"Avg: {avg_score}%")
    print(f"Max: {max_score}%")


# ---------- option 3: assignment graph ---------- #

def handle_assignment_graph(assignments_by_name, submissions_by_assignment):
    name = input("What is the assignment name: ").strip()

    if name not in assignments_by_name:
        print("Assignment not found")
        return

    assignment_id = assignments_by_name[name]["id"]
    scores = submissions_by_assignment.get(assignment_id, [])

    if not scores:
        print("Assignment not found")
        return

    plt.hist(scores, bins=[0, 25, 50, 75, 100])
    plt.title(name)
    plt.xlabel("Score (%)")
    plt.ylabel("Number of students")
    plt.show()


# ---------- main ---------- #

def main():
    students_by_name, students_by_id = load_students()
    assignments_by_name, assignments_by_id = load_assignments()
    submissions_by_student, submissions_by_assignment = load_submissions()

    print("1. Student grade")
    print("2. Assignment statistics")
    print("3. Assignment graph")
    print()
    selection = input("Enter your selection: ")

    if selection == "1":
        handle_student_grade(students_by_name, assignments_by_id, submissions_by_student)
    elif selection == "2":
        handle_assignment_stats(assignments_by_name, submissions_by_assignment)
    elif selection == "3":
        handle_assignment_graph(assignments_by_name, submissions_by_assignment)
    else:
        # spec says we don't have to handle invalid input
        pass


if __name__ == "__main__":
    main()

