from tkinter import *
from tkinter.filedialog import askdirectory
import os,re
from apiclient.discovery import build
import pprint
import PTN

#custom search API key
API_KEY = ''

def getRating(queryString):
	request = service.cse().list( q = queryString, cx = '',)
	response = request.execute()
	for item in response.get('items',[]):
		dictionaryResponse = item['pagemap']
		listed = dictionaryResponse['aggregaterating'][0]
		rating = listed['ratingvalue']
		return rating

#select folder GUI
def select():	
	Tk().withdraw()
	global foldername 
	foldername = askdirectory()

def todo():
	#finding files with particular extension
	exten = variable.get()
	results = []
	results += [each for each in os.listdir(foldername) if each.endswith(exten)]
	print(results)

	#google custom search
	global service 
	service = build('customsearch','v1',developerKey = API_KEY)
	os.chdir(foldername)
	for mov in results:
		nam = mov.replace(exten,"")
		if not nam.endswith("-imdb)"):
			print(mov)
			search_term = PTN.parse(mov)
			os.rename(mov,search_term['title']+ "(" + getRating(search_term['title']) +"-imdb)"+exten)
	return

root = Tk()
root.minsize(width = 200, height = 200)
root.maxsize(width = 200, height = 200)
futton = Button(root, text = "Select Folder",command = select)
futton.pack()

variable = StringVar(root)
variable.set(".mkv") #default value
w = OptionMenu(root, variable, ".mkv", ".mp4", ".avi")
w.pack()
button = Button(root,text = "Go",command = todo)
button.pack()

mainloop()
