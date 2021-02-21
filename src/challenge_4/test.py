from command  import Command

userInput = input()
userCommand = Command(userInput)
print(userCommand.instruction, userCommand.value, type(userCommand.value))