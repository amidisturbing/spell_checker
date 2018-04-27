from textblob import TextBlob
import csv
import re
datasource = 'labeled_data_ol_short.csv'
rowname = 'comment_text'
with open('/Users/rafa/spell_checker/data/'+datasource, newline='') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
     	print(row[rowname])
     	blob = TextBlob(row[rowname])
     	corrected = blob.correct()
     	print(corrected)
     	#match user id  of offensive language data set
     	matchObj = re.match( r'(\@(.*)\:)', corrected, re.M|re.I)
     	if matchObj:
     		print ("matchObj.group() : ", matchObj.group())
     		print ("matchObj.group(1) : ", matchObj.group(1))
     		print ("matchObj.group(2) : ", matchObj.group(2))
     	else:
     		print ("No match!!")
	
	#line = "@X_XPDOTJDOT: Damn near gotta protect my tweets.. stalkers being annoying you got that dope dick. Drive these bitches loco"
	#print(re.sub(r'(\@(.*)\:)','', line))
