import asyncio
import websockets

async def handler(websocket, path):  # Path argument is essential
    client_address = websocket.remote_address # Get the client address
    print(f"Client connected: {client_address} at path: {path}")  # Log connection

    try:
        while True: # Keep connection open to handle multiple messages from the same client
            data = await websocket.recv()
            print(f"Received from {client_address} at {path}: {data}")  # Log received data

            reply = f"Data received as: {data}!"
            await websocket.send(reply)
            print(f"Sent to {client_address} at {path}: {reply}")  # Log sent data

    except websockets.exceptions.ConnectionClosedError:
        print(f"Client disconnected: {client_address} at {path}")
    except Exception as e:
        print(f"An error occurred: {e}")

async def main():
    async with websockets.serve(handler, "0.0.0.0", 8000):  # Use 0.0.0.0 for network access
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())