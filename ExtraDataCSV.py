import os
import shutil
import csv

# Set root directory and target directory
root_dir = 'data/extra'
target_dir = 'data/all_images'

# Create the target directory if it doesn't exist
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# Create an empty list to store image IDs and dog breed information
data = []

# Iterate over all subdirectories in the root directory
for breed_dir in os.listdir(root_dir):
    full_breed_dir = os.path.join(root_dir, breed_dir)

    # Check if it is a directory
    if os.path.isdir(full_breed_dir):
        # Extract the dog breed name (directory name is in the format n02085620-Chihuahua)
        breed_name = breed_dir.split('-')[-1].lower()

        # Iterate over all image files in the dog breed directory
        for image_file in os.listdir(full_breed_dir):
            if image_file.endswith('.jpg'):
                # Extract the image ID (filename without extension)
                image_id = os.path.splitext(image_file)[0]

                # Copy the image file to the target directory
                source_path = os.path.join(full_breed_dir, image_file)
                target_path = os.path.join(target_dir, image_file)
                shutil.copy2(source_path, target_path)

                # Add the image ID and dog breed name to the data list
                data.append([image_id, breed_name])

# Specify the output path for the CSV file
output_csv = 'dog_breeds.csv'

# Write the data to a CSV file
with open(output_csv, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)

    # Write the header
    csvwriter.writerow(['id', 'breed'])

    # Write the image ID and dog breed data
    csvwriter.writerows(data)

print(f"All images have been copied to: {target_dir}")
print(f"CSV file has been saved to: {output_csv}")