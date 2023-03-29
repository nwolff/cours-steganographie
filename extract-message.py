from numpy import asarray
from PIL import Image

if __name__ == "__main__":
    george_with_message = Image.open("assets/george-with-message.png")
    george_with_message_pixels = asarray(george_with_message)

    george = Image.open("assets/george.png")
    george_pixels = asarray(george)

    message_pixels = george_with_message_pixels - george_pixels
    message = Image.fromarray(message_pixels)
    brightened_message = message.point(lambda p: 255 if p > 0 else 0)
    brightened_message.save("build/extracted-message.png")
