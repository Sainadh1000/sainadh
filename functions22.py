#Create a function get_scores() that:

#Asks the user to input scores for 5 subjects.

#Returns the scores as a list of floats or integers.

#Create a function calculate_average(scores) that:

#Takes the list of scores.

#Returns the average score.

#Create a function get_grade(average) that:

#Takes the average score.

#Returns the grade as a string based on this scale:

#90–100: A

#80–89: B

#70–79: C

#60–69: D

#Below 60: F

#Create a main function that:

#Calls the above functions in the correct order.

#Prints the average and the final grade.

def getscores():
    scores = []
    while True:
        score_input = input('Enter score: ')
        if score_input.isdigit():
            score_value = int(score_input)
            if 0 <= score_value <= 100:
                scores.append(score_value)
            else:
                print("Please enter a score between 0 and 100.")
        else:
            print("Invalid input. Please enter a number.")

        choice = input('Want to enter another score? (yes/no): ')
        if choice.lower() != "yes":
            break
    return scores

def calculate_avg(scores):
    if len(scores) == 0:
        return 0
    total = sum(scores)
    avg = total / len(scores)
    return avg

def getgrade(avg):
    if 90 <= avg <= 100:
        return 'A'
    elif 80 <= avg <= 89:
        return 'B'
    elif 70 <= avg <= 79:
        return 'C'
    elif 60 <= avg <= 69:
        return 'D'
    else:
        return 'F'

# Main program
scores = getscores()
average = calculate_avg(scores)
grade = getgrade(average)

print("\n--- Result ---")
print("Scores:", scores)
print("Average:", round(average, 2))
print("Grade:", grade)
