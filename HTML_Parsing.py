from html.parser import HTMLParser
import urllib.request as urllib2

class MyHTMLParser(HTMLParser):

   #Initializing lists
   lsStartTags = list()
   lsEndTags = list()
   lsStartEndTags = list()
   lsComments = list()
   lsdata = list()
   foundPracticeList = False 

   #HTML Parser Methods
   def handle_starttag(self, startTag, attrs):
      if startTag == 'div':
          if len(attrs) == 1: 
            if attrs[0][0] == 'class':
              if attrs[0][1] == "practice-item":
                #print(len(attrs), attrs[0][0], attrs[0][1])
                #print("Found Practice List")
                self.foundPracticeList = True
       #self.lsStartTags.append(startTag)

   def handle_endtag(self, endTag):
      if endTag == 'div':
        if self.foundPracticeList:
          self.foundPracticeList = False
          self.lsEndTags.append(endTag)
          #print(self.lsdata)

   def handle_startendtag(self,startendTag, attrs):
       self.lsStartEndTags.append(startendTag)

   def handle_comment(self,data):
       self.lsComments.append(data)

   def handle_data(self,data):
      if self.foundPracticeList:
        #self.lsdata.append(data)
        #self.lsdata.append(data.encode('UTF-8'))
        self.lsdata.append(data)


        #print.lsdata
      #print(data.encode('ascii'))
      #print("\n")

#creating an object of the overridden class
parser = MyHTMLParser()
practiceList = list()

#Opening NYTimes site using urllib2
#html_page = urllib2.urlopen("https://www.nytimes.com/")
with open('/Users/ajantaphatak/Downloads/Legal Services _ International Law _ White & Case.htm', encoding="UTF-8") as html_file_object:
  htmlContent=html_file_object.read()

#Feeding the content
parser.feed(htmlContent)
print("Number of elements in list", len(parser.lsdata))
for practice in parser.lsdata:
  if len(practice.strip()) != 0:
    practiceList.append(practice)
for practice in practiceList:
  print(practice)

 

