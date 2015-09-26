from flask import Flask, render_template, json, request
import sqlite3
import uuid
import types
players=[]



class Game:
	gameRound=0
	players=1
	def __init__(self,gameID):
		self.gameID=gameID


def generateID():
	return uuid.uuid4()

gameID = generateID()
mygame = Game(gameID)
print mygame.gameID
app=Flask(__name__)


@app.route("/")
def main():
	return ""

@app.route("/addPlayer/<user>")
def addPlayer(user):
	players.append(user)
	return ""

@app.route("/game/join/<gID>")
def join(gID):
	if(str(gID)==str(mygame.gameID)):
		return render_template('index.html',gID=str(gID))
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
