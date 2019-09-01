result = 0
scores = [80, 100, 70, 90, 40]

class_scores = [
    [30, 90, 80, 40, 50],
    [100, 100, 100, 100, 100],
    [90, 90, 30, 30, 20]
]

for i in class_scores:
    print(sum(i), sum(i)/len(i))

scoress(class_scores)

def scoress(list):
    for i in list:
        print(sum(i), sum(i)/len(i))
    return


def SumScore(list):
    sum = 0
    for i in range(0, len(list)):
        for j in range(0, len(list[i])):
            sum += list[i][j]

    return sum
print(SumScore(class_scores))






# for i in range(0, len(scores)):
#     result += scores[i]
# print(result)

# for score in scores:
#     result += score
# print(result)

