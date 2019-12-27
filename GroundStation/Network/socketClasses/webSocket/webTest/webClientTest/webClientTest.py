import asyncio
import logging

import websockets


async def hello(websocket, path):
    logging.info('Waiting for data')
    data = await websocket.recv()

    logging.info('Received data from {}'.format(path))
    return data


Server = websockets.serve(hello, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(Server)
asyncio.get_event_loop().run_forever()
