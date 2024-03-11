import os
import shutil

if not os.path.exists('structured_valid'):
    os.makedirs('structured_valid')

if not os.path.exists('structured_test'):
    os.makedirs('structured_test')

for class_folder in os.listdir('structured_train'):
    print(f"Processing {class_folder}...")

    valid_class_folder = os.path.join('structured_valid', class_folder)
    if not os.path.exists(valid_class_folder):
        os.makedirs(valid_class_folder)

    test_class_folder = os.path.join('structured_test', class_folder)
    if not os.path.exists(test_class_folder):
        os.makedirs(test_class_folder)

    train_class_folder = os.path.join('structured_train', class_folder)

    images = os.listdir(train_class_folder)

    # Move N% of images to the given set
    num_valid_images = int(len(images) * 0.15)
    valid_images = images[:num_valid_images]
    for img in valid_images:
        src = os.path.join(train_class_folder, img)
        dst = os.path.join(valid_class_folder, img)
        shutil.move(src, dst)
        print(f"Moved {src} to {dst}")

print("Done!")

