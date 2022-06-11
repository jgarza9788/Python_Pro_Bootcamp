student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}
# ^this is not needed

#TODO-2: Write your code below to add the grades to student_grades.👇
def convert_scores_to_grades(scores):
    # Scores 91 - 100: Grade = "Outstanding"
    # Scores 81 - 90: Grade = "Exceeds Expectations"
    # Scores 71 - 80: Grade = "Acceptable"
    # Scores 70 or lower: Grade = "Fail"

    result = {}

    for i in scores:
        score = scores[i]
        grade = ''

        if score >= 91:
            grade = 'Outstanding'
        elif score >= 81:
            grade = 'Exceeds Expectations'
        elif score >= 71:
            grade = 'Acceptable'
        else:
            grade = 'Fail'
        
        result[i] = grade

    return result


student_grades = convert_scores_to_grades(student_scores)

# 🚨 Don't change the code below 👇
print(student_grades)

