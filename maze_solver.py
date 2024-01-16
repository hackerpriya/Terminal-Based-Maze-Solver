import random
from colorama import init, Fore

init(autoreset=True)

# Maze Generation Function
def generate_maze(n):
    maze = [[random.choice(['◌', '▓']) for _ in range(n)] for _ in range(n)]
    maze[0][0] = Fore.GREEN + 'S'  # Start
    maze[n - 1][n - 1] = Fore.BLUE + 'E'  # End

    # Mark a certain percentage of cells as walls
    num_walls = int(0.25 * n * n)
    for _ in range(num_walls):
        row, col = random.randint(0, n - 1), random.randint(0, n - 1)
        maze[row][col] = Fore.RED + '▓'

    return maze

# Maze Printing Function
def print_maze(maze):
    for row in maze:
        print(' '.join(row))
    print()

# Pathfinding Function (Using BFS)
def find_path(maze):
    # Implementation of BFS algorithm to find a path
    pass

# Path Printing Function
def print_path(path):
    # Print the path in a readable format
    pass

# Path Marking Function
def mark_path(maze, path):
    pass

# Main Function
def main():
    n = int(input("Enter the size of the maze (n * n): "))
    maze = generate_maze(n)

    while True:
        print_maze(maze)

        option = input("Choose an option:\n1. Print Path\n2. Generate Another Puzzle\n3. Exit\n")

        if option == '1':
            path = find_path(maze)
            if path:
                print_path(path)
                mark_path(maze, path)
            else:
                print(Fore.RED + "No path found.")
        elif option == '2':
            maze = generate_maze(n)
        elif option == '3':
            print("Exiting the game.")
            break
        else:
            print(Fore.RED + "Invalid option. Please choose again.")

if __name__ == "__main__":
    main()