import pandas as pd
from model import model

print("This personality test is going to predict your personality type based on the Big 5 Personality traits.")
print("Max required time: 1hr.")

print("Enter your Gender: ")
gender = input()
if gender == "Male".upper():
    gender = 1
else:
    gender = 0

age = int(input("Enter your age: "))

print("This program will tell what personality suits you...\n")

print("\n1. OPENNESS "
      "for more info. visit https://www.psychologytoday.com/us/basics/openness")
print("Rate your openness from 0 to 9: ")
print("If you want to find out how Open-minded you are!?.. You can take this openness test --> "
      "https://www.truity.com/test/how-open-are-you ")
openness = int(input("Enter your openness score (0-9):"))

print("\n2. NEUROTICISM "
      "for more info. visit https://www.psychologytoday.com/us/basics/neuroticism")
print("Rate your neuroticism from 0 to 9: ")
print("To know your Neurotic score, visit --> "
      "https://www.psychologistworld.com/influence-personality/five-factor-test/neuroticism-quiz")
neuroticism = int(input("Enter your neurotic score(0-9): "))

print("\n3. CONSCIENTIOUSNESS "
      "for more info. visit https://www.psychologytoday.com/us/basics/conscientiousness")
print("Rate your conscientiousness from 0 to 9: ")
print("To know your Conscientiousness score, visit --> "
      "https://www.psychologistworld.com/influence-personality/five-factor-test/conscientiousness-test")
conscientiousness = int(input("Enter your conscientiousness score (0-9): "))

print("\n4. AGREEABLENESS "
      "for more info. visit https://www.psychologytoday.com/us/basics/agreeableness")
print("Rate your neuroticism from 0 to 9: ")
print("To know your Agreeableness score, visit --> "
      "https://www.truity.com/test/how-agreeable-are-you")
agreeableness = int(input("Enter your agreeable score (0-9): "))

print("\n5. EXTROVERSION "
      "for more info. visit https://www.psychologytoday.com/us/basics/extroversion")
print("Rate your extroversion from 0 to 9: ")
print("To know your Extroversion score, visit --> "
      "https://www.psychologytoday.com/us/tests/personality/extroversion-introversion-test")
extroversion = int(input("Enter your agreeable score (0-9): "))

X = [[gender, age, openness, neuroticism, conscientiousness, agreeableness, extroversion]]
data = pd.DataFrame(X)
print("\n\nYour expected personality is: ", model.predict(data)[0])

print("Thank You! For taking this test. ")
