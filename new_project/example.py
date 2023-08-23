import pandas as pd 

songs = pd.read_csv("top_10000_1960-now.csv")
artist_name_a = []

for index,row in songs.iterrows():
    time = row["Track Duration (ms)"]
    track_name = row["Track Name"]
    artist_name = row["Artist Name(s)"]
    
    if isinstance(artist_name,str) and  artist_name[0] == "A" and int(time/1000) > 120:
            value_dict = {"artist": artist_name, "time": time}
            artist_name_a.append(value_dict)
            print(artist_name_a)

    

    
