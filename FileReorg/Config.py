import json

def GetConfig():
	return json.load(open('Config.json'))