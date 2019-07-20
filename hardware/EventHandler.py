import hardware.ControllerEvent as ce


class EventHandler:

    @staticmethod
    async def filter_known(generator):

        async for event in generator:
            next_event = event
            parsed_next_event = ce.ControllerEvent(next_event)

            if parsed_next_event.ControllerKeyCode is not None:
                yield parsed_next_event
