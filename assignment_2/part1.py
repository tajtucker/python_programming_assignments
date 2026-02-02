# Part-1 (20 Points): Write a program that asks the user to enter information about a group of students using a while loop. The information includes name (data type String) and score (data type float). The program displays the name with the highest score. The number of students is given by the user.

# The program creates two empty lists (one for names and one for scores) and fills them in the while loop. Then, you can use index method of the list and max function to find the index of the maximum score.

names_list = []
scores_list = []

numof_students = int(input("Enter number of students: "))


while numof_students != 0:
    name = input("Enter name: ")
    names_list.append(name)

    score = float(input("Enter score: "))
    scores_list.append(score)

    numof_students -= 1

highest_score = max(scores_list)
index = scores_list.index(highest_score)
highest_name = names_list[index]

print(f"{highest_name} has the highest score {highest_score}")