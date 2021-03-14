################
# 目前版本无法测前导0
# 目前有两个mode，高概率0模式与无0模式
# cjy记得删sys.path.append和改.jar路径！！
# ###########

import sys
sys.path.append('/home/yuxin/.local/lib/python2.7/site-packages')

import os
import exrex
import subprocess
from sympy import *

import Head

# print(Head.Term)

global AK
AK = 1

x = Symbol("x")
# lot of 0
termLotOfZero = r'([+-])?((([+-])?(0|([1-9][0-9]{0,})))|(x(\*{2}([+-])?(0|([1-9][0-9]{0,})))?))(\*((([+-])?(0|([1-9][0-9]{0,})))|(x(\*{2}([+-])?(0|([1-9][0-9]{0,})))?))){0,}'
# no 0
termNoZero = r'([+-])?((([+-])?(([1-9][0-9]{0,})))|(x(\*{2}([+-])?(([1-9][0-9]{0,})))?))(\*((([+-])?(([1-9][0-9]{0,})))|(x(\*{2}([+-])?(([1-9][0-9]{0,})))?))){0,}'

# SET PATH here:
BasicOrder = 'java -jar '
fileName1 = 'Saber.jar'
fileName2 = 'Lancer.jar'
fileName3 = 'Archer.jar'
fileName4 = 'Caster.jar'
fileName5 = 'Assassin.jar'
fileName6 = 'Berserker.jar'
fileName7 = 'Alterego.jar'
fileName8 = 'OOhomework1.2.jar'
fileName9 = 'cjy.jar'
logName = "output.log"

PATH = BasicOrder + fileName8
PATH1 = BasicOrder + fileName8
PATH2 = BasicOrder + fileName9

# FILE I/O
FILE = open(logName, 'w')

# Different

def PrintDifferent(turn, stdinLine, answer1, answer2):
    print("point" + str(turn) + "-----DIFFERENT OUTPUT")
    print("stdin:")
    print(stdinLine)
    print("HIM1 answer:")
    print(answer1)
    print("HIM2 answer:")
    print(answer2)

# All Same
def PrintAllSame(turn):
    PrintString("point" + str(turn) + "-----ALL SAME")

# No Answer
def PrintNoAnswer(stdinLine, answer, stdAnswer):
    PrintString("Where is my answer?")
    PrintString("stdin:")
    PrintString(stdinLine)
    PrintString("HIM answer:")
    PrintString(answer)
    PrintString("STD answer:")
    PrintString(stdAnswer)

# Wrong Answer
def PrintWrongAnswer(turn, stdinLine, answer, stdAnswer):
    PrintString("point" + str(turn) + "-----WA")
    PrintString("stdin:")
    PrintString(str(stdinLine))
    PrintString("HIM answer:")
    PrintString(str(answer))
    PrintString("STD answer:")
    PrintString(str(stdAnswer))

# Accept
def PrintAccept(turn):
    PrintString("point" + str(turn) + "-----AC")

# No Output
def PrintNoOutput(turn, stdinLine, answer, stdAnswer):
    PrintString("point" + str(turn) + "-----NO output")
    PrintString("stdin:")
    PrintString(str(stdinLine))
    PrintString("HIM answer:")
    PrintString(str(answer))
    PrintString("STD answer:")
    PrintString(str(stdAnswer))

# PrintStr to both console and log
def PrintString(str):
    print(str)
    FILE.write(str + '\n')

def BuildExpression(term, mode):
    if mode!=3:
        return r'([+-])?' + term + r'(([+-])' + term + r'){0,}'
    else:
        return Head.EXPRESSION1

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
    print(stdinLine)
    return stdinLine


def FileReadLine(point):
    return point.readline().split("\n", 1)[0]  # str


def AutoDataTest(expression, Range, checkDetail):
    global AK
    for turn in range(Range):
        # print \n
        PrintString('\n')

        # create test input line: stdinLine
        stdinLine = AutoExpression(expression)

        # communicate to .jar file
        answer = Communicate(stdinLine, PATH)

        # get standard answer
        stdAnswer = diff(eval(stdinLine), x)  # ADD

        # print input & answer
        if checkDetail == 1:
            PrintString('stdin:\n' + stdinLine)
            PrintString("stdAnswer:\n" + str(stdAnswer))

        if answer == "":
            PrintNoOutput(turn, stdinLine, answer, stdAnswer)
            AK = 0
            break

        answer = eval(answer)
        if checkDetail == 1:
            PrintString("answer:\n" + str(answer))

        # check ifEqual
        if simplify(stdAnswer - answer) == 0:
            PrintAccept(turn)
        else:
            PrintWrongAnswer(turn, stdinLine, answer, stdAnswer)
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
    PrintString(">>>Range is set as:" + str(Range))

    ########################
    print(">>>INPUT '1', turn to Lots of Zero mode")
    print(">>>INPUT '2', turn to None Zero mode")
    print(">>>INPUT '3', turn to homework2")
    mode = sys.stdin.readline()
    if int(mode) == 1:
        PrintString(">>>Thanks for choose Lots of Zero mode")
        term = termLotOfZero
    elif int(mode) == 2:
        PrintString(">>>Thanks for choose None Zero mode")
        term = termNoZero
    else:
        PrintString(">>>Thanks for choose homework2")
        term = Head.TERM
    expression = BuildExpression(term, int(mode))

    ########################
    print(">>>if YOU want to check details, please input '1', else input '0'")
    checkDetail = sys.stdin.readline()
    if int(checkDetail) == 1:
        PrintString(">>>you choose checking details")

    AutoDataTest(expression, int(Range), int(checkDetail))


def HandData():
    global AK
    PrintString(">>>Now Check Hand data")

    print(">>>if you need details, input '1'")
    checkDetail = eval(sys.stdin.readline())

    HandDataIn = open("HandDataIn.txt", "r")
    HandDataAns = open("HandDataAns.txt", "r")
    turn = 0
    while True:
        PrintString('\n')

        turn += 1
        stdinLine = FileReadLine(HandDataIn)
        if stdinLine == '':
            break
        answer = Communicate(stdinLine, PATH)
        stdAnsLine = FileReadLine(HandDataAns)

        # print input & answer
        if checkDetail == 1:
            PrintString('stdin:\n' + stdinLine)
            PrintString("stdAnswer:\n" + str(stdAnsLine))
        '''
        if int(checkDetail) == 1:
            print("STD answer:")
            print(stdAnsLine)
            print("HIM answer:")
            print(answer)
        '''

        stdAnswer = eval(stdAnsLine)
        if answer == "":
            PrintNoOutput(turn, stdinLine, answer, stdAnswer)
            AK = 0
            break

        if stdAnsLine == '':
            PrintNoAnswer(stdinLine, answer, stdAnswer)
            AK = 0
            break

        answer = eval(answer)
        if simplify(stdAnswer - answer) == 0:
            PrintAccept(turn)
        else:
            PrintWrongAnswer(turn, stdinLine, answer, stdAnswer)
            AK = 0
            break


def CompareCheck():
    global AK
    # compare hand data output:
    print(">>>if you need details, input '1'")
    checkDetail = sys.stdin.readline()

    PrintString(">>>Now Check Hand data")
    CompareData = open("CompareData.txt", "r")
    turn = 0
    while True:
        PrintString('\n')
        turn += 1
        stdinLine = FileReadLine(CompareData)
        if stdinLine == '':
            break
        answer1 = Communicate(stdinLine, PATH1)
        answer2 = Communicate(stdinLine, PATH2)

        if int(checkDetail) == 1:
            PrintString("HIM1 answer:")
            PrintString(answer1)
            PrintString("HIM2 answer:")
            PrintString(answer2)

        answer1 = eval(answer1)
        answer2 = eval(answer2)
        if simplify(answer1 - answer2) == 0:
            PrintAllSame(turn)
        else:
            PrintDifferent(turn, stdinLine, answer1, answer2)
            AK = 0
            break

# ---------------main---------------

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
    PrintString("What's the mode!")

if AK == 1:
    PrintString(">>>All points are Killed!")

# close FILE
FILE.close()