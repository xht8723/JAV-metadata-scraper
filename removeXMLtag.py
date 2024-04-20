import os
import xml.etree.ElementTree as ET

# Specify the directory path (current directory in this case)
directory = input("director:")

# Iterate over all files in the directory
for filename in os.listdir(directory):
    # Check if the file has a .nfo extension
    if filename.endswith('.nfo'):
        file_path = os.path.join(directory, filename)
        
        try:
            # Parse the XML file
            tree = ET.parse(file_path)
            root = tree.getroot()
            
            # Iterate over all elements in the XML tree
            for element in root.iter():
                # Clear the text content of the element
                element.text = None
            
            # Write the modified XML back to the file
            tree.write(file_path, encoding='utf-8', xml_declaration=True)
            
            print(f'Processed: {filename}')
        except ET.ParseError:
            print(f'Skipping {filename} due to XML parsing error.')

print('Done.')
