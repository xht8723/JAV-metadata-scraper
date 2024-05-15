<<<<<<< HEAD
import os
import utilities as ut

def rename_files(directory, replaceString, replaceto, widget):
    for filename in os.listdir(directory):
        if replaceString in filename:
            # Extract the desired part of the filename
            new_filename = filename.replace(replaceString, replaceto).strip()
            
            # Construct the full file paths
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)
            
            # Rename the file
            os.rename(old_path, new_path)
            ut.display(widget, f"Renamed: {filename} -> {new_filename}")
=======
import os
import utilities as ut

def rename_files(directory, replaceString, replaceto, widget):
    for filename in os.listdir(directory):
        if replaceString in filename:
            # Extract the desired part of the filename
            new_filename = filename.replace(replaceString, replaceto).strip()
            
            # Construct the full file paths
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)
            
            # Rename the file
            os.rename(old_path, new_path)
            ut.display(widget, f"Renamed: {filename} -> {new_filename}")
>>>>>>> bug
    return