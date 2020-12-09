# -*- coding: utf-8 -*-
"""NetworkAnalysis_GOT.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iunxJ33mOhVeEv4S_ERrc4EVNG3PjnGP

# **WINTER IS COMING....**
"""

# Importing modules
import pandas as pd
# Reading in datasets/book1.csv
book1 = pd.read_csv('https://raw.githubusercontent.com/debadrita1517/Network-Analysis-On-Game-Of-Thrones/main/book1.csv')
# Printing out the head of the dataset
book1.head()

"""# **Uploading the Network of Thrones -**"""

# Importing modules
import networkx as nx
# Creating an empty graph object
G_book1 = nx.Graph()

"""# **Populating the Network with the Dataframe -**"""

# Iterating through the DataFrame to add edges
for i, edge in book1.iterrows():
    G_book1.add_edge(edge['Source'], edge['Target'], weight=edge['weight'])
# Creating a list of networks for all the books
books = [G_book1]
book_fnames = ['https://raw.githubusercontent.com/debadrita1517/Network-Analysis-On-Game-Of-Thrones/main/book2.csv', 
               'https://raw.githubusercontent.com/debadrita1517/Network-Analysis-On-Game-Of-Thrones/main/book3.csv', 
               'https://raw.githubusercontent.com/debadrita1517/Network-Analysis-On-Game-Of-Thrones/main/book4.csv', 
               'https://raw.githubusercontent.com/debadrita1517/Network-Analysis-On-Game-Of-Thrones/main/book5.csv']
for book_fname in book_fnames:
    book = pd.read_csv(book_fname)
    G_book = nx.Graph()
    for _, edge in book.iterrows():
        G_book.add_edge(edge['Source'], edge['Target'], weight=edge['weight'])
    books.append(G_book)

"""# **The Most Important Character in The Game of Thrones -**"""

# Calculating the degree centrality of book 1
deg_cen_book1 = nx.degree_centrality(books[0])
# Calculating the degree centrality of book 5
deg_cen_book5 = nx.degree_centrality(books[4])
# Sorting the dictionaries according to their degree centrality and storing the top 10
sorted_deg_cen_book1 = sorted(deg_cen_book1.items(), key=lambda x: x[1], reverse=True)[0:10]
# Sorting the dictionaries according to their degree centrality and storing the top 10
sorted_deg_cen_book5 = sorted(deg_cen_book5.items(), key=lambda x: x[1], reverse=True)[0:10]
# Printing out the top 10 of book1 and book5
print(sorted_deg_cen_book1)
print(sorted_deg_cen_book5)

"""# **Evolution of the Importance of Characters in the Book -**"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
# Creating a list of degree centrality of all the books
evol = [nx.degree_centrality(book) for book in books]
# Creating a DataFrame from the list of degree centralities in all the books
degree_evol_df = pd.DataFrame.from_records(evol)
# Plotting the degree centrality evolution of Eddard-Stark, Tyrion-Lannister and Jon-Snow
degree_evol_df[['Eddard-Stark', 'Tyrion-Lannister', 'Jon-Snow']].plot();

"""# **What's up with Stannis Baratheon ?**"""

# Creating a list of betweenness centrality of all the books just like we did for degree centrality
evol = [nx.betweenness_centrality(book, weight='weight') for book in books]
# Making a DataFrame from the list
betweenness_evol_df = pd.DataFrame.from_records(evol).fillna(0)
# Finding the top 4 characters in every book
set_of_char = set()
for i in range(5):
    set_of_char |= set(list(betweenness_evol_df.T[i].sort_values(ascending=False)[0:4].index))
list_of_char = list(set_of_char)
# Plotting the evolution of the top characters
betweenness_evol_df[list_of_char].plot(figsize=(13, 7));

"""# **What Google PageRank Algorithm tells about Game of Thrones ?**"""

# Creating a list of pagerank of all the characters in all the books
evol = [nx.pagerank(book, weight='weight') for book in books]
# Making a DataFrame from the list
pagerank_evol_df = pd.DataFrame.from_records(evol)
# Finding the top 4 characters in every book
set_of_char = set()
for i in range(5):
    set_of_char |= set(list(pagerank_evol_df.T[i].sort_values(ascending=False)[0:4].index))
list_of_char = list(set_of_char)
# Plotting the top characters
pagerank_evol_df[list_of_char].plot(figsize=(13, 7));

"""# **Correlation between Different Measures -**"""

# Creating a list of pagerank, betweenness centrality, degree centrality
# of all the characters in the fifth book.
measures = [nx.pagerank(books[4]), 
            nx.betweenness_centrality(books[4], weight='weight'), 
            nx.degree_centrality(books[4])]
# Creating the correlation DataFrame
cor = pd.DataFrame.from_records(measures)
# Calculating the correlation
cor.corr().T

"""# **Conclusion -**"""

# Finding the most important character in the fifth book,  
# according to degree centrality, betweenness centrality and pagerank.
p_rank, b_cent, d_cent = cor.idxmax(axis=1)
# Printing out the top character accoding to the three measures
print(p_rank)
print(b_cent)
print(d_cent)