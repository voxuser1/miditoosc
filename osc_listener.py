from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer

def print_message(address, *args):
    """
    Callback function that processes incoming OSC messages.
    """
    print(f"Received OSC message: {address} with arguments {args}")

def main():
    # Port to listen on
    ip = "0.0.0.0"  # Listens on all available interfaces
    port = 1234     # Port to monitor

    # Set up the dispatcher to handle messages
    dispatcher = Dispatcher()
    dispatcher.set_default_handler(print_message)  # Default callback for all OSC addresses

    # Start the OSC server
    print(f"Listening for OSC messages on {ip}:{port}")
    server = BlockingOSCUDPServer((ip, port), dispatcher)

    try:
        server.serve_forever()  # The server blocks and waits for incoming messages
    except KeyboardInterrupt:
        print("\nServer stopped.")

if __name__ == "__main__":
    main()
