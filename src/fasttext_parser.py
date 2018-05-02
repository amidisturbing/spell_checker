import pandas as pa

def to_fasttest_label(label):
    return "__label__"+label;

df=pa.read_csv("../data/kaggle-data-short.csv")
toxic_df=df[['comment_text','toxic']]
toxic_df['toxic']=toxic_df['toxic'].astype(str)
print (toxic_df['toxic'])
toxic_df['toxic']=toxic_df['toxic'].apply(to_fasttest_label)
toxic_df.to_csv('comments_toxic',columns=['toxic','comment_text'], sep=' ',index=False,header=False,encoding='utf-8')

