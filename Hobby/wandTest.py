from wand.image import Image
from wand.display import display

with Image(filename='moe.jpg') as img:
    print(img.size)
    img.type = 'grayscale';
    img.save(filename='moe.jpg');
    print(img.size)