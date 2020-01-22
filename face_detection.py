# FACE DETECTION
from google.cloud import vision
from google.cloud.vision import types
from PIL import Image, ImageDraw
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/alex/sura-poc-analisis-de-sueno-297379928d09.json"
client = vision.ImageAnnotatorClient()



def detect_face(face_file, max_results=4):
    client = vision.ImageAnnotatorClient()
    content = face_file.read()
    image = types.Image(content=content)
    return client.face_detection(image=image, max_results=max_results).face_annotations


def highlight_faces(image, faces, output_filename):
    im = Image.open(image)
    draw = ImageDraw.Draw(im)
    # Sepecify the font-family and the font-size
    for face in faces:
        box = [(vertex.x, vertex.y)
               for vertex in face.bounding_poly.vertices]
        draw.line(box + [box[0]], width=5, fill='#00ff00')
        # Place the confidence value/score of the detected faces above the
        # detection box in the output image
        draw.text(((face.bounding_poly.vertices)[0].x,
                   (face.bounding_poly.vertices)[0].y - 30),
                  str(format(face.detection_confidence, '.3f')) + '%',
                  fill='#FF0000')
    im.save(output_filename)


def main(input_filename, output_filename, max_results):
    with open(input_filename, 'rb') as image:
        faces = detect_face(image, max_results)
        print('Found {} face{}'.format(
            len(faces), '' if len(faces) == 1 else 's'))
        print('Writing to file {}'.format(output_filename))
        # Reset the file pointer, so we can read the file again
        image.seek(0)
        highlight_faces(image, faces, output_filename)


route1="/home/alex/Imágenes/VID-20190814-WA0031/expresion3.png"
route2="/home/alex/Imágenes/VID-20190814-WA0031/expresion3_analisis.png"

main(route1, route2, 1)




def return_feelings():
    indexes = [('joy_likelihood', 'Felicidad'), ('sorrow_likelihood', 'tristeza'), ('anger_likelihood', 'enojo'), ('surprise_likelihood', 'sorpresa')]
    response = client.annotate_image({
        'image': {'source': {'image_uri': 'gs://raw-video-files-89guyjhb5/VID-20190814-WA0032/presentacion.png'}},
        'features': [{'type': vision.enums.Feature.Type.FACE_DETECTION}],
    })
    for index in indexes:
        cmd = "response.face_annotations[0]." + index[0]
        if eval(cmd) >= 2:
            print(eval(cmd))
            print(index[1])