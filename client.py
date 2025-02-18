import asyncio
import websockets

async def chat():
    try:
        async with websockets.connect('ws://localhost:5000') as websocket:
            while True:
                message = input("Ping Adell? (Y/n): ")
                await websocket.send(message)
                response = await websocket.recv()
                print(f"Received: {response}")
    except websockets.exceptions.ConnectionClosedError:
        print("Connection to server closed.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(chat())