from src.command_parser import CommandParser
from src.spaceship import Spaceship

def main():
    start_position = (0, 0, 0)
    start_direction = "N"
    commands = input("Enter commands: ")
    
    parsed_commands = CommandParser.parse_commands(commands) 

    spaceship = Spaceship()
    for command in parsed_commands:
        spaceship.execute_command(command)
    
    final_position = spaceship.get_position()
    final_direction = spaceship.get_direction()
    
    print("Starting Position:", start_position)
    print("Initial Direction:", start_direction)
    print("Final Position:", final_position)
    print("Final Direction:", final_direction)

if __name__ == "__main__":
    main()
