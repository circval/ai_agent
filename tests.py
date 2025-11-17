from functions.write_file import *

def main():
    calculator_lorem = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    calculator_morelorem = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    calculator_temp = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    #calculator_dni = get_file_content("calculator", "pkg/does_not_exist.py")

    print (f"Result for current directory: \n{calculator_lorem}")
    print (f"Result for current directory: \n{calculator_morelorem}")
    print (f"Result for current directory: \n{calculator_temp}")
    #print (f"Result for current directory: \n{calculator_dni}")
    return

if __name__ == "__main__":
    main()
