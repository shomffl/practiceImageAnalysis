import io
import os
from dotenv import load_dotenv
from google.cloud import vision


load_dotenv()

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]

client = vision.ImageAnnotatorClient()

file_name = os.path.abspath('./images/canvas3.png')


with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)

response = client.label_detection(image=image)
labels = response.label_annotations

print('Labels:')
for label in labels:
    print(label.description)
