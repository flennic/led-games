from enum import Enum, auto


class ControllerKeyCode(Enum):
    A = auto()
    B = auto()
    X = auto()
    Y = auto()
    SELECT = auto()
    START = auto()
    L = auto()
    R = auto()
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()
    UP_DOWN = auto()
    LEFT_RIGHT = auto()


class ControllerKeyDirection(Enum):
    PRESS = auto()
    RELEASE = auto()


class ControllerEvent:

    controller_key_code = None
    controller_key_direction = None
    controller_id = None

    def __init__(self, event):
        self.event = event['event']
        self.controller_id = event['gamepad_id']
        self.__assign_code_and_direction()

    def __str__(self):
        return self.__to_string__()

    def __repr__(self):
        return self.__to_string__()

    def __to_string__(self):

        time = self.event.sec

        try:
            code = self.controller_key_code.name
            direction = self.controller_key_direction.name
        except AttributeError:
            return "Unidentifiable event at {0}.".format(time)

        return "Gamepad {0}: Button {1} was {2}ED at {3}.".format(self.controller_id, code, direction, time)

    def __assign_code_and_direction(self):

        if self.event.type == 0:
            return
        # A
        if self.event.code == 289:
            self.controller_key_code = ControllerKeyCode.A
            if self.event.value == 1:
                self.controller_key_direction = ControllerKeyDirection.PRESS
            elif self.event.value == 0:
                self.controller_key_direction = ControllerKeyDirection.RELEASE

        # B
        if self.event.code == 290:
            self.controller_key_code = ControllerKeyCode.B
            if self.event.value == 1:
                self.controller_key_direction = ControllerKeyDirection.PRESS
            elif self.event.value == 0:
                self.controller_key_direction = ControllerKeyDirection.RELEASE

        # X
        if self.event.code == 288:
            self.controller_key_code = ControllerKeyCode.X
            if self.event.value == 1:
                self.controller_key_direction = ControllerKeyDirection.PRESS
            elif self.event.value == 0:
                self.controller_key_direction = ControllerKeyDirection.RELEASE

        # Y
        if self.event.code == 291:
            self.controller_key_code = ControllerKeyCode.Y
            if self.event.value == 1:
                self.controller_key_direction = ControllerKeyDirection.PRESS
            elif self.event.value == 0:
                self.controller_key_direction = ControllerKeyDirection.RELEASE

        # SELECT
        if self.event.code == 296:
            self.controller_key_code = ControllerKeyCode.SELECT
            if self.event.value == 1:
                self.controller_key_direction = ControllerKeyDirection.PRESS
            elif self.event.value == 0:
                self.controller_key_direction = ControllerKeyDirection.RELEASE

        # START
        if self.event.code == 297:
            self.controller_key_code = ControllerKeyCode.START
            if self.event.value == 1:
                self.controller_key_direction = ControllerKeyDirection.PRESS
            elif self.event.value == 0:
                self.controller_key_direction = ControllerKeyDirection.RELEASE

        # L
        if self.event.code == 292:
            self.controller_key_code = ControllerKeyCode.L
            if self.event.value == 1:
                self.controller_key_direction = ControllerKeyDirection.PRESS
            elif self.event.value == 0:
                self.controller_key_direction = ControllerKeyDirection.RELEASE

        # R
        if self.event.code == 294:
            self.controller_key_code = ControllerKeyCode.R
            if self.event.value == 1:
                self.controller_key_direction = ControllerKeyDirection.PRESS
            elif self.event.value == 0:
                self.controller_key_direction = ControllerKeyDirection.RELEASE

        # UP_DOWN
        if self.event.code == 1:
            if self.event.value == 0:
                self.controller_key_code = ControllerKeyCode.UP
                self.controller_key_direction = ControllerKeyDirection.PRESS
            elif self.event.value == 255:
                self.controller_key_code = ControllerKeyCode.DOWN
                self.controller_key_direction = ControllerKeyDirection.PRESS
            elif self.event.value == 127:
                self.controller_key_code = ControllerKeyCode.UP_DOWN
                self.controller_key_direction = ControllerKeyDirection.RELEASE

        # LEFT_RIGHT
        if self.event.code == 0:
            if self.event.value == 0:
                self.controller_key_code = ControllerKeyCode.LEFT
                self.controller_key_direction = ControllerKeyDirection.PRESS
            elif self.event.value == 255:
                self.controller_key_code = ControllerKeyCode.RIGHT
                self.controller_key_direction = ControllerKeyDirection.PRESS
            elif self.event.value == 127:
                self.controller_key_code = ControllerKeyCode.LEFT_RIGHT
                self.controller_key_direction = ControllerKeyDirection.RELEASE
