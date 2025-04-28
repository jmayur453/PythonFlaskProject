from PIL import Image, ImageFilter
import io

def edit_uploaded_image(file):
    img = Image.open(file.stream)
    img = img.resize((300, 300)).filter(ImageFilter.CONTOUR)

    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    return img_io

