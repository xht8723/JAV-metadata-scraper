import os
import utilities as ut
""" 
# Get the target directory from user input
target_directory = input("Enter the target directory path: ")
link_directory = input("Enter the link directory path: ")
 """
def make_hl(target_directory, link_directory, widget):
# Iterate over all files in the target directory
    for filename in os.listdir(target_directory):
        # Get the full path of the file
        file_path = os.path.join(target_directory, filename)
        
        # Check if the item is a file (not a directory)
        if os.path.isfile(file_path):
            # Create the hard link path with "hardlink -" at the start of the filename
            hardlink_path = os.path.join(link_directory, "hardlink - " + filename)
            
            # Create the hard link
            os.link(file_path, hardlink_path)
            
            ut.display(widget, f"Created hard link: {hardlink_path}")