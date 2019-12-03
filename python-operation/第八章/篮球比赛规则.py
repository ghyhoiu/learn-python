from random import random
countdown = 0;
def getInputs():
    while True:
        try:
            foulAscore,probA,probA3 = input('请输入 A 队的参数，用逗号隔开').split(',')
            foulBscore,probB,probB3 = input("请输入 B 队的参数，用逗号隔开").split(',')
            foulAscore = float(foulAscore)
            foulBscore = float(foulBscore)
            probA = float(probA)
            probB = float(probB)
            probA3 = float(probA3)
            probB3 = float(probB3)
            break
        except:
            print('您的输入有误，请重新输入')
            continue
    return                                  (foulAscore,probA,probA3), 
    (foulBscore,probB,probB3)
def foul(scoreA, scoreB, foulAscore, foulBscore):
    side = random()
    if side > 0.5:
        if scoreA > random():
            scoreA += 1
        else:
            scoreB += 1
    else:
        if scoreB > random():
            scoreB += 1
        else:
            scoreA += 1
    return scoreA, scoreB
def simOneGame(argA, argB, ser):
    global countdown
    scoreA, scoreB = 0,0
    fawl = 0.3
    serving = ser
    i = 1;
    countdown = 50
    foulAscore = argA[0]
    probA = argA[1]
    probA3 = argA[2]
    foulBscore = argB[0]
    probB = argB[1]
    probB3 = argB[2]
    while not gameOver(scoreA, scoreB):
        judge = random()
        if judge < fawl:
            scoreA, scoreB = foul(scoreA, scoreB, foulAscore,foulBscore)
        else:
            if serving is 'A':
                if random() < probA:
                    scoreA += 3 if probA3 > random() else 2
                else:
                    scoreB += 3 if probB3 > random() else 2
            else:
                if random() < probB:
                    scoreB += 3 if probB3 > random() else 2
                else:
                    scoreA += 3 if probA3 > random() else 2
    print(scoreA,'--',scoreB)
    return Winner(scoreA, scoreB)
def gameOver(scoreA, scoreB):
    global countdown;
    if countdown == 0:
        if scoreA == scoreB:
            countdown += 5
            return False
        else:
            return True
    else:
        countdown -= 1
        return False
def switchServing(serving):
    if serving is 'A':
        serving = 'B'
    else:
        serving = 'A'
    return serving
def Winner(scoreA, scoreB):
    return 'A' if scoreA > scoreB else 'B'
def simOneChampion():
    B = 0;
    A = 0;
    round = 1
    argA, argB = getInputs();
    serving = 'A'
    while True:
        print('第{}节'.format(round))
        r = simOneGame(argA, argB,serving)
        serving = switchServing(serving)
        round += 1
        if r is 'A':
            A += 1
        else:
            B += 1
        if A == 3:
            print('A 队胜出')
            break
        elif B == 3:
            print('B 队胜出')
            break
        else:
            continue
simOneChampion()
