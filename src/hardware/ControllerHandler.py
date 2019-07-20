import evdev
from evdev import InputDevice
import aiostream
import logging


class ControllerHandler:

    def __init__(self):
        logging.info("Devices found: {0}".format(evdev.list_devices()))
        self.__gamepads = list(map(InputDevice, evdev.list_devices()))

    @property
    def gamepads(self):
        return self.__gamepads

    @property
    def count(self):
        return len(self.__gamepads)

    async def global_generator(self):
        loops = [gamepad.async_read_loop() for gamepad in self.__gamepads]
        async with aiostream.stream.merge(*loops).stream() as merged:
            async for event in merged:
                yield event
