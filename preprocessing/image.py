from PIL import Image

MAX_SIZE = (1024, 1024)

def prepare_image(image_path):
    image = Image.open(image_path)
    image.thumbnail(MAX_SIZE)
    return image