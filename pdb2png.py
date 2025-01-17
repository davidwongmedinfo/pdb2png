import os
import pymol
from pymol import cmd

# Set the input and output directories
input_dir = 'D:\pytest'  # Directory containing .pdb files
output_dir = 'D:\pytest_out'    # Directory for saving images
if not os.path.exists(output_dir):
    os.makedirs(output_dir) # Ensure the output directory exists
	
# Iterate through all .pdb files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.pdb'):
        # Construct the full path to the file
        filepath = os.path.join(input_dir, filename)

        # Load the PDB file (protein structure in PDB format)
        cmd.load(filepath, filename[:-4])  # Use the filename without the .pdb extension as the object name
		
		# (Optional) Execute PyMOL commands to adjust the view or coloring, etc.
        cmd.orient()  # Automatically adjust the viewing angle
        # cmd.show_as('cartoon')  # Display in cartoon style
		
		# Render and save the image
        output_filename = os.path.join(output_dir, filename[:-4] + '.png')
        cmd.ray(width=1200, height=900)  # Set the dimensions of the rendered image
        cmd.png(output_filename)  # Save the rendered image

        # (Optional) Delete the loaded object in PyMOL to conserve memory
        cmd.delete(filename[:-4])

print('All images have been saved to:', output_dir)