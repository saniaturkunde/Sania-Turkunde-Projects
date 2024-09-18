from PIL import Image
import os

# Path to the directory containing multi-band TIFF images
input_dir = 'D:/Palak/MIT/Semester 6/Mini Project/CNN model/blood cancer dataset'

# Path to the directory where converted JPEG images will be saved
output_dir = 'D:/Palak/MIT/Semester 6/Mini Project/CNN model/Preprocessed dataset'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# List all files in the input directory
files = os.listdir(input_dir)

# Iterate through each file in the input directory
for filename in files:
    if filename.endswith('.tiff') or filename.endswith('.tif'):
        # Open the multi-band TIFF image
        with Image.open(os.path.join(input_dir, filename)) as img:
            # Convert the image to RGB mode (remove extra bands)
            img_rgb = img.convert('RGB')
            
            # Construct the output file path (replace ".tiff" with ".jpg")
            output_filename = os.path.splitext(filename)[0] + '.jpg'
            output_path = os.path.join(output_dir, output_filename)
            
            # Save the converted image as JPEG
            img_rgb.save(output_path, 'JPEG')
            print(f"Converted {filename} to JPEG format.")
