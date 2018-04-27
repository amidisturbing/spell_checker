from textblob import TextBlob
import pandas as pd
import csv

test_data_df=pd.read_csv('/Users/rafa/spell_checker/data/labeled_data_ol_short.csv')
print(test_data_df['tweet'])
df = test_data_df['tweet'].to_string

with open('/Users/rafa/spell_checker/data/labeled_data_ol_short.csv', newline='') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
     	print(row['tweet'])
     	blob = TextBlob(row['tweet'])
     	corrected = blob.correct()
     	print(corrected)
