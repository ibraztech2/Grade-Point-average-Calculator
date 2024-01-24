import sys
"""'
                                                IBRAZTECH  did it
"""

def calculate_exam_grade(exam_score, test_score):
    total_score = exam_score + test_score
    if total_score >= 70:
        return 'A'
    elif total_score >= 60:
        return 'B'
    elif total_score >= 50:
        return 'C'
    elif total_score >= 40:
        return 'D'
    else:
        return 'F'

def input_collector():
    no_of_courses = int(input('Input the number of courses you are offering: '))
    aggregat_score = 0
    aggregat_score_unit = 0
    
    courses = []
    for i in range(no_of_courses):
        course_name = input(f'Enter the name of course {i + 1}: ')
        course_unit = eval(input(f'Enter the course unit for {course_name}: '))
        test_score = eval(input(f'Enter your test score for {course_name}: '))
        exam_score = eval(input(f'Enter your exam score for {course_name}: '))
        
        grade = calculate_exam_grade(exam_score, test_score)
        unit_scored = return_Unit(grade) * course_unit
        aggregat_score += unit_scored
        aggregat_score_unit += course_unit

        courses.append({
            'Course Name': course_name,
            'Course Unit': course_unit,
            'Test Score': test_score,
            'Exam Score': exam_score,
            'Grade': grade
        })
    gpa_calculator_(aggregat_score_unit,aggregat_score,courses)
    return courses
def return_Unit(grade_scored):
    if grade_scored == 'A':
        return 5
    elif grade_scored == "B":
        return 4
    elif grade_scored == "c":
        return 3
    elif grade_scored == "D":
        return 2
    elif grade_scored == "E":
        return 1
    else:
        return 0
def gpa_calculator_(total_course_unit, total_unit_scored,courses):
    gpa_ = total_unit_scored/total_course_unit
    print(total_course_unit,total_unit_scored)
    prompt_user = input(' Do you want to see your Grade point average ? ').strip().upper()
    if prompt_user:
        print(f'your GPA for the semester is {gpa_:.2f}')
    else:
        print(courses)




def main():
    welcome_letter = input("Welcome to this platform. Press Enter to continue: ")
    courses = input_collector()

    for course in courses:
        print(f"Course: {course['Course Name']}, Exam Score: {course['Exam Score']}, Test Score: {course['Test Score']}, Grade: {course['Grade']}, Course Unit: {course['Course Unit']}")

if __name__ == "__main__":
    main()



''' 
                                              writer :  IBRAZTECH
'''