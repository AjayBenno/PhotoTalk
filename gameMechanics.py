import random
import math


def rotate(listOfPlayers):
	result = [listOfPlayers[-1]] + listOfPlayers[:-1] 
	return result


#returns a randomly generated noun
def generateRandomWord():
	listNouns = []
	infile = open('nouns.txt', 'r')
	for line in infile:
		temp = line.strip()
		temp = temp[:-1]
		listNouns.append(temp)
	randIndex = math.floor(random.random() * len(listNouns))
	while len(listNouns[randIndex]) == 0 or listNouns[randIndex][0] == "\\" or listNouns[randIndex][0] == "{":
		randIndex = math.floor(random.random() * len(listNouns))
	return listNouns[randIndex]


def nextStep(flaskInput):
	gameRoom = flaskInput[0]
	playerBoard = flaskInput[1]
	inputtedAnswers = flaskInput[2]
	turn = flaskInput[3]
	inputAnswers = flaskInput[4]

	if turn == 0:
		return [gameRoom,playerBoard, inputtedAnswers, turn, inputAnswers]
	playerBoard = rotate(playerBoard)
	for index in range(4):
		print(inputAnswers[index])
		inputtedAnswers[index] += [inputAnswers[index]]
	return [gameRoom,playerBoard, inputtedAnswers, turn, inputAnswers]


gameRoom = ['cow', 'monkey', 'zebra', 'snake']
playerBoard = [0,1,2,3]
inputtedAnswers = [['cow'], ['monkey'], ['zebra'], ['snake']]
turn = 1
inputAnswers = ['bovine','monkey','horse', 'cobra']

ultraLongList = [gameRoom, playerBoard, inputtedAnswers, turn, inputAnswers]
# print(ultraLongList)



	




