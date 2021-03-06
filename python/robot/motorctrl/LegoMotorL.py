"""
Represents a lego L motor 88003  and allows remote and
local control using MotorController or RemoteMotorController
"""


class LegoMotorL:
    min_motor_speed = 30

    def __init__(self, motor_controller):
        self.motor_controller = motor_controller
        motor_controller.stop()

    def update(self, direction, speed):
        if speed < LegoMotorL.min_motor_speed:
            speed = LegoMotorL.min_motor_speed
        self.motor_controller.update(direction, speed)

    def drive(self, speed):
        if speed == 0:
            self.update('R', 0)
        elif speed < 0:
            self.update('B', abs(speed))
        elif speed > 0:
            self.update('F', speed)

    def stop(self):
        self.motor_controller.stop()