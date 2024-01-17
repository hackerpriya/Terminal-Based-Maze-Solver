from collections import deque
import random
from colorama import init, Fore

init(autoreset=True)

# Maze Generation Function
def generate_maze(n):
    maze = [['◌' for _ in range(n)] for _ in range(n)]
    maze[0][0] = Fore.GREEN + 'S'  # Start
    maze[n - 1][n - 1] = Fore.BLUE + 'E'  # End

    # Mark a certain percentage of cells as walls
    num_walls = int(0.25 * n * n)
    for _ in range(num_walls):
        while True:
            row, col = random.randint(0, n - 1), random.randint(0, n - 1)
            if maze[row][col] != 'S' and maze[row][col] != 'E' and maze[row][col] != Fore.RED + '▓':
                maze[row][col] = Fore.RED + '▓'
                break

    return maze

# Maze Printing Function
def print_maze(maze):
    for row in maze:
        print(' '.join(row))
    print()

# Pathfinding Function (Using BFS)
def find_path(maze):
    start = (0, 0)
    end = (len(maze) - 1, len(maze[0]) - 1)

    queue = deque([(start, [])])
    visited = set()

    while queue:
        current, path = queue.popleft()
        if current == end:
            return path + [current]

        if current in visited:
            continue

        visited.add(current)

        row, col = current
        neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]

        valid_neighbors = [(r, c) for r, c in neighbors if 0 <= r < len(maze) and 0 <= c < len(maze[0]) and maze[r][c] != Fore.RED + '▓' and (r, c) not in visited]

        for neighbor in valid_neighbors:
            queue.append((neighbor, path + [current]))

    return None

# Path Printing Function
def print_path(path, maze):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if (row, col) == path[0]:
                print(Fore.GREEN + 'S', end=" ")
            elif (row, col) == path[-1]:
                print(Fore.BLUE + 'E', end=" ")
            elif (row, col) in path:
                if row != 0 or col != 0:
                    print(Fore.RED + 'X', end=" ")
            elif maze[row][col] == Fore.RED + '▓':
                print(Fore.RED + '▓', end=" ")
            else:
                print(Fore.BLUE + '◌', end=" ")
        print()


# Path Marking Function
def mark_path(maze, path):
    for row, col in path:
        maze[row][col] = Fore.GREEN + 'X'

# Clearing Path Markings Function
def clear_path(maze):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == Fore.GREEN + 'X':
                maze[row][col] = '◌'

# Main Function
def main():
    n = int(input("Enter the size of the maze (n * n): "))
    maze = generate_maze(n)
    print("Generated Maze:")

    while True:
        print_maze(maze)

        option = input("1. Print Path\n2. Generate Another Puzzle\n3. Exit\nEnter you choice (1/2/3):")

        if option == '1':
            path = find_path(maze)
            if path:
                print_path(path, maze)
                mark_path(maze, path)
        elif option == '2':
            clear_path(maze)
            maze = generate_maze(n)
        elif option == '3':
            print("Exiting the game.")
            break
        else:
            print(Fore.RED + "Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
