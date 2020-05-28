import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel 
from rake_nltk import Rake
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

def return_csv():
    df = pd.read_csv('allrecipes.csv')
    df = df.drop_duplicates(subset='title', keep="first")
    df = df[['title','calories','ingredients']]
    return df

def gen_bag_of_words(df):
    key_words = []
    title = []

    for index, row in df.iterrows():
        ing = row['ingredients']
        #direct = row['directions']
        #cat = row['categories']
        #title.append(row['title'].strip())
        titl = row['title']
        
        r = Rake()

        # extracting the words by passing the text
        r.extract_keywords_from_text(ing+titl)

        # getting the dictionary whith key words as keys and their scores as values
        key_words_dict_scores = r.get_word_degrees()
        
        # assigning the key words to the new column for the corresponding movie
        key_words.append(list(key_words_dict_scores.keys()))
    df['Key_words'] = key_words
    #df['title'] = title
    df.drop(columns = ['ingredients'], inplace = True)
    df.set_index('title', inplace = True)
    bags = []
    columns = df.columns
    for index, row in df.iterrows():
        words = ''
        for col in columns:
            if col == 'Key_words':
                keys = [str(i) for i in row[col]]
                words = words + ' '.join(row[col])+ ' '
            else:
                words = words + str(row[col])+ 'col' +' '
        bags.append(words)
    df['bag_of_words'] = bags
    df.drop(columns = [col for col in df.columns if col!= 'bag_of_words'], inplace = True)

    return df

def return_cos_sim(df,df1):
    # instantiating and generating the count matrix
    count = CountVectorizer()
    count_matrix = count.fit_transform(df['bag_of_words'])
    count_matrix1 = count.transform(df1['bag_of_words'])

    cosine_sim = cosine_similarity(count_matrix, count_matrix1)

    # creating a Series for the recipe titles so they are associated to an ordered numerical
    # list I will use later to match the indexes
    indices = pd.Series(df.index)

    return indices, cosine_sim

def recommendation(indices,cosine_sim):
    recommended_recipes = []

    # creating a Series with the similarity scores in descending order
    i=0
    score_series = []
    
    for line in cosine_sim:
        score_series.append((np.mean(line),i))
        i+=1
    k = lambda a:a[0]
    
    sort_mean = sorted(score_series,reverse=True)
    #print(sort_mean)
    
    # populating the list with the titles of the best 10 matching recipes
    for i in sort_mean[1:11]:
        recommended_recipes.append(list(indices)[i[1]])
        
    return recommended_recipes

#df = return_csv()
#df1 = df.sample(5)
#df = gen_bag_of_words(df)
#df1 = gen_bag_of_words(df1)
#ind, cosine_sim = return_cos_sim(df,df1)

#print(list(df1.index),recommendation(ind,cosine_sim))