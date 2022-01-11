with open("examplefile.txt", "w+") as f:
    # Datei ist hier offen
    f.readline()
    f.write("test")
# Datei ist hier nicht länger geöffnet
