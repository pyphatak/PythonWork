from html.parser import HTMLParser
import urllib.request as urllib2

class MyHTMLParser(HTMLParser):

   #Initializing lists
   lsStartTags = list()
   lsEndTags = list()
   lsStartEndTags = list()
   lsComments = list()
   lsdata = list()
   lookingForAttr = ['practice-item', 'industry-item', 'region-item']
   foundLookingForAttr = False 
   whitecaseDictionary = {}
   processAttr = ''

   #HTML Parser Methods
   def handle_starttag(self, startTag, attrs):
      #print(lookingForAttr)
      if startTag == 'div' and len(attrs) == 1 and attrs[0][0] == 'class' and attrs[0][1] in self.lookingForAttr:
        self.processAttr = attrs[0][1]
        self.foundLookingForAttr = True
        self.whitecaseDictionary[self.processAttr] = list('')

   def handle_endtag(self, endTag):
      if endTag == 'div':
        if self.foundLookingForAttr:
          self.foundLookingForAttr = False

   def handle_startendtag(self,startendTag, attrs):
       self.lsStartEndTags.append(startendTag)

   def handle_comment(self,data):
       self.lsComments.append(data)

   def handle_data(self,data):
      if self.foundLookingForAttr:
        #self.lsdata.append(data)
        #self.lsdata.append(data.encode('UTF-8'))
        #self.lsdata.append(data)
        if len(data.strip()) != 0:
          self.whitecaseDictionary[self.processAttr].append(data)


        #print.lsdata
      #print(data.encode('ascii'))
      #print("\n")

#creating an object of the overridden class
parser = MyHTMLParser()

#Opening NYTimes site using urllib2
#html_page = urllib2.urlopen("https://www.whitecase.com/law#industries")
with open('/Users/ajantaphatak/Downloads/Legal Services _ International Law _ White & Case.htm', encoding="UTF-8") as html_file_object:
  htmlContent=html_file_object.read()

#Feeding the content
parser.feed(htmlContent)
#parser.feed(str(html_page.read()))

#Print Key and their associated values

for k in parser.whitecaseDictionary.keys():
  print(k)
  for v in parser.whitecaseDictionary[k]:
    print(v)
  print('\n')
#print(parser.whitecaseDictionary)

 

