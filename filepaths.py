import os

def get_filepaths(directory):
    file_paths = []

    for root, directories, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".py"):
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)
            #     pass
            # else:
            #     filepath = os.path.join(root, filename)
            #     file_paths.append(filename)

    return file_paths

# os.chdir("/home/jinal/Development/")

full_file_paths = get_filepaths("/home/jinal/Development/")

#this is to go through text files and add everything to one file

with open("/home/jinal/Development/output.txt", 'w') as outfile:
    for fname in full_file_paths:
        outfile.write('\n' + '\n' + '----------------------------------------------------------------' + '\n')
        outfile.write(fname + '\n' + '\n')
        with open(fname) as infile:
            content = infile.read()
            outfile.write(content)
        infile.close()
