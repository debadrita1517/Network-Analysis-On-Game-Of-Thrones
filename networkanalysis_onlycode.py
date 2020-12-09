import pandas as pd
book1 = pd.read_csv('https://raw.githubusercontent.com/debadrita1517/Network-Analysis-On-Game-Of-Thrones/main/book1.csv')
book1.head()
import networkx as nx
G_book1 = nx.Graph()
for i, edge in book1.iterrows():
    G_book1.add_edge(edge['Source'], edge['Target'], weight=edge['weight'])
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
deg_cen_book1 = nx.degree_centrality(books[0])
deg_cen_book5 = nx.degree_centrality(books[4])
sorted_deg_cen_book1 = sorted(deg_cen_book1.items(), key=lambda x: x[1], reverse=True)[0:10]
sorted_deg_cen_book5 = sorted(deg_cen_book5.items(), key=lambda x: x[1], reverse=True)[0:10]
print(sorted_deg_cen_book1)
print(sorted_deg_cen_book5)
evol = [nx.degree_centrality(book) for book in books]
degree_evol_df = pd.DataFrame.from_records(evol)
degree_evol_df[['Eddard-Stark', 'Tyrion-Lannister', 'Jon-Snow']].plot();
evol = [nx.betweenness_centrality(book, weight='weight') for book in books]
betweenness_evol_df = pd.DataFrame.from_records(evol).fillna(0)
set_of_char = set()
for i in range(5):
    set_of_char |= set(list(betweenness_evol_df.T[i].sort_values(ascending=False)[0:4].index))
list_of_char = list(set_of_char)
betweenness_evol_df[list_of_char].plot(figsize=(13, 7));
evol = [nx.pagerank(book, weight='weight') for book in books]
pagerank_evol_df = pd.DataFrame.from_records(evol)
set_of_char = set()
for i in range(5):
    set_of_char |= set(list(pagerank_evol_df.T[i].sort_values(ascending=False)[0:4].index))
list_of_char = list(set_of_char)
pagerank_evol_df[list_of_char].plot(figsize=(13, 7));
measures = [nx.pagerank(books[4]), 
            nx.betweenness_centrality(books[4], weight='weight'), 
            nx.degree_centrality(books[4])]
cor = pd.DataFrame.from_records(measures)
cor.corr().T
p_rank, b_cent, d_cent = cor.idxmax(axis=1)
print(p_rank)
print(b_cent)
print(d_cent)
