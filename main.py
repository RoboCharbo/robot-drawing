"""

Press the A button to see how the robot travels from the bottom left of the grid to the top right.  Then use the Robo Drawing blocks to design a new path for your robot to follow.  Start the robot anywhere on the grid by setting the coordinates in the Reset block.

"""

def on_a_pressed():
    global n
    n = 1
    for index in range(3):
        for index2 in range(n):
            RoboDrawing.robo_move_forward()
        RoboDrawing.robo_turn(RoboDrawing.TurnDirection.LEFT)
        for index3 in range(n):
            RoboDrawing.robo_move_forward()
        RoboDrawing.robo_turn(RoboDrawing.TurnDirection.RIGHT)
        n += 1
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

n = 0
RoboDrawing.robo_reset(0, 6, RoboDrawing.Direction.RIGHT)
