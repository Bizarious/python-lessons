# Der letzte Versuch
# Definiert 3 Variablen (gelernt, glueck, aufgepasst) die True oder False sind.
gelernt = True
glueck = True
aufgepasst = False

# #1 Wenn (a) eine (b) zwei der 3 Variablen True sind, hat der Student bestanden,
# und es soll True ausgegeben werden
bestanden = gelernt and glueck or gelernt and aufgepasst or glueck and aufgepasst
print(bestanden)

# #2 Definiere eine weitere Variable (beitrag_bezahlt)
# und setzte sie auf True oder False
# es soll angezeigt werden ob der Student exmatrikuliert wird, dies hängt davon
# ab ob er den Beitrag bezahlt / bestanden hat.
beitrag_bezahlt = False
exmatrikuliert = not beitrag_bezahlt or not bestanden
