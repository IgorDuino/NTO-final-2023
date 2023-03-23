import asyncio
import websockets
import json

async def main():
    async with websockets.connect("ws://10.10.12.10:8080") as websocket:
        a = input()
        payload =  { "data": a.split('"')[1] }
        payload = json.dumps(payload).encode()
        await websocket.send("connected")
        res = await websocket.recv()
        await asyncio.sleep(1)
        await websocket.send(payload)
        res = await websocket.recv()

        print("\n\n\n")
        print(res)

asyncio.run(main())