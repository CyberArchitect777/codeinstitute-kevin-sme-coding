import os
import random
import time

grid = [[' '] * 10] * 10
direction = "right"
snake_head_position = [0, 0]
snake_positions = []
fruit_position = [5, 5]
length = 1


def clear_terminal():
  os.system('cls' if os.name == 'nt' else 'clear')


def get_direction():
  if snake_head_position[0] < fruit_position[0]:
    return "down"
  elif snake_head_position[0] > fruit_position[0]:
    return "up"
  elif snake_head_position[1] < fruit_position[1]:
    return "right"
  else:
    return "left"


def get_new_position():
  desired_direction = get_direction()
  direction_to_position_change = {
      "down": [1, 0],
      "up": [-1, 0],
      "right": [0, 1],
      "left": [0, -1]
  }
  return direction_to_position_change[desired_direction]


def move_fruit():
  x = random.randrange(0, 10)
  y = random.randrange(0, 10)
  return [x, y]


def check_fruit_collision():
  return snake_head_position == fruit_position


while True:

  snake_positions.insert(0, snake_head_position[:])
  to_draw = snake_positions[0:length]

  clear_terminal()
  if check_fruit_collision():
    length += 1
    fruit_position = move_fruit()

  new_position = get_new_position()
  snake_head_position[0] += new_position[0]
  snake_head_position[1] += new_position[1]

  if snake_head_position in to_draw:
    print("Snake bit himself and died!")
    break

  for i, x in enumerate(grid):
    for j, y in enumerate(x):
      if [i, j] in to_draw:
        print("■", end="")
      elif [i, j] == fruit_position:
        print("*", end="")
      else:
        print("-", end="")
    print("\n", end="")
  time.sleep(1)
