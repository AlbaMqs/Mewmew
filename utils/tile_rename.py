import os

def renommer_images_plage(dossier, prefixe, plage_debut, plage_fin, nouveau_suffixe):
    """
    Renomme les fichiers d'une plage spécifique de suffixes numériques.
    
    Arguments :
    - dossier : chemin du dossier contenant les fichiers.
    - prefixe : préfixe commun à tous les fichiers (ex : "prefixe").
    - plage_debut : premier numéro de la plage à renommer (ex : 15).
    - plage_fin : dernier numéro de la plage à renommer (ex : 45).
    - nouveau_suffixe : nouveau suffixe à ajouter (ex : "ajout").
    """
    # Génère les noms des fichiers à partir de la plage
    fichiers_cibles = [f"{prefixe}_{str(i).zfill(3)}.png" for i in range(plage_debut, plage_fin + 1)]
    
    # Filtrer uniquement les fichiers qui existent dans le dossier
    fichiers = [f for f in fichiers_cibles if os.path.exists(os.path.join(dossier, f))]
    
    # Calcul de la largeur pour le nouveau format
    total = len(fichiers)
    largeur = len(str(total - 1))
    nouveau_format = f"{prefixe}_{nouveau_suffixe}_{{:0{largeur}d}}.png"
    
    for index, fichier in enumerate(fichiers):
        ancien_chemin = os.path.join(dossier, fichier)
        nouveau_nom = nouveau_format.format(index)
        nouveau_chemin = os.path.join(dossier, nouveau_nom)
        
        # Renommer le fichier
        os.rename(ancien_chemin, nouveau_chemin)
        print(f"Renommé : {ancien_chemin} -> {nouveau_chemin}")

# Exemple d'utilisation
dossier = "assets/sprites/characters/base"  # Remplacez par le chemin de votre dossier
prefixe = "base"  # Préfixe commun aux fichiers
plage_debut = 0  # Numéro de début de la plage (ex : 015)
plage_fin = 7  # Numéro de fin de la plage (ex : 045)
nouveau_suffixe = "idle_down"  # Nouveau suffixe à ajouter

renommer_images_plage(dossier, prefixe, plage_debut, plage_fin, nouveau_suffixe)
