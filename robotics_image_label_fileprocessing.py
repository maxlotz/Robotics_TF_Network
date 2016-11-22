import os
import shutil

loc = "Image_Training/rgb/"

with open('robotics_labels.txt', 'a') as the_file:
	for num in range(100):

		blue_cube = loc + "blue_cube/" + "blue_cube" + str(num+1) + ".jpg" + " " + str(0) + "\n"
		blue_triangle = loc + "blue_triangle/" + "blue_triangle" + str(num+1) + ".jpg" + " " + str(1) + "\n"
		green_cube = loc + "green_cube/" + "green_cube" + str(num+1) + ".jpg" + " " + str(2) + "\n"
		light_green_cylinder = loc + "light_green_cylinder/" + "light_green_cylinder" + str(num+1) + ".jpg" + " " + str(3) + "\n"
		patric = loc + "patric/" + "patric" + str(num+1) + ".jpg" + " " + str(4) + "\n"
		purple_cross = loc + "purple_cross/" + "purple_cross" +  str(num+1) + ".jpg" + " " + str(5) + "\n"
		purple_star = loc + "purple_star/" + "purple_star" +  str(num+1) + ".jpg" + " " + str(6) + "\n"
		red_cube = loc + "red_cube/" + "red_cube" + str(num+1) + ".jpg" + " " + str(7) + "\n"
		red_hollow_cube = loc + "red_hollow_cube/" + "red_hollow_cube" + str(num+1) + ".jpg" + " " + str(8) + "\n"
		red_sphere = loc + "red_sphere/" + "red_sphere" + str(num+1) + ".jpg" + " " + str(9) + "\n"
		yellow_cube = loc + "yellow_cube/" + "yellow_cube" + str(num+1) + ".jpg" + " " + str(10) + "\n"
		yellow_sphere = loc + "yellow_sphere/" + "yellow_sphere" +str(num+1) + ".jpg" + " " + str(11) + "\n"

		the_file.write(blue_cube)
		the_file.write(blue_triangle)
		the_file.write(green_cube)
		the_file.write(light_green_cylinder)
		the_file.write(patric)
		the_file.write(purple_cross)
		the_file.write(purple_star)
		the_file.write(red_cube)
		the_file.write(red_hollow_cube)
		the_file.write(red_sphere)
		the_file.write(yellow_cube)
		the_file.write(yellow_sphere)