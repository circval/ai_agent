from functions.get_file_content import get_file_content

def main():
    calculator_main = get_file_content("calculator", "main.py")
    calculator_calc = get_file_content("calculator", "pkg/calculator.py")
    calculator_bin = get_file_content("calculator", "/bin/cat")
    calculator_dni = get_file_content("calculator", "pkg/does_not_exist.py")

    print (f"Result for current directory: \n{calculator_main}")
    print (f"Result for current directory: \n{calculator_calc}")
    print (f"Result for current directory: \n{calculator_bin}")
    print (f"Result for current directory: \n{calculator_dni}")
    return

if __name__ == "__main__":
    main()
