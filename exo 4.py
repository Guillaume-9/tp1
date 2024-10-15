min=int(input(print("Donnez le nombre de minutes : ")))
jour=(min%1440)-1
heure=min%60
minute=min-jour-heure
print(f"Il y a donc {jour} jour, {heure} heures et {minute} minutes")