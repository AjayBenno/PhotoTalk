from flask import Flask, render_template, json, request
from collections import deque
import uuid
import types
import json
import base64

gameBoard=[]
playerBoard=[0,1,2,3]
class Game:
	gameRound=1
	players=-1
	def __init__(self,gameID):
		self.gameID=gameID
def getHugeAssList():
	histList = [[gameBoard[0]],gameBoard[1],gameBoard[2],gameBoard[3]]
	tList= [gameBoard,playerBoard,histList,mygame.gameround,['','','','']]
	return tlist

def generateID():
	return uuid.uuid4()
def createGameBoard():
	return list[generateRandom(),generateRandom(),generateRandom(),generateRandom()]
gameBoard = createGameBoard();
gameID = generateID()
mygame = Game(gameID)
#print mygame.gameID
app=Flask(__name__, static_url_path='/static')


@app.route("/")
def main():
	return render_template('index.html',gID=str(mygame.gameID))
# @app.route("")
# def addPlayer(userID,base64):
# 	d_game[userID] = base64
# 	return str(base64)
@app.route('/game/getNumPlayers', methods=['POST'])
def getNumPlayers():
	return Game.players

@app.route('/game/userID', methods = ['POST'])
def userID():
	jsonString = request.form['wordlist']
	jsonOBJ= json.loads(jsonString)
	tempID= jsonOBJ['id']
	associatedPhoto=jsonOBJ['b64']
	d_game[tempID]=associatedPhoto

	if()
	return ""

@app.route("/game/disp")
def disp():
	return str(d_game)

@app.route("/game/join/<gID>")
def join(gID):

	if(str(gID)==str(mygame.gameID)):
		Game.players +=1
		return render_template('round1.html',gID=str(gID),players=Game.players,gameBoard=gameBoard)
	else:
		return "bad"

@app.route("/game/id")
def id():
	return str(mygame.gameID)


@app.route("/getPlayers")
def getPlayers():
	x=""
	for player in players:
		x+=player+" "
	return x


if __name__=="__main__":
	app.run(debug=True);
