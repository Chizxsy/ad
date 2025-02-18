import asyncio
import websockets


async def handler(websocket):
    while True:
        try:
            message = await websocket.recv()
            print(f"Received: {message}")

            if message == "button_clicked":
                print("Button clicked!")
    


        except websockets.exceptions.ConnectionClosedError:
            print("Client disconnected.")
            break
        except Exception as e:
            print(f"Error: {e}")
            break

async def main():
    async with websockets.serve(handler, "192.168.1.235", 22): # Use 0.0.0.0 to listen on all interfaces
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Server stopped.")