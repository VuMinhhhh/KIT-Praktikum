file = open('TextFile1.txt','r')
print("Geben Sie den Schlüssel:", end = "")
Schlüssel = int(input())
print("Geben Sie den Klartext:", end = "")
Klartext = input()
Geheimtext = ""
for i in range (len(Klartext)):
    if Klartext[i] == ' ':
        Geheimtext += ' '
    else: 
        Geheimtext += chr((ord(Klartext[i]) - 97 + Schlüssel) % 26  + 97)
print("Hier ist den Geheimtext:", Geheimtext)
file.close()
