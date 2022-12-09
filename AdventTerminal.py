import os
from glob import glob

#-> =======| Graphics |=======
main_logo = """
╭━━━╮╱╭╮╱╱╱╱╱╱╱╱╭╮╭━━━╮╭━┳━━━╮╱╱╱╱╭╮╱╱╭━━━┳━━━╮
┃╭━╮┃╱┃┃╱╱╱╱╱╱╱╭╯╰┫╭━╮┃┃╭┫╭━╮┃╱╱╱╱┃┃╱╱┃╭━╮┃╭━╮┃
┃┃╱┃┣━╯┣╮╭┳━━┳━╋╮╭┫┃╱┃┣╯╰┫┃╱╰╋━━┳━╯┣━━╋╯╭╯┣╯╭╯┃
┃╰━╯┃╭╮┃╰╯┃┃━┫╭╮┫┃┃┃╱┃┣╮╭┫┃╱╭┫╭╮┃╭╮┃┃━╋━╯╭╋━╯╭╯
┃╭━╮┃╰╯┣╮╭┫┃━┫┃┃┃╰┫╰━╯┃┃┃┃╰━╯┃╰╯┃╰╯┃┃━┫┃╰━┫┃╰━╮
╰╯╱╰┻━━╯╰╯╰━━┻╯╰┻━┻━━━╯╰╯╰━━━┻━━┻━━┻━━┻━━━┻━━━╯"""

separator = "---------------------------------------------"

#-> =======| Functions |=======
def main():
    os.system('cls')
    print(main_logo)
    print(separator)

    path, days = list_day_folders(os.path.dirname(__file__))

    print("Select day:")
    print(separator)

    for num in range(len(days)):
        print("   " + days[num] + " [{}]".format(num+1))
    print(separator)
    
    print("My selection: ")
    selected_number = input()

    os.system('cls')
    print(main_logo)
    print(separator)

    file_names, files = list_script_files(path, selected_number, days)
    
    print("Select day:")
    print(separator)

    for num in range(len(file_names)):
        print("   " + file_names[num] + " [{}]".format(num+1))
    print(separator)
    
    print("My selection: ")
    selected_number = input()

    run_script(files[int(selected_number)-1])

def list_day_folders(path):
    path_list = path + "/*/"
    folders = glob(path_list, recursive=True)
    days = list()
    for folder in folders:
        sub_path = folder.split("\\")
        days.append(sub_path[-2])
    return path, days

def list_script_files(origin_path, selected_number, days):
    selected_folder = origin_path + "/" + str(days[int(selected_number)-1]) + "/*.py"
    files = glob(selected_folder, recursive=True)
    file_names = list()
    for file in files:
        file_names.append(file.split("\\")[-1])
    return file_names, files

def run_script(file_path):
    os.system("cls")
    os.system("python " + file_path)


#-> =======| Execuded code |=======
main()