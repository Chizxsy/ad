import asyncio
import websockets

async def handler(websocket, path):
    try:
        data = await websocket.recv()
        reply = f"Data received as: {data}!"
        await websocket.send(reply)
    except websockets.exceptions.ConnectionClosedError:
        print("Client disconnected.")
    except Exception as e:
        print(f"An error occurred: {e}")

async def main():  # Wrap server start in a main function
    async with websockets.serve(handler, "localhost", 8000): # use async with to ensure proper cleanup
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())