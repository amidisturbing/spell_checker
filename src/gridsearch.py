import fasttext
import numpy as np
import sklearn.metrics as skm
import pandas as pd

word_ngrams=[1,2]
lr=[100,200]
dim=[100,200]
ws=[100,200]
epoch=[25,50]
los_function=['softmax','softmax']


def to_fasttest_label(label):
    return "__label__"+label;


test_data_df=pd.read_csv('tweet_class_pre.valid',delim_whitespace=True,index_col=False,names=['label','comment','shit'])

with open('gridsearch.csv', 'a') as the_file:
        the_file.write('wordNgrams,lr,dim,ws,epoch,loss_funcrtion\n')
        for i in range(0, len(word_ngrams)):
            the_file.write(str(word_ngrams[i])+','+str(lr[i] )+ ','+ str(dim[i])+','+ str(ws[i])+','+str(epoch[i])+','+los_function[i])
            the_file.write("\n")
            classifier = fasttext.supervised('tweet_class_pre.train', 'model',epoch=epoch[i],word_ngrams=word_ngrams[i],dim=dim[i])
            
            labels = classifier.predict(test_data_df['comment'])
            predicted_labels_df = pd.DataFrame(labels, columns=["label"])
            predicted_labels_df['label']=predicted_labels_df['label'].apply(to_fasttest_label)

            the_file.write("\n")
            the_file.write(str(skm.classification_report(test_data_df['label'], predicted_labels_df['label'])))
            the_file.write("\n f1 macro: ")
            the_file.write(str(skm.precision_recall_fscore_support(test_data_df['label'], predicted_labels_df['label'], average='macro')[2]))
            the_file.write("\n f1 micro: ")
            the_file.write(str(skm.precision_recall_fscore_support(test_data_df['label'], predicted_labels_df['label'], average='micro')[2]))
            the_file.write("\n")
            the_file.write("-------------------,---------------------,------------------------,----------------------")
            the_file.write("\n \n")
the_file.close()