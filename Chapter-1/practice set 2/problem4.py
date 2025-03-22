import os

# It generally setting up a path 
directory_path = '/'

# Seeing  all folder on that 
entries = os.listdir(directory_path)

# Print the folder by loop
for entry in entries:
    print(entry)
