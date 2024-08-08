import os

def rename_vrcw_files(folder_path):
    # Iterate through all files in the specified folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.vrcw'):
            # Split the filename based on the underscores
            parts = filename.split('_')
            
            # Check if the filename has the expected format
            if len(parts) >= 3:
                # Construct the new filename
                new_filename = f"{parts[0]}_{parts[1]}.{filename.split('.')[-1]}"
                
                # Full paths for renaming
                old_file = os.path.join(folder_path, filename)
                new_file = os.path.join(folder_path, new_filename)
                
                # Rename the file
                os.rename(old_file, new_file)
                print(f"Renamed: {filename} -> {new_filename}")

# Example usage
folder_path = 'torename'
rename_vrcw_files(folder_path)