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

    ControllerKeyCode = None
    ControllerKeyDirection = None

    def __init__(self, event):
        self.event = event
        self.__assign_code_and_direction()

    def __str__(self):
        return self.__to_string__()

    def __repr__(self):
        return self.__to_string__()

    def __to_string__(self):

        time = self.event.sec

        try:
            code = self.ControllerKeyCode.name
            direction = self.ControllerKeyDirection.name
        except AttributeError:
            return "Unidentifiable event at {0}.".format(time)

        return "Button {0} was {1}ED at {2}.".format(code, direction, time)

    def __assign_code_and_direction(self):

        # A
        if self.event.code == 289:
            self.ControllerKeyCode = ControllerKeyCode.A
            if self.event.value == 1:
                self.ControllerKeyDirection = ControllerKeyDirection.PRESS
            elif self.event.value == 0:
                self.ControllerKeyDirection = ControllerKeyDirection.RELEASE

        # B
        if self.event.code == 290:
            self.ControllerKeyCode = ControllerKeyCode.B
            if self.event.value == 1:
                self.ControllerKeyDirection = ControllerKeyDirection.PRESS
            elif self.event.value == 0:
                self.ControllerKeyDirection = ControllerKeyDirection.RELEASE

        # X
        if self.event.code == 288:
            self.ControllerKeyCode = ControllerKeyCode.X
            if self.event.value == 1:
                self.ControllerKeyDirection = ControllerKeyDirection.PRESS
            elif self.event.value == 0:
                self.ControllerKeyDirection = ControllerKeyDirection.RELEASE

        # Y
        if self.event.code == 291:
            self.ControllerKeyCode = ControllerKeyCode.Y
            if self.event.value == 1:
                self.ControllerKeyDirection = ControllerKeyDirection.PRESS
            elif self.event.value == 0:
                self.ControllerKeyDirection = ControllerKeyDirection.RELEASE

        # SELECT
        if self.event.code == 296:
            self.ControllerKeyCode = ControllerKeyCode.SELECT
            if self.event.value == 1:
                self.ControllerKeyDirection = ControllerKeyDirection.PRESS
            elif self.event.value == 0:
                self.ControllerKeyDirection = ControllerKeyDirection.RELEASE

        # START
        if self.event.code == 297:
            self.ControllerKeyCode = ControllerKeyCode.START
            if self.event.value == 1:
                self.ControllerKeyDirection = ControllerKeyDirection.PRESS
            elif self.event.value == 0:
                self.ControllerKeyDirection = ControllerKeyDirection.RELEASE

        # L
        if self.event.code == 292:
            self.ControllerKeyCode = ControllerKeyCode.L
            if self.event.value == 1:
                self.ControllerKeyDirection = ControllerKeyDirection.PRESS
            elif self.event.value == 0:
                self.ControllerKeyDirection = ControllerKeyDirection.RELEASE

        # R
        if self.event.code == 294:
            self.ControllerKeyCode = ControllerKeyCode.R
            if self.event.value == 1:
                self.ControllerKeyDirection = ControllerKeyDirection.PRESS
            elif self.event.value == 0:
                self.ControllerKeyDirection = ControllerKeyDirection.RELEASE

        # UP_DOWN
        if self.event.code == 1:
            if self.event.value == 0:
                self.ControllerKeyCode = ControllerKeyCode.UP
                self.ControllerKeyDirection = ControllerKeyDirection.PRESS
            elif self.event.value == 255:
                self.ControllerKeyCode = ControllerKeyCode.DOWN
                self.ControllerKeyDirection = ControllerKeyDirection.PRESS
            elif self.event.value == 127:
                self.ControllerKeyCode = ControllerKeyCode.UP_DOWN
                self.ControllerKeyDirection = ControllerKeyDirection.RELEASE

        # LEFT_RIGHT
        if self.event.code == 0:
            if self.event.value == 0:
                self.ControllerKeyCode = ControllerKeyCode.LEFT
                self.ControllerKeyDirection = ControllerKeyDirection.PRESS
            elif self.event.value == 255:
                self.ControllerKeyCode = ControllerKeyCode.RIGHT
                self.ControllerKeyDirection = ControllerKeyDirection.PRESS
            elif self.event.value == 127:
                self.ControllerKeyCode = ControllerKeyCode.LEFT_RIGHT
                self.ControllerKeyDirection = ControllerKeyDirection.RELEASE
