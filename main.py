import sys
from os.path import isfile, join
from os import path, listdir

def main(name):
    print(f"JMÉNO: \t{name}")
    count = 0
    for file in files_in_input_folder:
        fs = open(file, mode="r")
        try:
            if name in fs.read():
                print("\tANO", file)
                count += 1
            else: print("\tNE", file)
        except UnicodeDecodeError:
            print(f"Nemohu přečíst soubor: {file}")
        fs.close()
    print(f"> Zúčastnil se {str(count)} hodin.")

    return f"jmeno: {name} \t| \tucast: {str(count)} hodin\n"

if __name__ == "__main__":
    files_in_input_folder = []
    input_folder = ".\\input\\"
    t = listdir(input_folder)
    if path.exists(input_folder):
        files_in_input_folder = [join(input_folder, f) for f in listdir(input_folder) if isfile(join(input_folder, f)) and not f == input_folder+"main.py"]
    if len(files_in_input_folder) > 0:
        if len(sys.argv) > 1:
            main(sys.argv[1])
        elif path.exists("jmena.txt"):
            fs = open(".\\jmena.txt", mode="r")
            results = []
            names = [name for name in fs.read().splitlines() if len(name) > 0]
            for name in names:
                results.append(main(name))
            print("\n\n############### Výsledky ##########")
            for result in results:
                print(result)
            fs = open("výsledky.txt", mode="w")
            fs.writelines(results)

        else: 
            print("!Nebylo zadáno žádné jméno a neexistuje soubor jmena.txt!")
            print("příklad: python main.py [jméno]")
    else:
        print("Nejsou žádné soubory ve složce .\\input\\")