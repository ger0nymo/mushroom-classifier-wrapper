import json
import os
import shutil


def organize_images_by_class(coco_json_path, input_image_folder, output_base_folder):
    # Load the COCO annotations from the JSON file
    with open(coco_json_path, 'r') as f:
        coco_data = json.load(f)

    # Create output folders if they don't exist
    if not os.path.exists(output_base_folder):
        os.makedirs(output_base_folder)

    # Organize images into class-specific folders
    for image_info in coco_data['images']:
        image_id = image_info['id']

        # Find annotations for the current image
        annotations = [ann for ann in coco_data['annotations'] if ann['image_id'] == image_id]

        if annotations:
            # Use the first annotation (assuming images have a single category)
            category_id = annotations[0]['category_id']
            class_name = coco_data['categories'][category_id]['name']

            # Create class-specific folder if it doesn't exist
            class_folder = os.path.join(output_base_folder, class_name)
            if not os.path.exists(class_folder):
                os.makedirs(class_folder)

            # Copy the image to the class-specific folder
            image_filename = image_info['file_name']
            input_image_path = os.path.join(input_image_folder, image_filename)
            output_image_path = os.path.join(class_folder, image_filename)

            shutil.copy(input_image_path, output_image_path)

            print(f"Copied {input_image_path} to {output_image_path}")

    print(f"Organized {len(coco_data['images'])} images into {len(coco_data['categories'])} classes")

if __name__ == "__main__":

    folders = ["train", "test", "valid"]

    for folder in folders:
        coco_json_path = f'./{folder}/_annotations.coco.json'
        input_image_folder = f'./{folder}/'

        output_base_folder = f'./structured_{folder}/'

        organize_images_by_class(coco_json_path, input_image_folder, output_base_folder)
