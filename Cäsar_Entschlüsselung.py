Unigram_Häufigkeit = {
    'e': 17.4, 'n': 9.78, 'i': 7.55, 's': 7.27, 'r': 7.0, 'a': 6.51,
    't': 6.15, 'd': 5.08, 'h': 4.76, 'u': 4.35, 'l': 3.44, 'c': 3.06,
    'g': 3.01, 'm': 2.53, 'o': 2.51, 'b': 1.89, 'w': 1.89, 'f': 1.66,
    'k': 1.21, 'z': 1.13, 'p': 0.79, 'v': 0.67, 'j': 0.27, 'y': 0.04,
    'x': 0.03, 'q': 0.02
}
Wert_Unigram = 1.0

Bigram_Häufigkeit = {
    'er': 12.88, 'en': 11.88, 'ch': 9.22, 'de': 7.40, 
    'ei': 6.30, 'in': 6.23, 'te': 6.03, 'ie': 5.24, 
    'ge': 4.57, 'nd': 4.34, 'un': 4.17, 'be': 3.90
}
Wert_Bigram = 2.0

Trigram_Häufigkeit = {
    'sch': 8.54, 'der': 7.64, 'ich': 6.71, 'ein': 6.63,
    'che': 5.93, 'die': 5.10, 'und': 4.40, 'ung': 3.97,
    'eit': 2.60
}
Wert_Trigram = 3.0

def Entschlüsselung (Geheimtext, Schlüssel):
    Klartext = ""
    for i in range (len(Geheimtext)):
        if Geheimtext[i] == ' ':
            Klartext += ' '
        else: 
            Klartext += chr((ord(Geheimtext[i]) - 97 - Schlüssel) % 26  + 97)
    return Klartext

def Wert_n_gram (Geheimtext, n_gram_Häufigkeit, n):
    Wert = 0
    for i in range (len(Geheimtext) - n + 1):
        temp = ""
        temp = Geheimtext[i : i + n]
        Wert += n_gram_Häufigkeit.get(temp, 0)
    return Wert

def Wert(Klartext):
    Wert = 0
    Wert += Wert_n_gram(Klartext, Unigram_Häufigkeit, 1) * Wert_Unigram
    Wert += Wert_n_gram(Klartext, Bigram_Häufigkeit, 2) * Wert_Bigram
    Wert += Wert_n_gram(Klartext, Trigram_Häufigkeit, 3) * Wert_Trigram
    return Wert
    
print("Geben Sie den Geheimtext:", end = "")
Geheimtext = input()
Klartext = ""
Wert_Klartext = 0
for Schlüssel in range (26):
    entschlüsselt = Entschlüsselung(Geheimtext, Schlüssel)
    Wert_entschlüsselt = Wert(entschlüsselt)
    if Wert_entschlüsselt > Wert_Klartext:
        Klartext = entschlüsselt
        Wert_Klartext = Wert_entschlüsselt
print("Hier ist wahrscheinlich der Klartext:", end = "")
print(Klartext)
