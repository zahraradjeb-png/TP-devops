def afficher_accueil():
    print("Connexion : bienvenue utilisateur")


def main():
    afficher_accueil()
    taches = ["Apprendre Git", "Faire le TP DevOps"]
    for numero, tache in enumerate(taches, start=1):
        print(f"{numero}. {tache}")


if __name__ == "__main__":
    main()
