with open('Klartext.txt','r') as file:
    Klartext = file.read()
print("Geben Sie den Schluessel:", end = "")
Schluessel = int(input())
Geheimtext = ""
for i in range (len(Klartext)):
    zum_ascii = ord(Klartext[i])
    if Klartext[i] == ' ':
        Geheimtext += ' '
    elif 97 <= zum_ascii and zum_ascii <= 122: 
        Geheimtext += chr((zum_ascii - 97 + Schluessel) % 26  + 97)
    elif 65 <= zum_ascii and zum_ascii <= 90: 
        Geheimtext += chr((zum_ascii - 65 + Schluessel) % 26  + 65)
print("Hier ist den Geheimtext:", Geheimtext)
with open('Geheimtext.txt', 'w') as file:
    file.write(Geheimtext)
