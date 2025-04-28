from PIL import Image, ImageDraw, ImageFont
import os

def generate_handwriting_image(text, font_file='handwriting.ttf', max_width=750):
    try:
        # Get the absolute path for saving the image
        save_dir = os.path.join(os.path.dirname(__file__), 'static', 'images')
        os.makedirs(save_dir, exist_ok=True)  # Create the directory if it doesn't exist

        font_path = os.path.join('app', 'static', 'fonts', font_file)

        if not os.path.exists(font_path):
            raise FileNotFoundError(f"Font '{font_file}' not found at {font_path}.")

        # Try different font sizes to fit the text within the max_width
        font_size = 28
        font = ImageFont.truetype(font_path, font_size)

        # Split the input text into multiple lines
        lines = wrap_text(text, font, max_width)

        # Dynamically adjust image height based on the number of lines
        line_height = font.getbbox('A')[3] - font.getbbox('A')[1]  # Calculate line height using font bounding box
        image_height = 60 + len(lines) * (line_height + 10)  # Adjust for line height
        image = Image.new('RGB', (max_width, image_height), color=(255, 255, 255))
        draw = ImageDraw.Draw(image)

        # Draw the wrapped text on the image
        y = 40
        for line in lines:
            draw.text((20, y), line, font=font, fill=(0, 0, 0))
            y += line_height + 10  # Move to the next line

        output_path = os.path.join(save_dir, "handwriting_image.png")
        image.save(output_path)
        return output_path

    except Exception as e:
        raise Exception(f"Error generating handwriting: {str(e)}")


def wrap_text(text, font, max_width):
    """
    Wraps text so that it fits within the max_width of the image.
    """
    lines = []
    words = text.split()

    current_line = ""
    for word in words:
        # Check the width of the current line with the new word
        test_line = current_line + " " + word if current_line else word
        width, _ = font.getbbox(test_line)[2:]  # Get width of the line using getbbox()

        if width <= max_width:
            # If the line is within the width, add the word
            current_line = test_line
        else:
            # If the line exceeds the max width, add the current line to the lines list and start a new line
            lines.append(current_line)
            current_line = word  # Start a new line with the current word

    # Add the last line if any
    if current_line:
        lines.append(current_line)

    return lines
