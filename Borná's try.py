def maze_repr(maze):
  """
  Prints a nice textual represenatation of a maze.
  '*' indicates a wall, ' ' a corridor.
  """
  string_maze = ""
  for y in range(len(maze)):
    for x in range(len(maze[0])):
      string_maze += "*" if maze[y][x] else ' '
    string_maze += "\n"
  return string_maze[:-1]
