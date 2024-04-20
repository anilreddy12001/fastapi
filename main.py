import websockets
import asyncio
import logging
import subprocess

# Run the other script
subprocess.run(["python", "pymongo_test_query.py"])


# Server data
PORT = 10000
print("Server listening on Port " + str(PORT))
logging.basicConfig(level=logging.INFO)
logging.info("Server listening on Port" + str(PORT))


# A set of connected ws clients
connected = set()

# The main behavior function for this server
async def echo(websocket, path):
    print("A client just connected")
    logging.info("A client just connected")
    # Store a copy of the connected client
    connected.add(websocket)
    # Handle incoming messages
    try:
        async for message in websocket:
            print("Received message from client origin: " + websocket.origin+" message: "+message)
            #logging.debug('This is a debug message')
            logging.info("Received message from client origin: " + websocket.origin+" message: "+message)
            # Send a response to all connected clients except sender
            for conn in connected:
                #if conn != websocket:
                  await conn.send(" python responds to " +websocket.origin+" with a message: "+ message)
                
    # Handle disconnecting clients 
    except websockets.exceptions.ConnectionClosed as e:
        print("A client just disconnected")
        logging.info("A client just disconnected")
    finally:
        connected.remove(websocket)

# Start the server
start_server = websockets.serve(echo, "0.0.0.0", PORT)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
