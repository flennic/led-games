import evdev
from evdev import InputDevice
import aiostream
import logging


class ControllerHandler:

    def __init__(self):
        self._controller_mappings = {}
        self._next_free_id = 0
        self._gamepads = {}
        logging.info("Devices found: {0}".format(evdev.list_devices()))
        for gamepad in list(map(InputDevice, evdev.list_devices())):
            self.add_controller(gamepad)

    def add_controller(self, gamepad):
        self._gamepads[self._next_free_id] = {'gamepad_id': self._next_free_id,
                                            "gamepad": gamepad}
        self._controller_mappings[gamepad.path] = self._next_free_id
        self._next_free_id += 1

    async def __read_loop_with_controller_id(self, gamepad):
        async for event in gamepad['gamepad'].async_read_loop():
            yield{"gamepad_id": self._controller_mappings[gamepad['gamepad'].path], "event": event}

    @property
    def gamepads(self):
        return self._gamepads

    @property
    def count(self):
        return len(self._gamepads)

    @property
    def controller_mappings(self):
        return self._controller_mappings

    async def global_generator(self):
        loops = list(map(self.__read_loop_with_controller_id, self._gamepads.values()))
        async with aiostream.stream.merge(*loops).stream() as merged:
            async for gamepad_event in merged:
                yield gamepad_event
