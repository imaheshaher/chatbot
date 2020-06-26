import datetime
import webbrowser
print("----ChatBot------\n	 ")
Chat={ 
		'hii':'hello\nWhat Can I do for you?',
		'how are you':'I am fine! , How are you',
		'fine':'so glad',
		'time':datetime.datetime.now().time(),
		'date':datetime.datetime.now().date(),
		'listen song':'song',
		'google search':'search',
		'you tube search':'you tube search'
}
def song():
	print("which song y want to listen")
	song=input()
	url='https://google.com/search?q='+song
	webbrowser.open(url)
	
def search():
	print('What u want to search?>>>')
	search=input()
	url="https://google.com/search?q="+str(search)
	webbrowser.open(url)
def searchg(search):
	print('What u want to search?>>>')
	#search=input()
	url="https://google.com/search?q="+str(search)
	webbrowser.open(url)
	
def utube():
	print('What u want to search?>>>')
	search=input()
	url="https://google.com/search?q="+"youtube "+str(search)
	webbrowser.open(url)
	
	


lst=Chat.keys()

def single(emptylst):
	for j in emptylst:
		print('You want to  ->>>',j)
		print(Chat[j])
		if j == "listen song":
			song()
		if j=="google search":
			search()
def multi(emptylst):		
	for j in emptylst:
		print('[{}]{}'.format(emptylst.index(j),j))
	op=int(input('option :: '))
	for j in emptylst:
		if op==emptylst.index(j):
			print('You want to  ->>>',j)
			print(Chat[j])
			if j == "listen song":
				song()
			if j=="google search":
				search()
			if j=="you tube search":
				utube()
def chat_action():
	while True:
		emptylst=[]
		say=input('Say some Here::')
		for i in lst:
			if say in i:
				emptylst.append(i)
	#	print(len(emptylst))
		if len(emptylst)>1:
			multi(emptylst)
		elif len(emptylst)==0:
			print("You want to search on this google Y/N")
			y=input()
			if y=='Y':
				searchg(say)
			else:
				print('plese hit enter button')
		else:
			single(emptylst)
				
chat_action()




'''
while(True):
  #print("Assistant :: Ask me question")
  say=input("You: ")
  try:
  	for i in lst:
  		if say in i:
  			chat=Chat[say]
  	
  			print('Assistant:: ',Chat[say])
  	
  	if chat=='song':
  		song()
  	if chat=='search':
  		serach()
	  	
  except:
  	print('Sorry!, I Can\'t be it Please ask me another question')
'''  
  


