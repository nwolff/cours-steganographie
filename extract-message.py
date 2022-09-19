from PIL import Image
from numpy import asarray

if __name__ == "__main__":
    george_with_poems = Image.open("assets/george-with-message.png")
    george_with_poems_pixels = asarray(george_with_poems)

    george = Image.open("assets/george.png")
    george_pixels = asarray(george)

    poems_pixels = george_with_poems_pixels - george_pixels
    poems = Image.fromarray(poems_pixels)
    brightened_poems = poems.point(lambda p: 255 if p > 0 else 0)
    brightened_poems.save("build/extracted-message.png")
