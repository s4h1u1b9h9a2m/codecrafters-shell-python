import sys
import os

supported_commands = ["exit", "echo", "type", "pwd"]

def command_lookup_in_path(command):
    if os.environ["PATH"]:
        paths = os.environ["PATH"].split(":")
        for path in paths:
            if os.path.isfile(os.path.join(path, command)):
                return os.path.join(path, command)
    return False

def type_command(args):
    if len(args) == 0:
        print("type: too few arguments")
    elif len(args) > 1:
        print("type: too many arguments")
    elif args[0] in supported_commands:
        print(f"{args[0]} is a shell builtin")
    elif os.environ["PATH"]:
        location = command_lookup_in_path(args[0])
        if location:
            print(f"{args[0]} is {location}")
        else:
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

def exec_command(command, args):
    os.system(f"{command} {' '.join(args)}")

def pwd_command():
    print(os.getcwd())

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
        elif (command == "pwd"):
            pwd_command()
        else:
            location = command_lookup_in_path(command)
            if location:
                exec_command(location, args)
            else:
                print(f"{command}: command not found")


if __name__ == "__main__":
    main()
