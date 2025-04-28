from PIL import Image

ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

def image_to_ascii(image_file, width=100):
    image = Image.open(image_file).convert('L')
    aspect_ratio = image.height / image.width
    new_height = int(aspect_ratio * width * 0.55)
    resized_image = image.resize((width, new_height))

    pixels = resized_image.getdata()
    ascii_str = ''.join(ASCII_CHARS[pixel // 25] for pixel in pixels)

    ascii_img = "\n".join(
        ascii_str[i:i + width] for i in range(0, len(ascii_str), width)
    )
    return ascii_img
