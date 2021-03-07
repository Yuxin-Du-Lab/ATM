################
# 目前版本无法测前导0
# 目前有两个mode，高概率0模式与无0模式
###########

import sys

sys.path.append('/home/yuxin/.local/lib/python2.7/site-packages')
import os
import exrex
import subprocess
from sympy import *

PATH = 'java -jar cjy2.jar'
AK = 1
x = Symbol("x")


# print(term)
# print(expression)

def Communicate(stdinLine):
    # communicate to .jar file
    p = subprocess.Popen(
        PATH,
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE
    )
    outline = p.communicate(bytes(stdinLine, encoding="utf8"))  # puple

    # output as string form: buffer
    buffer = bytes.decode(outline[0])  # str

    # his real answer:
    answer = buffer.split('\n', 1)[0]  # str

    return answer


def AutoDataTest(expression, Range, checkDetail):
    for turn in range(Range):
        # create test input line: stdinLine
        # stdinLine = exrex.getone(term)
        stdinLine = exrex.getone(expression)
        # print(stdinLine)

        # print input:
        if checkDetail == 1:
            print('stdin:\n' + stdinLine)

        # communicate to .jar file
        answer = Communicate(stdinLine)

        # get standard answer
        stdAnswer = diff(eval(stdinLine), x)  # mul
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
            print(stdAnswer)
            AK = 0
            break

        # next turn
        turn += 1
        print()


def AutoData():
    # set standard form:
    # with front 0
    # term0 = r'(([+-])?((([+-])?[0-9]{1,})|(x(\*{2}([+-])?[0-9]{1,})?))(\*((([+-])?[0-9]{1,})|(x(\*{2}([+-])?[0-9]{1,})?))){0,})'

    # lot of 0
    termLotOfZero = r'([+-])?((([+-])?(0|([1-9][0-9]{0,})))|(x(\*{2}([+-])?(0|([1-9][0-9]{0,})))?))(\*((([+-])?(0|([1-9][0-9]{0,})))|(x(\*{2}([+-])?(0|([1-9][0-9]{0,})))?))){0,}'
    # no 0
    termNoZero = r'([+-])?((([+-])?(([1-9][0-9]{0,})))|(x(\*{2}([+-])?(([1-9][0-9]{0,})))?))(\*((([+-])?(([1-9][0-9]{0,})))|(x(\*{2}([+-])?(([1-9][0-9]{0,})))?))){0,}'

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
    # expression0 = r'([+-])?' + term0 + r'(([+-])' + term0 + r'){0,}'
    expression = r'([+-])?' + term + r'(([+-])' + term + r'){0,}'

    ########################
    print(">>>if YOU want to check details, please input '1', else input '0'")
    checkDetail = sys.stdin.readline()
    if int(checkDetail) == 1:
        print(">>>you choose checking details")

    AutoDataTest(expression, int(Range), int(checkDetail))

    if AK == 1:
        print(">>>POINTS are ALL KILLED!!!!!")


def HandData():
    HandDataIn = open("HandDataIn.txt", "r")
    HandDataAns = open("HandDataAns.txt", "r")
    turn = 0
    while True:
        turn += 1
        stdinLine = HandDataIn.readline().split("\n", 1)[0]
        if stdinLine == '':
            break;
        answer = Communicate(stdinLine)
        stdAnsLine = HandDataAns.readline().split("\n", 1)[0]

        # get standard answer
        stdAnswer = eval(stdAnsLine)
        if answer == "":
            print("point" + str(turn) + "-----NO output")
            print("stdin:")
            print(stdinLine)
            print("HIM answer:")
            print(answer)
            print("STD answer:")
            print(stdAnswer)
#           AK = 0
            break

        if stdAnsLine == '':
            print("Where is my f**k answer?")
            print("stdin:")
            print(stdinLine)
            print("HIM answer:")
            print(answer)
            print("STD answer:")
            print(stdAnswer)
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
#           AK = 0
            break

print("IF you want auto data, input '1'")
mode = sys.stdin.readline()
if int(mode) == 1:
    AutoData()
else:
    HandData()
    print("not finished built")
