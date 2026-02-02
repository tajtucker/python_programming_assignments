#Repeat Part-1 using a for loop.

names_list = []
scores_list = []

numof_students = int(input("Enter number of students: "))

for x in range(numof_students):
    name = input("Enter name: ")
    names_list.append(name)

    score = float(input("Enter score: "))
    scores_list.append(score)

highest_score = max(scores_list)
index = scores_list.index(highest_score)
highest_name = names_list[index]

print(f"{highest_name} has the highest score {highest_score}")