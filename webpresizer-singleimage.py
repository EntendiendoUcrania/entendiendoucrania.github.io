import os
import subprocess
from PIL import Image

# Specify the input WebP image file name
input_image = "images/crimenes/osievsky_1/img1.webp"  # Replace with the name of your input WebP image

# Create the output image name by appending ".webp" to the input image name
output_image = os.path.splitext(input_image)[0] + "_resized.webp"

# Function to resize a WebP image and overwrite the original
def resize_webp_image(input_image):
    # Specify the new width for resizing
    new_width = 400  # Replace with the desired width in pixels

    # Use the dwebp command to decode the input WebP image
    dwebp_executable = r"C:\Program Files\libwebp-1.3.2-windows-x64\bin\dwebp.exe"
    subprocess.run([dwebp_executable, input_image, "-o", "temp.png"])

    # Use Pillow to open the image and get its dimensions
    with Image.open("temp.png") as img:
        original_width, original_height = img.size

    # Calculate the new height proportionally
    new_height = int(new_width * original_height / original_width)

    # Use the cwebp command to resize and encode the image to WebP with the specified width and calculated height
    cwebp_executable = r"C:\Program Files\libwebp-1.3.2-windows-x64\bin\cwebp.exe"
    subprocess.run([cwebp_executable, "temp.png", "-resize", str(new_width), str(new_height), "-o", output_image])

    # Remove the temporary decoded image
    os.remove("temp.png")

    print(f"Resized and replaced: {input_image}")
    print(f"New Height: {new_height}")

# Run the resizing function
resize_webp_image(input_image)