import os

def rename_files(directory, replaceString, replaceto):
    for filename in os.listdir(directory):
        if replaceString in filename:
            # Extract the desired part of the filename
            new_filename = filename.replace(replaceString, replaceto).strip()
            
            # Construct the full file paths
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)
            
            # Rename the file
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_filename}")

# Specify the directory path where the files are located
directory_path = input("input directory_path: ")
ReplaceString = input("things to replace: ")
replaceto = input("Replace them to: ")
# Call the function to rename the files
rename_files(directory_path, ReplaceString, replaceto)
