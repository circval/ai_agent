from functions.get_files_info import get_files_info

def main():
    calculator_current = get_files_info("calculator", ".")
    calculator_pkg = get_files_info("calculator", "pkg")
    calculator_bin = get_files_info("calculator", "/bin")
    calculator_prev = get_files_info("calculator", "../")

    print (f"Result for current directory: \n{calculator_current}")
    print (f"Result for 'pkg' directory: \n{calculator_pkg}")
    print (f"Result for '/bin' directory: \n{calculator_bin}")
    print (f"Result for '../' directory: \n{calculator_prev}")
    return

if __name__ == "__main__":
    main()
