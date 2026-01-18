# Text-Based Maze Adventure Game

maze = [
    ["S", ".", ".", "#", "."],
    ["#", "#", ".", "#", "."],
    [".", ".", ".", ".", "."],
    [".", "#", "#", "#", "."],
    [".", ".", ".", "T", "#"]
]

player_pos = [0, 0]

def print_maze():
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if [i, j] == player_pos:
                print("P", end=" ")
            else:
                print(maze[i][j], end=" ")
        print()


def move_player(direction):
    x, y = player_pos
    if direction == "w":
        x -= 1
    elif direction == "s":
        x += 1
    elif direction == "a":
        y -= 1
    elif direction == "d":
        y += 1
    else:
        print("Invalid move!")
        return False

    if x < 0 or y < 0 or x >= 5 or y >= 5:
        print("You hit the wall!")
        return False

    if maze[x][y] == "#":
        print("Blocked path!")
        return False

    player_pos[0], player_pos[1] = x, y
    return True


print("🏆 Welcome to Maze Adventure!")
print("Reach the Treasure (T)")
print("Controls: w = up, s = down, a = left, d = right\n")

while True:
    print_maze()
    move = input("\nYour move: ").lower()

    move_player(move)

    x, y = player_pos
    if maze[x][y] == "T":
        print("\n🎉 Congratulations! You found the treasure!")
        break
