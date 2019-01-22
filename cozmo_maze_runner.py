# import the cozmo and image libraries
import cozmo

# import libraries for movement
from cozmo.util import degrees, distance_mm, speed_mmps


def move_in_circle(robot: cozmo.robot.Robot, speed, seconds):
    robot.say_text("I will spin in three circles").wait_for_completed()
    # the first value is the speed for one of the treads, and the second value
    # is the speed for the other tread (left? right?).  They can both be
    # the same sign, or have opposite signs.  the last value is the duration of the
    # movement (measured in seconds?)
    robot.drive_wheels(speed, -1 * speed, None, None, seconds)


def turn_right(robot: cozmo.robot.Robot):
    robot.turn_in_place(degrees(-90)).wait_for_completed()


def turn_left(robot: cozmo.robot.Robot):
    robot.turn_in_place(degrees(90)).wait_for_completed()


def read_maze(file_name: str):
    maze = []
    maze_file = open(file_name, 'r', encoding='utf-8')

    # Convert to a list of command strings
    maze_text = maze_file.read().splitlines()

    # Split individual movement and rotation commands out into a tuple
    for command in maze_text:
        command_pair = tuple(command.split(','))
        maze.append(command_pair)

    maze_file.close()
    return maze


def run_maze(robot: cozmo.robot.Robot):
    maze = read_maze('maze.txt')

    # Unpack the movement and direction tuples and run each command
    for movement, direction in maze:
        move_cozmo(robot, int(movement), int(direction))


def move_cozmo(robot: cozmo.robot.Robot, movement, direction):
    if direction < 0:
        turn_right(robot)
    elif direction > 0:
        turn_left(robot)

    if movement > 0:
        robot.drive_straight(distance_mm(movement), speed_mmps(200)).wait_for_completed()


cozmo.run_program(run_maze, use_viewer=False, force_viewer_on_top=False)
