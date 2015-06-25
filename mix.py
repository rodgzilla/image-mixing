import sys
from PIL import Image
import random

def get_image_data(image):
    """This function load the image into a 2 dimensional array of pixels.

    """
    data = [[0] * image.size[1] for _ in range(image.size[0])]

    for x in range(image.size[0]):
        for y in range(image.size[1]):
            data[x][y] = image.getpixel((x, y))

    return image.size[0], image.size[1], data

def save_data(width, height, data, filename):
    """This function save a 2 dimensional array of pixels into a file.

    """
    img = Image.new('RGB', (width, height))
    img.putdata([data[x][y] for y in range(height) for x in
                 range(width)])
    img.save(filename)
    img.close()

def mix_line(width, height, data_img1, data_img2):
    data = [[0] * height for _ in range(width)]

    for y in range(height):
        line_source = data_img1 if y % 2 == 0 else data_img2
        for x in range(width):
            data[x][y] = line_source[x][y]

    return data

def mix_line_random(width, height, data_img1, data_img2):
    data = [[0] * height for _ in range(width)]

    for y in range(height):
        line_source = random.choice([data_img1, data_img2])
        for x in range(width):
            data[x][y] = line_source[x][y]

    return data

def mix_pixel_random(width, height, data_img1, data_img2):
    data = [[0] * height for _ in range(width)]

    for y in range(height):
        for x in range(width):
            data[x][y] = random.choice([data_img1[x][y], data_img2[x][y]])

    return data

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('python mix.py img1 img2')
        sys.exit(1)
    img1 = Image.open(sys.argv[1])
    img2 = Image.open(sys.argv[2])
    width1, height1, data_img1 = get_image_data(img1)
    width2, height2, data_img2 = get_image_data(img2)
    if not width1 == width2 or not height1 == height2:
        print('Image have different sizes.')
        sys.exit(2)
    output_data = mix_pixel_random(width1, height1, data_img1, data_img2)
    output_name = ''.join(sys.argv[1].split('.')[:-1]) + '_' + \
                  ''.join(sys.argv[2].split('.')[:-1]) + '_pixel_random.png'
    save_data(width1, height1, output_data, output_name)
