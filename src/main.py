from src.hardware.ControllerHandler import ControllerHandler
from src.hardware.EventHandler import EventHandler
import asyncio
import logging


async def main():
    controller_handler = ControllerHandler()
    global_generator = controller_handler.global_generator()
    event_handler = EventHandler()
    global_generator_filtered = event_handler.filter_known(global_generator)

    async for event in global_generator_filtered:
        print(event)

logging.basicConfig(level=logging.INFO)

loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(main())
except KeyboardInterrupt:
    logging.info("Shutting down...")
finally:
    loop.run_until_complete(loop.shutdown_asyncgens())
    loop.close()
