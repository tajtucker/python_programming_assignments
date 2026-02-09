# Part-4(a) (15 Points): Create a module named comp_3140_utilities.py that includes the following functions. Each function takes a list of scores.
# •	average_score(scores), returns the average score.
# •	highest_score(scores), returns the highest score.
# •	lowest_score(scores), returns the lowest score.
# •	score_range(scores), returns the range (difference between the highest and lowest scores).

def average_score(scores):
    total = 0
    for score in scores:
        total += score
    average = total / len(scores)
    return average

def highest_score(scores):
    highest = max(scores)
    return highest

def lowest_score(scores):
    lowest = min(scores)
    return lowest

def score_range(scores):
    highest = max(scores)
    lowest = min(scores)
    difference = highest - lowest
    return difference

