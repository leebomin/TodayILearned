## Fill this file second

def class_total(scores, subject):
    total = 0
    for score in scores:
        total += score[subject]
    return total
