from textblob import TextBlob
import csv
import re
datasource = 'comments_toxic.train'
rowname = 'comment_text'
with open('/Users/rafa/spell_checker/data/'+datasource, newline='') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
     	print(row[rowname])
     	blob = TextBlob(row[rowname])
     	corrected = blob.correct()
     	print(corrected)
     	#match user id  of offensive language data set
     	
	
	#line = "@X_XPDOTJDOT: Damn near gotta protect my tweets.. stalkers being annoying you got that dope dick. Drive these bitches loco"
	#print(re.sub(r'(\@(.*)\:)','', line))
