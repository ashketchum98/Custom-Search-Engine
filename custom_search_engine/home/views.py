from django.shortcuts import render
from apiclient.discovery import build
# Create your views here.

API_KEY = '' #Assign it your API KEY
SE_ID = '' # Assign it your search engine ID


def getResults(query):
	htmlTitles = [] # this will contain top 10 titles of pages
	htmlSnippets = [] # this will contain top 10 meta descriotions of pages
	links = [] # will contain top 10 links of pages.
	displayLinks = [] # will conatin text to display for links.
	resource = build("customsearch", "v1", developerKey=API_KEY).cse()
	result = resource.list(q=query, cx=SE_ID).execute()
	for i in range(len(result['items'])):
		links.append(result['items'][i]['link'])
		htmlTitles.append(result['items'][i]['htmlTitle'])
		htmlSnippets.append(result['items'][i]['htmlSnippet'])
		displayLinks.append(result['items'][i]['displayLink'])
	return zip(htmlTitles, links, displayLinks, htmlSnippets)

def index(request):
	if request.method == "POST":
		query = request.POST['query']
		context = getResults(query)
		return render(request, 'index.html', {"context": context, "query_str": query})
	return render(request,'index.html', {})