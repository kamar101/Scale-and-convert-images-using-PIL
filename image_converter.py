from PIL import Image
import os

# Enter Current and New file locations
image_folder = "~/images/"
new_save_location = "/opt/icons/" 

#Creates a list of images in the folder
image_files = os.listdir(image_folder)


# Iterate through images in the folder 
for image in image_files:
	if not image.startswith('.'): 					#filter out hidden files
		fileName, ext = os.path.splitext(image) 	#split the filename and extension of the images
		with Image.open(os.path.join(image_folder,image)) as im:
			im.resize((128,128)).rotate(270).convert('RGB').save(new_save_location+ fileName+".JPEG")