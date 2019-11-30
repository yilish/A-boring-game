import time
import random
import os
def gameStart():
    os.system("cls")
    print('It\'s a boring test intending to measure your reaction time')
    print('are you ready?')
    print('\n(continue with entering any press)')
    input()
    os.system("cls")
    sleepTime=random.randint(2,5)
    time.sleep(sleepTime)
    print('It\'s time to test your handSpeed!')
    #sys.stdin.flush()
    startTime=time.time()
    input()
    endTime=time.time()
    thisTurn=endTime-startTime
    if thisTurn<0.05:
        print('You have cheated, no record!')
        input()
        gameStart()
    global bestScore
    bestScore=min(thisTurn,bestScore)
    print('Your reaction time is',thisTurn,'s')
    for i in range (10):
        print(' ')
    
    print('Your best score is',bestScore,'s')
    input()
    gameStart()
bestScore=999
gameStart()
