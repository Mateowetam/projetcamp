import pandas as pd

df = pd.read_csv("lieuxDF.csv")

with open("insert_script.txt", "w", encoding="utf-8") as f:
    for i, row in df.iterrows():
        id_val = i + 1
        
        lat = row["Latitude"]
        lon = row["Longitude"]
        lien = row["lien"]
        
        insert_line = (
            f"INSERT INTO sitecamp_lieux (id, latitude, longitude, lien) "
            f"VALUES ({id_val}, {lat}, {lon}, '{lien}');\n"
        )
        
        f.write(insert_line)

print("Fichier 'insert_script.sql' généré avec succès !")
