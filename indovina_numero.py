# INDOVINA IL NUMERO SEGRETO
# Un semplice gioco dove il computer sceglie un numero a caso e tu devi indovinare

import random  # Questa libreria serve per generare numeri casuali

# Messaggio di benvenuto
print(" BENVENUTO AL GIOCO 'INDOVINA IL NUMERO'!")
print("Ho pensato a un numero segreto tra 1 e 20.")
print("Prova a indovinare in meno tentativi possibile!")

# Il computer sceglie un numero segreto tra 1 e 20
numero_segreto = random.randint(1, 20)

# Questa variabile terrà il conto dei tentativi fatti
tentativi = 0

# Inizia il ciclo: finché non indovini, continua a chiedere
while True:
    # Chiediamo all'utente di inserire un numero
    risposta = input("Inserisci il tuo numero: ")
    
    # Convertiamo la risposta (che è testo) in un numero intero
    # Nota: se l'utente scrive una lettera, il programma si fermerebbe.
    # Per semplicità, diamo per scontato che l'utente inserisca un numero valido.
    tentativo = int(risposta)
    
    # Aumentiamo il contatore dei tentativi
    tentativi = tentativi + 1
    
    # Controlliamo se il numero è giusto, troppo alto o troppo basso
    if tentativo == numero_segreto:
        print(f" COMPLIMENTI! Hai indovinato in {tentativi} tentativi!")
        break  # Esce dal ciclo while
    elif tentativo < numero_segreto:
        print(" Troppo basso! Prova con un numero più alto.")
    else:
        print(" Troppo alto! Prova con un numero più basso.")

print("Grazie per aver giocato! 🎮")