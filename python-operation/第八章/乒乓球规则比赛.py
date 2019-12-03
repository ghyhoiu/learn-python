from random import random
def getInputs():
# 乒乓球规则是一局比赛中先得 11 分为胜，10 平时，先得 2 分为胜
# 一场比赛采用三局两胜，当每人各赢一局时，最后一局为决胜局
    probA = float(input("请输入选手 A 的能力值(0-1)："))
    probB = float(input("请输入选手 B 的能力值(0-1)："))
    return probA, probB
def simOneGame(probA, probB):
    scoreA, scoreB = 0,0
    serving = 'A'
    i = 1;
    while not gameOver(scoreA, scoreB):
        serving = switchServing(i, serving)
        i += 1
        if serving is 'A':
            if random() < probA:
                scoreA += 1
            else:
                scoreB += 1
        else:   
            if random() < probB:
                scoreB += 1
            else:
                scoreA += 1
    print(scoreA,'--',scoreB)
    return Winner(scoreA, scoreB)
def gameOver(scoreA, scoreB):
    if scoreA == 10 & scoreB == 10:
        return False
    elif scoreA == 12 or scoreB == 12:
        return True
    else:
        return scoreA == 11 or scoreB == 11
def switchServing(i, serving):
    if i%5 == 0 and i > 0:
        if serving is 'A':
            serving = 'B'
        else:
            serving = 'A'
    return serving
def Winner(scoreA, scoreB):
    if scoreA == 12 or scoreB == 12:
        if scoreA == 12:
            return 'A'
        else:
            return 'B'
    else:
        if scoreA == 11:
            return 'A'
        else:
            return 'B'
def simOneChampion():
    B = 0;
    A = 0;
    round = 1
    probA, probB = getInputs();
    while True:
        print('第{}局'.format(round))
        r = simOneGame(probA, probB)
        round += 1
        if r is 'A':
            A += 1
        else:
            B += 1
        if A == 2:
            print('A 获胜')
            break
        elif B == 2:
            print('B 获胜')
            break
        else:
            continue
simOneChampion()