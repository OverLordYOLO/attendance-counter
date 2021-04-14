import sys
from os.path import isfile, join
from os import path, listdir

def get_results(name, input_files):
    print(f"JMÉNO: \t{name}")
    count = 0
    partial_results = []
    for file in input_files:
        file_contents = read_file_contents(file)
        if name in file_contents:
            partial_results.append(f"ANO\t{file}")
            count += 1
        else: partial_results.append(f"NE\t{file}")

    return {
        "total": f"jmeno: {name} \t| \tucast: {str(count)} hodin",
        "partial": partial_results
    }

def read_file_contents(file_name):
    fs = open(file_name, mode="r")
    try: contents = fs.read()
    except UnicodeDecodeError: print(f"Nemohu přečíst soubor: {file_name}")
    fs.close()
    return contents

def get_names():
    names = []
    if len(sys.argv) > 1:
        names.append(sys.argv[1])
    elif path.exists("jmena.txt"):
        fs = open(".\\jmena.txt", mode="r")
        names = [name for name in fs.read().splitlines() if len(name) > 0]
    else: 
        print("!Nebylo zadáno žádné jméno a neexistuje soubor jmena.txt!")
        print("příklad: python main.py [jméno]")
    return names

def get_input_files():
    files_in_input_folder = []
    input_folder = ".\\input\\"
    if path.exists(input_folder):
        files_in_input_folder = [join(input_folder, f) for f in listdir(input_folder) if isfile(join(input_folder, f)) and not f == input_folder+"main.py"]
    return files_in_input_folder

def save_results(results):
    fs = open("výsledky.txt", mode="w")
    for result in results: fs.write(result["result"]["total"] + "\n")
    fs.close()

def print_results(results):
    print("\n\n############### Výsledky ##########")
    for result in results:
        print("\n>>", result["name"])
        for partial in result["result"]["partial"]:
            print(partial)
    print("\n-------- TOTAL --------")
    for result in results:
        print(result["result"]["total"])

def main():
    input_files = get_input_files()
    if len(input_files) > 0:
        names = get_names()
        results = [{"name": name, "result": get_results(name, input_files)} for name in names]
        
        print_results(results)
        
        save_results(results)

    else:
        print("Nejsou žádné soubory ve složce .\\input\\")

if __name__ == "__main__":
    main()