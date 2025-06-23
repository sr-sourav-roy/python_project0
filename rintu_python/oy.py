# Function to find the maximum marks
def FindMax(scores):
    max_score = max(scores)
    print("Highest marks:", max_score)

# Function to find the minimum marks
def FindLeast(scores):
    min_score = min(scores)
    print("Lowest marks:", min_score)

# Function to calculate the average of the scores
def FindAverage(scores):
    average = sum(scores) / len(scores)
    return average

# Function to count the number of passing students
def Find_Passing_Students(scores, passing_mark):
    passing_students = [score for score in scores if score >= passing_mark]
    print("Number of passing students:", len(passing_students))

# Function to check if a student has passed
def check_Pass(score):
    passing_marks = 60
    return score >= passing_marks

# Function to assign grade based on the score
def get_Grade(score):
    if score >= 90:
        return "A+"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

# Sample usage
class_scores = [80, 30, 50, 80, 60, 55]

# Calling the functions
FindMax(class_scores)
FindLeast(class_scores)
average = FindAverage(class_scores)
print("Average marks:", average)
Find_Passing_Students(class_scores, 60)

# Example: Check if a student with 55 passed
result = check_Pass(55)
print("Did the student pass (55)?", result)

# Example: Get grade for a score of 80
grade = get_Grade(80)
print("Grade for score 80:", grade)