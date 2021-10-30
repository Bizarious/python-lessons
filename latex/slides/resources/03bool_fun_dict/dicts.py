# ein dictionary erstellen
lexikon = dict()
lexikon = {}
lexikon = {"Haus": "Substantiv", "stehlen": "Verb", "Geld": "Substantiv"}

# einen wert per key auslesen
x = lexikon["Haus"] # "Substantiv"
# einen neues paar einfügen
lexikon["neu"] = "Adjektiv"
# einen wert überschreiben
lexikon["Haus"] = "Verb"

# keys und values eines dictionarys
keys = lexikon.keys()
values = lexikon.values()

# durch ein dictionary iterieren
for key in lexikon.keys():
    print(f"key : {key}")
    value = lexikon[key]
    print(f"value: {value}")
