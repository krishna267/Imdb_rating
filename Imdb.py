from tkinter import Tk
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
Tk().withdraw()
foldername = askdirectory()

exten = ".mkv"

#finding files with particular extension
results = []
results += [each for each in os.listdir(foldername) if each.endswith(exten)]
print(results)

#google custom search
service = build('customsearch','v1',developerKey = API_KEY)
os.chdir(foldername)
for mov in results:
	nam = mov.replace(exten,"")
	if nam.endswith("-imdb)"):
		print(mov)
		search_term = PTN.parse(mov)
		os.rename(mov,search_term['title']+ "(" + getRating(search_term['title']) +"-imdb)"+exten)