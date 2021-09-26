import sys
import usb
busses = usb.busses()
for bus in busses:
  devices = bus.devices
  for dev in devices:
    print(repr(dev))
    print("Device:", dev.filename)
    print(f"  idVendor: {dev.idVendor}, {dev.idVendor}")
    print(f"  idProduct: {dev.idProduct}, {dev.idProduct}")
    print("Manufacturer:", dev.iManufacturer)
    print("Serial:", dev.iSerialNumber)
    print("Product:", dev.iProduct)