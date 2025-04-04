file = open('TextFile1.txt','r')
print("Geben Sie den Schluessel:", end = "")
schluessel = int(input())
print("Geben Sie den Klartext:", end = "")
stri = input()
stro = ""
for i in range (len(stri)):
    if stri[i] == ' ':
        stro += ' '
    else: 
        stro += chr((ord(stri[i]) - 65 + schluessel) % 26  + 65)
print("Hier ist den Geheimtext:", stro)
file.close()
