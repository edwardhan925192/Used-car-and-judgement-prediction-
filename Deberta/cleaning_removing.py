# -*- coding: utf-8 -*-
"""Cleaning_removing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Lc_dj2Qhnfed_ywzrdmWb1lm0w3L_1LJ
"""

def cleaning (df = df_train, col_name = 'first_party'):
    df = df
    for index, row in df.iterrows():
        name = row[col_name]
        # Split 'first_party' into individual words
        name_split = name.split(' ')

        facts = row['facts']
        # Remove newline characters
        facts = facts.replace('\n', '')
        df.at[index, 'facts'] = facts

        # Split 'facts' into individual words
        facts_split = facts.split(' ')

        # List of words to clean
        words_to_clean = ["U.", "S.", "Mr.", "Ms.", "Mrs.", "Miss.", "U.S." ]

        # Check if any word in 'first_party' is the same as any word in 'facts'
        for name_word in name_split:
            for i, fact_word in enumerate(facts_split):
                # Check if the word from 'facts', minus any trailing punctuation, matches the current word from 'first_party'
                if name_word == re.sub(r'[^\w\s]$', '', fact_word):
                    # If word is in facts, remove trailing punctuation and update it
                    cleaned_word = re.sub(r'[^\w\s]$', '', fact_word)
                    df.at[index, 'facts'] = df.at[index, 'facts'].replace(fact_word, cleaned_word)
                # Additional check to clean specific words
                if fact_word == 'U.S.':
                    df.at[index, 'facts'] = df.at[index, 'facts'].replace(fact_word, 'US')

                if fact_word in words_to_clean:
                    cleaned_word = fact_word.replace('.', '')
                    df.at[index, 'facts'] = df.at[index, 'facts'].replace(fact_word, cleaned_word)


        # Additional check to remove dot at the end of the sentence
        if df.at[index, 'facts'].endswith('.'):
            df.at[index, 'facts'] = df.at[index, 'facts'][:-1]

    return df

def remove_short_words(sentence):
    words = str(sentence).split()
    long_words = [word for word in words if len(word) > 2]
    new_sentence = ' '.join(long_words)
    return new_sentence