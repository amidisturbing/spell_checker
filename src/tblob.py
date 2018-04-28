from textblob import TextBlob
import csv
import re
datasource = 'comments_toxic.short'
rowname = 'comment_text'
outf = 'tblob_temp'

rows_corrected = ''

with open('/Users/rafa/spell_checker/data/'+datasource, newline='') as csvfile :
     reader = csv.DictReader(csvfile)
     for row in reader:
          blob = TextBlob(row[rowname])
          row ['comment_text'] = str(blob.correct())
          rows_corrected += row['id'] + row['comment_text'] + row ['toxic']+'\n'
          #print (rows_corrected)

with open('/Users/rafa/spell_checker/data/results_spell_checker.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(['id','comment_text', 'toxic'])
    for key, value in rows_corrected.items():
       writer.writerow([key, value])           

#print(pbp)

