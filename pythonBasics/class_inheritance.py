class Device:
  def __init__(self, name, connected_by):
    self.name = name
    self.connected_by = connected_by
    self.connected= True

  def __str__(self):
    # !r calls the __repr__ method of self.name so you don't need to add the quotes
    return f"Device {self.name!r} ({self.connected_by})"

  def disconnect(self):
    self.connected = False
    print("disconnected")

# printer = Device('Printer', 'USB')
# print(printer)
# printer.disconnect()

# Passed the device class into the printer class so that Printer class inherits/can use all of Devices' functions
class Printer(Device):
  def __init__(self, name, connected_by, capacity):
    # super() gets the parent class (Device), then the Devices' init function is called
    super().__init__(name, connected_by)
    self.capacity = capacity
    self.remaining_pages = capacity

  def __str__(self):
    return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

  def print(self, pages):
    if not self.connected:
      print("Your printer is not connected")
      return
    print(f'Printing {pages} pages')
    self.remaining_pages -= pages

printer = Printer("Printer", "USB", 500)
printer.print(20)

print(printer)
