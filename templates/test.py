from PIL import Image, ImageDraw, ImageFont

def generate_image():
    # Image settings
    width, height = 800, 600
    background_color = (0, 0, 0)  # RGB for black

    # Text settings
    text = "Levi's Binary Ballet: 01011001 01101111 01110101 01110010 00100000 01100011 01101111 01100100 01100101 01110011 00101100 00100000 01111001 01101111 01110101 01110010 00100000 01100011 01110010 01100101 01100001 01110100 01101001 01110110 01101001 01110100 01111001"
    text_color = (255, 255, 255)  # RGB for white

    # Create a new image with a dark background
    img = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(img)

    # Use a suitable font (adjust the path if needed)
    font = ImageFont.load_default()

    # Calculate text size and position
    text_width, text_height = draw.textsize(text, font)
    x = (width - text_width) // 2
    y = (height - text_height) // 2

    # Add the text to the image
    draw.text((x, y), text, font=font, fill=text_color)

    # Save the image
    img.save("LevisBinaryBallet.png")

if __name__ == "__main__":
    generate_image()
