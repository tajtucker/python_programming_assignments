# Write a Python program that defines a function named comp3140_scores which takes a list of student scores as input and returns the average, highest, and lowest scores. The program should prompt the user to enter a series of scores separated by spaces, convert these inputs to a list of numbers (refer to your lecture notes on data structures for refreshing yourself about lists), and then pass this list to the comp3140_scores function. The function should calculate and return the average, highest, and lowest scores, which should then be displayed. 

prompt = input("Enter scores separated by spaces: ")
scores = [float(s) for s in prompt.split()]

def comp3140_scores(scores):
    total = 0
    for score in scores:
        total += score
    
    average = total / len(scores)
    highest = max(scores)
    lowest = min(scores)

    return average, highest, lowest

avg, high, low = comp3140_scores(scores)
print(f"Average: {avg}")
print(f"Highest: {high}")
print(f"Lowest: {low}")