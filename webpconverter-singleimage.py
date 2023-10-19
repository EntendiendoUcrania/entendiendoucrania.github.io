import os
import subprocess

# Specify the input image file name
input_image = "input_image.png"  # Replace with the name of your input image

# Create the output image name by appending ".webp" to the input image name
output_image = os.path.splitext(input_image)[0] + ".webp"

# Function to convert a single image to WebP
def convert_image_to_webp(input_image, output_image):
    # Use the cwebp command to convert the input image to WebP
    subprocess.run(["cwebp", input_image, "-resize", "400", "0", "-o", output_image])

    print(f"Converted: {input_image} -> {output_image}")

# Run the conversion function
convert_image_to_webp(input_image, output_image)
