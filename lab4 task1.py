# TODO решите задачу
def task() -> float:
    summa = 0
    ch1 = 0
    ch2 = 0
    f = open("input.json", "r")
    x = f.readlines()
    for i in range(len(x)):
        if x[i].find("score") != -1:
            ch1 = float(x[i][((x[i].find("score")) + 8):len(x[i]) - 2])
        elif (x[i].find("weight")) != -1:
            ch2 = float(x[i][((x[i].find("weight")) + 9):len(x[i]) - 1])
        if (ch1 != 0) and (ch2 != 0):
            summa += ch1 * ch2
            ch1, ch2 = 0, 0
    f.close()
    return round(summa, 3)


print(task())
