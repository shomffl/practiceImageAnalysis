import io
import os
from dotenv import load_dotenv
from google.cloud import vision


load_dotenv()

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]

client = vision.ImageAnnotatorClient()

file_name = os.path.abspath('./images/myshelf_1.jpg')



def detect_text(path):
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    return texts

texts = detect_text(file_name)
print('\n"{}"'.format(texts[0].description))
