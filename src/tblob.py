from textblob import TextBlob
import csv
import re
datasource = 'comments_toxic.short'
rowname = 'comment_text'
outf = 'tblob_temp'

rows_corrected = ''
r = ''
print('Opening and reading file...')
with open('/Users/rafa/spell_checker/data/'+datasource) as csvfile, open('/Users/rafa/spell_checker/data/results_spell_checker.csv', 'w') as csv_file :
  reader = csv.DictReader(csvfile)
  fieldnames = ['id','comment_text','toxic']
  writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
  writer.writeheader()
  for row in reader:
    print('Processing next row...')
    blob = TextBlob(row[rowname])
    row ['comment_text'] = str(blob.correct())
    print('Writing row...')
    writer.writerow({'id': row['id'], 'comment_text': row['comment_text'], 'toxic':row ['toxic']})
