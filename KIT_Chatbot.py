# -*- coding: utf-8 -*-
import random
import meine_Variablen

def Antworten(Benutzer_Woeter):
    in_Reaktionsantworten = False
    for Einzelwoeter in Benutzer_Woeter:
        if Einzelwoeter in meine_Variablen.Reaktionsantworten:
            print(meine_Variablen.Reaktionsantworten[Einzelwoeter])
            in_Reaktionsantworten = True
    if in_Reaktionsantworten == False:
        print(random.choice(meine_Variablen.Zufallsantworten))

print("Willkommen beim Chatbot")
print("Wonach möchten Sie sich gerne erkundigen")
print("Zum Beenden einfach eintippen")
print("")
Benutzer_Eingabe = ""
while(Benutzer_Eingabe != "bye"):   
    leer_Eingabe = True
    while leer_Eingabe == True:
        Benutzer_Eingabe = input("Ihre Frage/Antwort: ")
        if Benutzer_Eingabe.strip() == "":
            print ("Wie bitte?")
            leer_Eingabe = True
        else:
            leer_Eingabe = False
    Benutzer_Eingabe = Benutzer_Eingabe.lower()
    Benutzer_Woeter = Benutzer_Eingabe.split()
    Antworten(Benutzer_Woeter)

    
