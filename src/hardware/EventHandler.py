from hardware.ControllerEvent import ControllerEvent


class EventHandler:

    @staticmethod
    async def filter_known(generator):
        async for event in generator:
            next_event = event
            parsed_next_event = ControllerEvent(next_event)

            if parsed_next_event.controller_key_code is not None:
                yield parsed_next_event
