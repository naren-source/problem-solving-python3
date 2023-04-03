class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def disconnect(self):
        self.connected = False
        print("Disconnected")

    def __str__(self):
        return f"Device {self.name} is {self.connected_by}"


class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def print(self, pages):
        if not self.connected:
            print("Device is disconnected")
            return
        self.remaining_pages -= pages
        print(f"{pages} are getting printed")

    def __str__(self):
        return f"{super().__str__()} {self.remaining_pages} pages remaining"


printer = Printer("Printer", "USB", 200)
printer.print(50)
print(printer)
printer.disconnect()
printer.print(2)
