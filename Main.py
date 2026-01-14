import json

FILENAME = "courses.json"

def save_courses(courses, filename):
    with open(filename, "w") as f:
        json.dump(courses, f, indent=2)

def load_courses(filename):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print("No saved file found yet.")
        return {}


courses = {}
GRADE_POINTS = {"A": 4.0, "A-": 3.7,
        "B+": 3.3, "B": 3.0, "B-": 2.7,
        "C+": 2.3, "C": 2.0, "C-": 1.7,
        "D+": 1.3, "D": 1.0, "D-": 0.7,
        "F": 0.0}

while True:
    selection = input("What would you like to do \n1. Add Course\n2. Remove Course\n3. Calculate GPA\n4. View All Courses\n5. Save\n6. Load\n7. Quit\n ").strip().lower()


    if selection in ("7", "quit"):
        break

    elif selection in ("1", "add course"):
        name = input("Course Name: ").strip().lower()
        letter_grade = input("Letter Grade: ").upper().strip()
        if letter_grade not in GRADE_POINTS:
            print("Not a valid Grade")
            continue
        credits = int(input("Credits: " ))

        courses[name] = {"Grade" : letter_grade, "Credits": credits}

    elif selection in ("2", "remove course"):
        course = input("What is the name of the course would you like to remove?").strip().lower()
        if course in courses:
            del courses[course]
        else:
            print("course not found")

    elif selection in ("3", "calculate gpa"):
        if len(courses) == 0:
            print("no courses yet")
            continue
        quality_points = 0
        total_credits = 0

        grades = [info["Grade"] for info in courses.values()]
        credits = [info["Credits"] for info in courses.values()]
        for i in range(len(credits)):
            total_credits += credits[i]
            
        for i in range(len(grades)):
            quality_points += credits[i] * GRADE_POINTS[grades[i]] 
        gpa = quality_points / total_credits
        print("GPA: ", gpa)
            
    elif selection in ("4", "view all courses"):
        print(courses)
    
    elif selection in ("5", "save"):
        save_courses(courses, FILENAME)
        print("Saved!")

    elif selection in ("6", "load"):
        courses = load_courses(FILENAME)
        print("Loaded!")










