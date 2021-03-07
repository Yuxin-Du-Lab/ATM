################
# 目前版本无法测前导0
# 目前有两个mode，高概率0模式与无0模式
# cjy记得删sys.path.append和改.jar路径！！
# 下一版本加log
###########

import sys
sys.path.append('/home/yuxin/.local/lib/python2.7/site-packages')

import os
import exrex
import subprocess
from sympy import *

global AK
AK = 1

x = Symbol("x")
# lot of 0
termLotOfZero = r'([+-])?((([+-])?(0|([1-9][0-9]{0,})))|(x(\*{2}([+-])?(0|([1-9][0-9]{0,})))?))(\*((([+-])?(0|([1-9][0-9]{0,})))|(x(\*{2}([+-])?(0|([1-9][0-9]{0,})))?))){0,}'
# no 0
termNoZero = r'([+-])?((([+-])?(([1-9][0-9]{0,})))|(x(\*{2}([+-])?(([1-9][0-9]{0,})))?))(\*((([+-])?(([1-9][0-9]{0,})))|(x(\*{2}([+-])?(([1-9][0-9]{0,})))?))){0,}'

# take care here:
BasicOrder = 'java -jar '
fileName1 = 'home1_1.jar'
fileName2 = 'lhy2.jar'
PATH = BasicOrder + fileName1
PATH1 = BasicOrder + fileName1
PATH2 = BasicOrder + fileName2


def BuildExpression(term):
    return r'([+-])?' + term + r'(([+-])' + term + r'){0,}'


def Communicate(stdinLine, path):
    # communicate to .jar file
    p = subprocess.run(
        path,
        input=stdinLine,
        stdout=subprocess.PIPE,
        text=True,
        shell=True
    )
    buffer = p.stdout
    answer = buffer.split("\n", 1)[0]
    '''
    p = subprocess.Popen(
        path,
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE
    )
    outline = p.communicate(bytes(stdinLine, encoding="utf8"))  # puple

    # output as string form: buffer
    buffer = bytes.decode(outline[0])  # str

    # his real answer:
    answer = buffer.split('\n', 1)[0]  # str
    '''

    return answer


def AutoExpression(expression):
    stdinLine = exrex.getone(expression)  # str
    return stdinLine


def FileReadLine(point):
    return point.readline().split("\n", 1)[0]  # str


def AutoDataTest(expression, Range, checkDetail):
    global AK
    for turn in range(Range):
        # create test input line: stdinLine
        stdinLine = AutoExpression(expression)

        # print input:
        if checkDetail == 1:
            print('stdin:\n' + stdinLine)

        # communicate to .jar file
        answer = Communicate(stdinLine, PATH)

        # get standard answer
        stdAnswer = diff(eval(stdinLine), x)  # ADD

        if checkDetail == 1:
            print("stdAnswer:\n" + str(stdAnswer))

        if answer == "":
            print("point" + str(turn) + "-----NO output")
            print("stdin:")
            print(stdinLine)
            print("HIM answer:")
            print(answer)
            print("STD answer:")
            print(stdAnswer)
            AK = 0
            break

        answer = eval(answer)
        if checkDetail == 1:
            print("answer:\n" + str(answer))

        # check ifEqual
        if simplify(stdAnswer - answer) == 0:
            print("point" + str(turn) + "-----AC")
        else:
            print("point" + str(turn) + "-----WA")
            print("stdin:")
            print(stdinLine)
            print("HIM answer:")
            print(answer)
            print("STD answer:")
            print(sdAnswer)
            AK = 0
            break

        # next turn
        turn += 1
        print()


def AutoData():
    global AK
    # set standard form:
    # with front 0
    # term0 = r'(([+-])?((([+-])?[0-9]{1,})|(x(\*{2}([+-])?[0-9]{1,})?))(\*((([+-])?[0-9]{1,})|(x(\*{2}([+-])?[0-9]{1,})?))){0,})'

    ########################
    print(">>>INPUT int to set the test point number")
    Range = sys.stdin.readline()
    print(">>>Range is set as:" + str(Range))

    ########################
    print(">>>INPUT '1', turn to Lots of Zero mode")
    print(">>>INPUT '2', turn to None Zero mode")
    mode = sys.stdin.readline()
    if int(mode) == 1:
        print(">>>Thanks for choose Lots of Zero mode")
        term = termLotOfZero
    else:
        print(">>>Thanks for choose None Zero mode")
        term = termNoZero
    expression = BuildExpression(term)

    ########################
    print(">>>if YOU want to check details, please input '1', else input '0'")
    checkDetail = sys.stdin.readline()
    if int(checkDetail) == 1:
        print(">>>you choose checking details")

    AutoDataTest(expression, int(Range), int(checkDetail))


def HandData():
    global AK
    print(">>>if you need details, input '1'")
    checkDetail = sys.stdin.readline()

    HandDataIn = open("HandDataIn.txt", "r")
    HandDataAns = open("HandDataAns.txt", "r")
    turn = 0
    while True:
        turn += 1
        stdinLine = FileReadLine(HandDataIn)
        if stdinLine == '':
            break
        answer = Communicate(stdinLine, PATH)
        stdAnsLine = FileReadLine(HandDataAns)

        if int(checkDetail) == 1:
            print("STD answer:")
            print(stdAnsLine)
            print("HIM answer:")
            print(answer)

        stdAnswer = eval(stdAnsLine)
        if answer == "":
            print("point" + str(turn) + "-----NO output")
            print("stdin:")
            print(stdinLine)
            print("HIM answer:")
            print(answer)
            print("STD answer:")
            print(stdAnswer)
            AK = 0
            break

        if stdAnsLine == '':
            print("Where is my f**k answer?")
            print("stdin:")
            print(stdinLine)
            print("HIM answer:")
            print(answer)
            print("STD answer:")
            print(stdAnswer)
            AK = 0
            break

        answer = eval(answer)
        if simplify(stdAnswer - answer) == 0:
            print("point" + str(turn) + "-----AC")
        else:
            print("point" + str(turn) + "-----WA")
            print("stdin:")
            print(stdinLine)
            print("HIM answer:")
            print(answer)
            print("STD answer:")
            print(stdAnswer)
            AK = 0
            break


def CompareCheck():
    global AK
    # compare hand data output:
    print(">>>if you need details, input '1'")
    checkDetail = sys.stdin.readline()

    print(">>>Now Check Hand data")
    HandDataIn = open("HandDataIn.txt", "r")
    turn = 0
    while True:
        turn += 1
        stdinLine = FileReadLine(HandDataIn)
        if stdinLine == '':
            break;
        answer1 = Communicate(stdinLine, PATH1)
        answer2 = Communicate(stdinLine, PATH2)

        if int(checkDetail) == 1:
            print("HIM1 answer:")
            print(answer1)
            print("HIM2 answer:")
            print(answer2)

        answer1 = eval(answer1)
        answer2 = eval(answer2)
        if simplify(answer1 - answer2) == 0:
            print("point" + str(turn) + "-----ALL SAME")
        else:
            print("point" + str(turn) + "-----DIFFERENT OUTPUT")
            print("stdin:")
            print(stdinLine)
            print("HIM1 answer:")
            print(answer1)
            print("HIM2 answer:")
            print(answer2)
            print("STD answer:")
            print(snswer)
            AK = 0
            break


################

print(">>>INPUT '1', turn to Auto Data")
print(">>>INPUT '2', turn to Hand Data")
print(">>>INPUT '3', turn to Compare Run")
mode = sys.stdin.readline()
if int(mode) == 1:
    AutoData()
elif int(mode) == 2:
    HandData()
elif int(mode) == 3:
    CompareCheck()
else:
    print("What's the f**k mode!")

if AK == 1:
    print(">>>All points are Killed!")
