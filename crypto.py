def chiffrer_cesar(message_clair, decalage):
    message_chiffre = ""

    for caractere in message_clair:
        if caractere.isalpha():  # Vérifie si le caractère est une lettre
            majuscule = caractere.isupper()  # Vérifie si le caractère est en majuscule
            caractere = caractere.lower()  # Convertit en minuscule pour le traitement

            # Chiffrement en utilisant la formule de César
            decalage_cesar = (ord(caractere) - ord('a') + decalage) % 26
            caractere_chiffre = chr(decalage_cesar + ord('a'))

            # Restaure la majuscule si c'était le cas dans le message original
            if majuscule:
                caractere_chiffre = caractere_chiffre.upper()

            message_chiffre += caractere_chiffre
        else:
            # Ajoute les caractères non alphabétiques tels quels
            message_chiffre += caractere

    return message_chiffre


def dechiffrer_cesar(message_chiffre, decalage):
    message_dechiffre = ""

    for caractere in message_chiffre:
        if caractere.isalpha():  # Vérifie si le caractère est une lettre
            majuscule = caractere.isupper()  # Vérifie si le caractère est en majuscule
            caractere = caractere.lower()  # Convertit en minuscule pour le traitement

            # Déchiffrement en utilisant la formule de César
            decalage_inverse = (ord(caractere) - ord('a') - decalage) % 26
            caractere_dechiffre = chr(decalage_inverse + ord('a'))

            # Restaure la majuscule si c'était le cas dans le message original
            if majuscule:
                caractere_dechiffre = caractere_dechiffre.upper()

            message_dechiffre += caractere_dechiffre
        else:
            # Ajoute les caractères non alphabétiques tels quels
            message_dechiffre += caractere

    return message_dechiffre


# Menu principal
while True:
    print("\n1. Chiffrer un message")
    print("2. Déchiffrer un message")
    print("3. Quitter")

    choix = input("Choisissez une option (1/2/3) : ")

    if choix == "1":
        message_clair = input("Entrez le message clair : ")
        decalage_chiffrement = int(input("Entrez le décalage de chiffrement : "))
        message_chiffre = chiffrer_cesar(message_clair, decalage_chiffrement)
        print("Message chiffré :", message_chiffre)

    elif choix == "2":
        message_chiffre = input("Entrez le message chiffré : ")
        decalage_dechiffrement = int(input("Entrez le décalage de déchiffrement : "))
        message_dechiffre = dechiffrer_cesar(message_chiffre, decalage_dechiffrement)
        print("Message déchiffré :", message_dechiffre)

    elif choix == "3":
        print("Programme terminé.")
        break

    else:
        print("Option invalide. Veuillez choisir 1, 2 ou 3.")
