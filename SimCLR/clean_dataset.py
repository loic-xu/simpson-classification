import os
import shutil

def delete_small_folders(directory, min_images=100):
    """
    Deletes folders containing fewer than a certain number of images.
    
    Args:
        directory (str): Path to the main folder containing the subfolders.
        min_images (int): Minimum number of images required to keep a folder.
    """
    for folder_name in os.listdir(directory):
        folder_path = os.path.join(directory, folder_name)
        
        if os.path.isdir(folder_path):
            # Count the number of files in the folder
            num_files = len([file for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))])
            
            # Delete the folder if it contains fewer than `min_images` files
            if num_files < min_images:
                shutil.rmtree(folder_path)
                print(f"Deleted folder: {folder_path} (contained {num_files} images)")
            else:
                print(f"Kept folder: {folder_path} (contained {num_files} images)")


main_directory = './data'  
delete_small_folders(main_directory, min_images=287)
