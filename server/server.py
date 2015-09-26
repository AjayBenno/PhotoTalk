from flask import Flask, render_template, json, request
import sqlite3

players=[]


class Game:
	def __init__(self):

	def start():

	def rotate():

	def 


app=Flask(__name__)
@app.route("/")
def main():
	return

@app.route("/addPlayer/<user>")
def addPlayer(user):
	players.append(user)
	return ""

@app.route("/getPlayers")
def getPlayers():
	x=""
	for player in players:
		x+=player+" "
	return x

@app.route("/startGame")
def startGame():
	game.start()
if __name__=="__main__":
	app.run(debug=True);