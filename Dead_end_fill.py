import doctest
import time

BLOCKED = 1
EMPTY = 0

class dead_end_fill:
  def dead_end_fill(self):
    pass
  
  def is_dead_end(self, x, y, maze):
      """
      Is the square at (x, y) of the maze a dead end?
      """
      if self.maze[y][x] == BLOCKED:
          return False
      return list(nears(x, y, maze)).count(BLOCKED) in (3, 4)

  def fill_one_dead_end(self, maze):
      """
      Fills the first encountered dead end of the maze.
      """
      self.new = maze[:]
      self.found_dead_end = False
      for y in range(len(maze)):
          for x in range(len(maze[0])):
              if (not found_dead_end) and self.is_dead_end(x, y, maze):
                  found_dead_end = True
                  self.new[y][x] = BLOCKED
              else:
                  self.new[y][x] = maze[y][x]
      return self.new

  def has_at_least_one_dead_end(self, maze):
      """
      Does the maze have at least one dead end?
      """
      for y in range(len(maze)):
          for x in range(len(maze[0])):
              if self.is_dead_end(x, y, maze):
                  return True
      return False