from PIL import Image
import os

def split_image(image_path, output_width, output_height, margin_x, margin_y, start_x=0, start_y=0):
    """
    Lit une image, la découpe en sous-images, et sauvegarde ces sous-images.

    :param image_path: Chemin de l'image source.
    :param output_width: Largeur des sous-images.
    :param output_height: Hauteur des sous-images.
    :param margin_x: Marge horizontale entre chaque sous-image.
    :param margin_y: Marge verticale entre chaque sous-image.
    :param start_x: Coordonnée X de départ (en pixels).
    :param start_y: Coordonnée Y de départ (en pixels).
    """
    try:
        # Ouvre l'image source
        img = Image.open(image_path)
        img_width, img_height = img.size

        # Extraire le nom du fichier sans extension
        original_name = os.path.splitext(os.path.basename(image_path))[0]

        # Calcul des positions pour la découpe
        count = 0  # Compteur pour nommer les sous-images
        output_dir = os.path.dirname(image_path)

        for y in range(start_y, img_height, output_height + margin_y):
            for x in range(start_x, img_width, output_width + margin_x):
                # Vérifie si le sous-rectangle reste dans les limites de l'image
                if x + output_width <= img_width and y + output_height <= img_height:
                    # Découpe le rectangle
                    box = (x, y, x + output_width, y + output_height)
                    cropped_img = img.crop(box)

                    # Nom du fichier pour la sous-image (nom original + numéro)
                    output_file = os.path.join(
                        output_dir, f"{original_name}_{count:03d}.png"
                    )
                    cropped_img.save(output_file)
                    print(f"Sous-image sauvegardée : {output_file}")
                    count += 1

        print(f"Découpage terminé. {count} sous-images générées.")
    except Exception as e:
        print(f"Erreur : {e}")

# Exemple d'utilisation
if __name__ == "__main__":
    image_path = "assets/sprites/characters/base.png"  # Remplace par le chemin de ton image
    output_width = 16  # Largeur des sous-images
    output_height = 16  # Hauteur des sous-images
    margin_x = 32  # Marge horizontale
    margin_y = 32  # Marge verticale
    start_x = 16  # Point de départ X
    start_y = 16  # Point de départ Y

    split_image(image_path, output_width, output_height, margin_x, margin_y, start_x, start_y)
