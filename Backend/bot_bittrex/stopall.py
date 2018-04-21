#!/usr/bin/python

import os
import MySQLdb as mysql

def main():
	stopBots()

def stopBots():
	bots = getConfigBots()
	for bot in bots:
		os.kill(bot[1], 9)

def getConfigBots():
	try:
		db = mysql.connect(host="localhost", user="root", passwd="Gv9KP70E316v", db="protrader")
		cursor = db.cursor()
		query = ("SELECT id, pid FROM bot")
		cursor.execute(query)
		data = cursor.fetchall()
		cursor.close()
		return data
	except:
		print("Erro getConfigBots.")


main()