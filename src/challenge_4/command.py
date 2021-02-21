class Command :
    def __init__(self, command: str):
        splitted = command.split(" ", 1)
        self.instruction = splitted[0]
        self.value = int(splitted[1])
    



            
            
            