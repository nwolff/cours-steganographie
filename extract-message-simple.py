from PIL import Image, ImageChops

if __name__ == "__main__":
    george_with_message = Image.open("assets/george-with-message.png")
    george = Image.open("assets/george.png")
    message = ImageChops.difference(george_with_message, george)
    # ImageEnhance.Contrast(message).enhance(100)
    # ImageEnhance.Brightness(message).enhance(100)
    message = message.point(lambda p: 255 if p > 0 else 0)
    message.save("build/extracted-message-simple.png")
