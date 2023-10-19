import os
import subprocess

# Set the folder path where your images are located
folder_path = "path/to/your/folder"

# Function to convert images to WebP
def convert_images_to_webp(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
            input_image = os.path.join(folder_path, filename)
            output_image = os.path.join(folder_path, os.path.splitext(filename)[0] + ".webp")

            # Use the cwebp command to convert the image
            subprocess.run(["cwebp", input_image, "-resize", "400", "0", "-o", output_image])

            print(f"Converted: {input_image} -> {output_image}")

# Run the conversion function
convert_images_to_webp(folder_path)
