from bs4 import BeautifulSoup as bs
from os import listdir

textFiles = [ f for f in listdir('./') if f.endswith(".txt") ]
text = ''
for i,file in enumerate(textFiles):
    html = open('./'+file,"r",encoding='utf-16')
    soup = bs(html,"html.parser")
    textArray = [t for t in soup.find_all(text=True) if t.parent.name=='p']
    text += '\n'.join(textArray)

textFile = open("text.txt","w")
textFile.write(text)
textFile.close()
