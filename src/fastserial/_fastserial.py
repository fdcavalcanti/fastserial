import serial.tools.list_ports

class FastSerial:
    def __init__(self):
        self.ports_available = []
        self.port_selection = None

    def get_ports_available(self) -> list:
        """Reads the available serial ports on the system."""
        port_list = serial.tools.list_ports.comports()
        if not port_list:
            print("No ports available")
        return port_list
    
    def get_serial_port_names(self) -> list:
        """Extracts the port name from the available ports.
            On Windows, returns COMX or /dev/ttyX on Unix.
        """
        ports = self.get_ports_available()
        port_names = [port.name for port in ports]
        return port_names

    def select_serial_port_index(self, index: int) -> None:
        """Select the active serial port by index."""
        self.ports_available = self.get_serial_port_names()
        try:
            self.port_selection = self.ports_available[index]
        except IndexError:
            print("Port not available")


a = FastSerial()
b = a.get_serial_port_names()
print(b)
a.select_serial_port_index(3)
