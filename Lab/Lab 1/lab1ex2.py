
#open the file
earthquake_file = open("earthquake.txt", "r")

#create the new file
earthquake_fmt_file = open("earthquakefmt.txt", "w")

#create a dictionary to save the data
earthquake_dict={}

#read the file and store the data in the dictionary
for line in earthquake_file:
    line_list = line.split()
    if line_list[-1] not in earthquake_dict:
        earthquake_dict[line_list[-1]] = [[line_list[1], line_list[0]]]
    else:
        earthquake_dict[line_list[-1]].append([line_list[1], line_list[0]])

# #write the data to the file
for region in earthquake_dict:
    earthquake_fmt_file.write(str([region, earthquake_dict[region]]))
    earthquake_fmt_file.write("\n")

#close the files
earthquake_file.close()
earthquake_fmt_file.close()
