# Analyze student scores in Programming, Math, and MachineLearning using a nested dictionary. Calculate and print the average score for each student. Identify and display the top scorer in each subject.

data_5100_students = {
    "Chris": {"Programming": 85, "Math": 90, "MachineLearning": 78},
    "Robert": {"Programming": 70, "Math": 88, "MachineLearning": 92},
    "Julie": {"Programming": 95, "Math": 67, "MachineLearning": 85}
}

chris_scores = data_5100_students["Chris"]
chris_total = (chris_scores["Programming"] + chris_scores["Math"] + chris_scores["MachineLearning"])
chris_average = float(chris_total / 3)

robert_scores = data_5100_students["Robert"]
robert_total = (robert_scores["Programming"] + robert_scores["Math"] + robert_scores["MachineLearning"])
robert_average = float(robert_total / 3)

julie_scores = data_5100_students["Julie"]
julie_total = (julie_scores["Programming"] + julie_scores["Math"] + julie_scores["MachineLearning"])
julie_average = float(julie_total / 3)

programming_scores = {
    "Chris": data_5100_students["Chris"]["Programming"],
    "Robert": data_5100_students["Robert"]["Programming"],
    "Julie": data_5100_students["Julie"]["Programming"]
}
top_prog_score = max(programming_scores.values())

math_scores = {
    "Chris": data_5100_students["Chris"]["Math"],
    "Robert": data_5100_students["Robert"]["Math"],
    "Julie": data_5100_students["Julie"]["Math"]
}
top_math_score = max(math_scores.values())

machinelearning_scores = {
    "Chris": data_5100_students["Chris"]["MachineLearning"],
    "Robert": data_5100_students["Robert"]["MachineLearning"],
    "Julie": data_5100_students["Julie"]["MachineLearning"]
}
top_machinelearning_score = max(machinelearning_scores.values())

print("STUDENT AVERAGES:")
print(f"Chris - Average Score: {chris_average:.2f}")
print(f"Robert - Average Score: {robert_average:.2f}")
print(f"Julie - Average Score: {julie_average:.2f}")
print()
print("TOP SCORER IN EACH SUBJECT:")
for student in programming_scores:
    if programming_scores[student] == top_prog_score:
        print(f"Programming - Top Scorer: {student}")
for student in math_scores:
    if math_scores[student] == top_math_score:
        print(f"Math - Top Scorer: {student}")
for student in machinelearning_scores:
    if machinelearning_scores[student] == top_machinelearning_score:
        print(f"MachineLearning - Top Scorer: {student}")