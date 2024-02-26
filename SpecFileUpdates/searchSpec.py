import os

text = input("Please enter text: ")
print(f"You have entered \"{text}\" word to search.")

#current_path = os.getcwd()
#current_path

path = 'C:/temp/des'
path


def searchText(path):
    os.chdir(path)
    files = os.listdir()
    #print(files)
    for file_name in files:
        print(file_name)

        abs_path = os.path.abspath(file_name)
        print("Absolute path of the file:", abs_path)

        if os.path.isfile(abs_path):
            with open(file_name, 'r', encoding='utf-8') as f:
                if text in f.read():
                    final_path = os.path.abspath(file_name)
                    print(text + " word found in this path " + final_path)
                else:
                    print("No match found in " + abs_path)
    pass

searchText(path)












