from functions.run_python_file import *

def main():
    calculator_main = run_python_file("calculator", "main.py")
    calculator_eight = run_python_file("calculator", "main.py", ["3 + 5"])
    calculator_tests = run_python_file("calculator", "tests.py")
    calculator_main2 = run_python_file("calculator", "../main.py")
    calculator_non = run_python_file("calculator", "nonexistent.py")
    calculator_lorem = run_python_file("calculator", "lorem.txt")

    print (f"Result for current directory: \n{calculator_main}")
    print (f"Result for current directory: \n{calculator_eight}")
    print (f"Result for current directory: \n{calculator_tests}")
    print (f"Result for current directory: \n{calculator_main2}")
    print (f"Result for current directory: \n{calculator_non}")
    print (f"Result for current directory: \n{calculator_lorem}")
    return

if __name__ == "__main__":
    main()
