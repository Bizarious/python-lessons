# 1# definiere ein passwort, frage den input des Terminals ab,
# bis es richtig eingegeben wurde
passwort = 'somepasswort123'
asking_again = True
while asking_again:
    if input("Passwort: ") == passwort:
        asking_again = False
        print('Eingeloggt')

# 2# Sammle alle falsch eingegebenen Passwörter und gib sie aus
# wenn das passwort richtig eingegeben wurde, sowie die Anzahl
asking_again = True
wrong_passwords = []
while asking_again:
    entered_password = input("Passwort: ")
    if entered_password == passwort:
        asking_again = False
        print("Eingeloggt")
    else:
        wrong_passwords.append(entered_password)
        print("Falsche Eingabe")
print(f"Falsche Versuche: {len(wrong_passwords)}, falsche Passworter: {wrong_passwords}")

# 3# Gib über das Terminal die maximale Anzahl von Eingabeversuchen
# für das Passwort ein
max_pw_trys = int(input("Anzahl der Versuche: "))
current_try = 0
while max_pw_trys > current_try:
    current_try += 1
    if input("Passwort: ") == passwort:
        print("Eingeloggt")
        break
    print("Falsche Eingabe")
