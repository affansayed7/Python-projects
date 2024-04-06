import qrcode
from PIL import Image, ImageDraw, ImageOps


data = "https://affansayed7.github.io/basic-website/"

# Generate the QR code
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code with a solid color fill
qr_image = qr.make_image(fill_color="black", back_color="white")

start_color = (173, 216, 230)  # Light blue
end_color = (25, 25, 112)  # Dark blue
gradient_direction = "horizontal"  # Change to "vertical" for vertical gradient

# Create a gradient overlay image
gradient_width, gradient_height = qr_image.size
gradient = Image.new("RGB", (gradient_width, gradient_height))
draw = ImageDraw.Draw(gradient)
if gradient_direction == "horizontal":
    for x in range(gradient_width):
        r = int(start_color[0] + (end_color[0] - start_color[0]) * x / gradient_width)
        g = int(start_color[1] + (end_color[1] - start_color[1]) * x / gradient_width)
        b = int(start_color[2] + (end_color[2] - start_color[2]) * x / gradient_width)
        draw.line([(x, 0), (x, gradient_height)], fill=(r, g, b))
else:  # Vertical gradient
    for y in range(gradient_height):
        r = int(start_color[0] + (end_color[0] - start_color[0]) * y / gradient_height)
        g = int(start_color[1] + (end_color[1] - start_color[1]) * y / gradient_height)
        b = int(start_color[2] + (end_color[2] - start_color[2]) * y / gradient_height)
        draw.line([(0, y), (gradient_width, y)], fill=(r, g, b))

# Blend the gradient overlay with the QR code image
qr_with_gradient = Image.blend(qr_image.convert("RGBA"), gradient.convert("RGBA"), alpha=0.5)


logo_path = "whitelogo.png"
logo = Image.open(logo_path)

# Resize the logo image
logo_size = (qr_with_gradient.size[0] // 4, qr_with_gradient.size[1] // 4)  # Adjust the size of the logo as needed
logo.thumbnail(logo_size, Image.ANTIALIAS)

# Calculate the position to paste the logo on the QR code (centered)
position = ((qr_with_gradient.size[0] - logo.size[0]) // 2, (qr_with_gradient.size[1] - logo.size[1]) // 2)
qr_with_gradient.paste(logo, position, logo)
qr_with_gradient.save("qr_with_gradient_and_logo.png")

