import sys


def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    exp = input()

    if exp.strip() == "":
        return

    exp_arr = exp.split()

    command = exp_arr[0]
    
    print(f"{command}: command not found")


if __name__ == "__main__":
    main()
