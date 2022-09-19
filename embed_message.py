from PIL import Image
from numpy import asarray

if __name__ == "__main__":
    message = Image.open("assets/message.png")
    darkened_message = message.point(lambda p: p // 255)
    darkened_message_pixels = asarray(darkened_message)

    george = Image.open("assets/george.png")
    george_pixels = asarray(george)

    addition = george_pixels + darkened_message_pixels

    resultImage = Image.fromarray(addition)
    resultImage.save("assets/george-with-message.png")
