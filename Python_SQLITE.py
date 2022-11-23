####################################################
##  Cours MCNDU 2021
##  Python et SQLITE
####################################################
import pandas as pd
import os
import sqlite3

# ctrl+1 單行註解
# ctrl+4&5 多行註解

#import csv

#Pour se placer dans le bon répertoire
dir_Simu_Results = os.chdir('D:\Fafa\Downloads\Python-SQLITE-23\Python-SQLITE-23')

#Chargement d'un fichier .csv
communes = pd.read_csv('Data/Communes.txt', sep=';',encoding='latin-1')#,dtype={
  #  'CODNUM':'str','REG':'str','CODEPOSTAL':'str','EPCIMODIF':'str','DEP':'str'})

#Liste de tous les noms de colonnes
list(communes.columns)

#COnnection à la base de données
conn = sqlite3.connect('DB_Communes.db')
cur = conn.cursor() 

#Deux manières de créer une table dans la base de données à partir d'une dataframe
communes.to_sql("Table_Communes", conn, if_exists='append', index=False)
#Soit (IF NOT EXISTS)
cur.execute("""CREATE TABLE IF NOT EXISTS  list_communes (CODGEO , P16_POP)""")
cur.executemany("INSERT INTO list_communes (CODGEO, P16_POP) VALUES (?, ?)", communes[["CODGEO","P16_POP"]].values.tolist())
#verification
cur.execute(" SELECT * FROM list_communes").fetchone()
for row in cur.execute("SELECT * FROM list_communes LIMIT 10"):
    print (row)
    
#Supprimer une table
#cur.execute("""DROP TABLE list_communes""")

# =============================================================================
# 
# #Pour voir la liste des tables de la base de données :
# cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
# print(cur.fetchall())
# 
# #Pour voir la table sans tout afficher : 
# #Methode 1
# =============================================================================
# cur.execute(" SELECT * FROM list_communes LIMIT 10")
# cur.fetchall()
# for resultat in cur:
#      print(resultat)
# =============================================================================
# #Methode 2
#cur.execute(" SELECT * FROM Table_Communes").fetchone()
# 
# cur.execute(" SELECT * FROM Table_Communes WHERE P16_POP > 10000")
# #Affichage à l'écran : 
# #cur.fetchall()
# #ou :
# for resultat in cur:
#     print(resultat)
# 
# #Compte le nombre de ligne dans la table
# cur.execute("SELECT COUNT(*) FROM Table_Communes")
# cur.fetchall()
# 
# #On peut rajouter des selections : 
# =============================================================================
# cur.execute("SELECT * FROM Table_Communes WHERE  P11_POP - P16_POP > 0")
# # 
# data = cur.fetchall() 
# pd_communes_lost_residents = pd.DataFrame(data)                   
# =============================================================================
# 
# #Creation d'une table departement à partir des communes : 
cur.execute("""DROP TABLE Departement""")
cur.execute("CREATE TABLE Departement AS SELECT DEP,SUM(P11_POP),SUM(P16_POP) FROM Table_Communes GROUP BY DEP")
cur.execute("SELECT * FROM Departement")
# 
data = cur.fetchall() 
pd_France_Department = pd.DataFrame(data)  
print(pd_France_Department)                 
# 
conn.commit()
conn.close()
# 




    
import datetime 
import pandas as pd
import time

while True:
    time.sleep(1)
    print("I'm working...")
    now = datetime.datetime.now()
    now_str = now.strftime("%Y-%m-%d-%H-%M-%S")
    print("date and time =", now_str)	
    pd_France_Department.to_csv('BUS-'+now_str+'.csv',index=False)

# datetime object containing current date and time


now = datetime.datetime.now()
 
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d-%m-%Y-%H-%M-%S")
print("date and time =", dt_string)	
now_str = now.strftime("%Y-%m-%d-%H-%M")
print("date and time =", now_str)	
# Get the current date and time
now = datetime.datetime.now()
now_str = now.strftime("%Y-%m-%d")

# #Enregistrement dans un fichier csv
pd_France_Department.to_csv('bus-'+now_str+'.csv',index=False)
pd_France_Department.to_csv('q',index=False)
# 
# 
# =============================================================================

import datetime
str1 = "\n".join(data)

# Get the current date and time
now = datetime.datetime.now()
now_str = now.strftime("%Y-%m-%d")

# Write out to a file for today
outfilename = 'sampledata-{}.csv'.format(now_str)

outFile = open(outfilename, 'write')
outFile.write(str1)
outFile.close()