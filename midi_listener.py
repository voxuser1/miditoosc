import mido
from mido import MidiInput
from pythonosc import udp_client
import time

osc_client = SimpleUDPClient(OSC_IP, OSC_PORT)

def main():
    # List all available MIDI ports
    available_ports = mido.get_input_names()
    if not available_ports:
        print("No MIDI input ports available.")
        return

    print("Available MIDI ports:")
    for i, port in enumerate(available_ports):
        print(f"{i}: {port}")

    # Select a MIDI port
    port_index = 1
    if port_index < 0 or port_index >= len(available_ports):
        print("Invalid selection.")
        return

    selected_port = available_ports[port_index]
    print(f"Connected to: {selected_port}")

    # Open the MIDI port and read messages
    with mido.open_input(selected_port) as inport:
        print("Listening for MIDI messages. Press Ctrl+C to exit.")

        try:
            for message in inport:
                # Check for Program Change messages
                if message.type == 'program_change' and message.channel == 15:
                    program_number = message.program
                    print(f"Program Change received: Program {program_number}, Channel {message.channel + 1}")

                    # Send OSC message
                    osc_client.send_message(OSC_PATH, program_number)
                    print(f"OSC sent: {OSC_PATH} {program_number}")

        except KeyboardInterrupt:
            print("\nTerminated.")

if __name__ == "__main__":
    main()

# Save and close the file.
# Start the program with: python3 midi_listener.py
