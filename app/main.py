import sys
import os

supported_commands = ["exit", "echo", "type"]

def command_lookup_in_path(command, path):
    for root, dirs, files in os.walk(path):
        if command in files:
            return os.path.join(root, command)

def type_command(args):
    if len(args) == 0:
        print("type: too few arguments")
    elif len(args) > 1:
        print("type: too many arguments")
    elif args[0] in supported_commands:
        print(f"{args[0]} is a shell builtin")
    elif os.environ["PATH"]:
        paths = os.environ["PATH"].split(":")
        location = False
        for path in paths:
            location = command_lookup_in_path(args[0], path)
            if location:
                print(f"{args[0]} is {location}")
                break
        
        if not location:
            print(f"{args[0]}: not found")
            
    else:
        print(f"{args[0]}: not found")

def exit_command(args):
    code = 0
    if len(args) > 1:
        print("exit: too many arguments")
    elif len(args) == 1 and not args[0].isnumeric():
        print("exit: argument must be a number")
    elif len(args) == 1:
        code = int(args[0])
    sys.exit(code)

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
            exit_command(args)
        elif (command == "echo"):
            print(" ".join(args))
        elif (command == "type"):
            type_command(args)
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
