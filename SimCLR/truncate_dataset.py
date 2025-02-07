import os

def delete_extra_images(directory, max_images=300):
    """
    Deletes excess images in each subfolder, keeping only `max_images` images.

    Args:
        directory (str): Path to the main folder containing subfolders.
        max_images (int): Maximum number of images to keep in each subfolder.
    """
    for folder_name in os.listdir(directory):
        folder_path = os.path.join(directory, folder_name)
        
        if os.path.isdir(folder_path):
            # Get the list of files (sorted to ensure consistent deletion)
            files = sorted([file for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))])
            
            # Check if the folder contains more images than `max_images`
            if len(files) > max_images:
                num_to_delete = len(files) - max_images  # Number of images to delete
                
                # Delete the excess images
                for file in files[:num_to_delete]: 
                    file_path = os.path.join(folder_path, file)
                    os.remove(file_path)
                
                print(f"{num_to_delete} images deleted in: {folder_path} (remaining {max_images} images)")
            else:
                print(f"Folder kept as is: {folder_path} (contained {len(files)} images)")


main_directory = './data'
delete_extra_images(main_directory, max_images=300)
