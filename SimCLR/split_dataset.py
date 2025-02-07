import os
import shutil
import random

def split_data_into_train_val_test(data_dir, output_dir, train_ratio=0.7, test_ratio=0.2, val_ratio=0.1):
    """
    Splits the data from a source folder into training, validation, and test sets
    while keeping the original data intact.

    Args:
        data_dir (str): Path to the source folder containing subfolders by class.
        output_dir (str): Path to the target folder where `train`, `val`, and `test` will be created.
        train_ratio (float): Ratio of data for training
        test_ratio (float): Ratio of data for testing
        val_ratio (float): Ratio of data for validation
    """
    total_ratio = train_ratio + test_ratio + val_ratio
    if not abs(total_ratio - 1.0) < 1e-6:
        raise ValueError("The train, test, and val ratios must sum up to 1.0.")

    # Create the `train`, `val`, and `test` directories in the output folder
    train_dir = os.path.join(output_dir, 'train')
    val_dir = os.path.join(output_dir, 'val')
    test_dir = os.path.join(output_dir, 'test')

    for dir_path in [train_dir, val_dir, test_dir]:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    # Iterate through subfolders (classes)
    for class_name in os.listdir(data_dir):
        class_path = os.path.join(data_dir, class_name)
        if os.path.isdir(class_path): 
            # List files in the class folder
            files = os.listdir(class_path)
            if len(files) == 0:
                print(f"Class '{class_name}': No files found, nothing to move.")
                continue

            # Shuffle the files to ensure random selection
            random.shuffle(files)

            # Calculate the indices for each split
            num_total = len(files)
            num_train = int(num_total * train_ratio)
            num_test = int(num_total * test_ratio)

            train_files = files[:num_train]
            test_files = files[num_train:num_train + num_test]
            val_files = files[num_train + num_test:]

            # Create subdirectories for each class
            target_train_class_path = os.path.join(train_dir, class_name)
            target_val_class_path = os.path.join(val_dir, class_name)
            target_test_class_path = os.path.join(test_dir, class_name)

            for target_path in [target_train_class_path, target_val_class_path, target_test_class_path]:
                if not os.path.exists(target_path):
                    os.makedirs(target_path)

            # Copy the files to the corresponding directories
            for file_name in train_files:
                src_file = os.path.join(class_path, file_name)
                dest_file = os.path.join(target_train_class_path, file_name)
                shutil.copy(src_file, dest_file)

            for file_name in val_files:
                src_file = os.path.join(class_path, file_name)
                dest_file = os.path.join(target_val_class_path, file_name)
                shutil.copy(src_file, dest_file)

            for file_name in test_files:
                src_file = os.path.join(class_path, file_name)
                dest_file = os.path.join(target_test_class_path, file_name)
                shutil.copy(src_file, dest_file)

            print(f"Class '{class_name}':")
            print(f"  {len(train_files)} images copied to {target_train_class_path}")
            print(f"  {len(val_files)} images copied to {target_val_class_path}")
            print(f"  {len(test_files)} images copied to {target_test_class_path}")

data_directory = './data' 
output_directory = './'  

split_data_into_train_val_test(data_directory, output_directory, train_ratio=0.7, test_ratio=0.2, val_ratio=0.1)
