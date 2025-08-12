# Initialization
print("The quiz is starting...")


# This is a simple quiz program
correct_1 = input("What is the capital of France? ")
if correct_1.lower() == "paris":
    print("Correct!")
else:
    print ("Incorrect!")

correct_2 = input("What is the capital of the United States? ")
if correct_2 == "Washington":
    print("Correct!")
else:
    print ("Incorrect!")
    

correct_3 = input("What is the capital of Arizona? ")
if correct_3.lower() == "Phoenix":
    print("Correct!")
else:
    print ("Incorrect!")


correct_4 = input("What is the capital of Georgia?")
if correct_4.lower() == "Atlanta":
    print("Correct!")
else:
    print ("Incorrect!")


correct_5 = input("What is the capital of Chile?")
if correct_5.lower() == "Santiago":
    print("Correct!")
else:
    print ("Incorrect!")


# if: 
#     correct_1.lower() == "paris"
#     correct_2 == "Washington", 
#     correct_3.lower() == "Phoenix", 
#     correct_4.lower() == "Atlanta", 
#     correct_5.lower() == "Santiago"
#     print("You got all of them correct.")



# Check Percentage
total_questions = 5
correct_answers = 0
if correct_1.lower() == "paris":
    correct_answers += 1
if correct_2 == "washington":
    correct_answers += 1
if correct_3.lower() == "phoenix":
    correct_answers += 1
if correct_4.lower() == "atlanta":
    correct_answers += 1
if correct_5.lower() == "santiago":
    correct_answers += 1
percentage = (correct_answers / total_questions) * 100
print(f"You answered {correct_answers} out of {total_questions} questions correctly.")
print(f"Your score is {percentage}%.")




print("The quiz is over. Thanks for playing!")

