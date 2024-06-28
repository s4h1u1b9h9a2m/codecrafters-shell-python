import sys

supported_commands = ["exit", "echo", "type"]
def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        exp = input()

        if exp.strip() == "":
            sys.exit(0)

        exp_arr = exp.split()

        command = exp_arr[0]
        args = exp_arr[1:]

        if (command == "exit"):
            code = 0
            if len(args) > 1:
                print("exit: too many arguments")
            elif len(args) == 1 and not args[0].isnumeric():
                print("exit: argument must be a number")
            elif len(args) == 1:
                code = int(args[0])
            sys.exit(code)
        elif (command == "echo"):
            print(" ".join(args))
        elif (command == "type"):
            if len(args) == 0:
                print("type: too few arguments")
            elif len(args) > 1:
                print("type: too many arguments")
            elif args[0] in supported_commands:
                print(f"{args[0]} is a shell builtin")
            else:
                print(f"{args[0]}: not found")
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
