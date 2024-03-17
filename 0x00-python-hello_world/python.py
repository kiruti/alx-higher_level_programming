import os 

#get the name of the current python file 
current_file_name = __file__

#Set the environment varuable with the file name
os.environ['PYFILENO'] = current_file_name


print("Python file name saved to environment variable: ", os.environ['PYFILENO'])
