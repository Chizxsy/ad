import asyncio
import websockets

async def client():
    uri = "ws://192.168.1.235:22"  # Replace with your Pi's IP and port

    try:
        async with websockets.connect(uri) as websocket:
            print("Connected to WebSocket server")

            while True:  # Keep the connection open to send multiple messages
                message = input("Enter message (or 'q' to quit): ")
                if message.lower() == 'q':
                    break

                await websocket.send(message)
                print(f"Sent: {message}")

                try:  # Handle potential receive errors
                    response = await websocket.recv()
                    print(f"Received: {response}")
                except websockets.exceptions.ConnectionClosedOK:
                    print("Server closed the connection.")
                    break
                except Exception as e:
                    print(f"Error receiving: {e}")
                    break

    except websockets.exceptions.ConnectionRefusedError:
        print(f"Connection refused. Make sure the server is running at {uri}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(client())