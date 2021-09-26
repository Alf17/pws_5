import usb.core
import usb.backend.libusb1

print('[START]')
busses = usb.busses()
# print(f'busses: {busses}')
for bus in busses:
    # print(f'bus: {bus}')
    devices = bus.devices
    # print(f'devices: {devices}')
    for dev in devices:
        # print(f'dev: {dev}')
        if dev != None:
            try:
                xdev = usb.core.find(idVendor=dev.idVendor, idProduct=dev.idProduct)
                print("********************************************")
                print(f'xdev: {xdev}')
                if xdev._manufacturer is None:
                    xdev._manufacturer = usb.util.get_string(xdev, xdev.iManufacturer)
                if xdev._product is None:
                    xdev._product = usb.util.get_string(xdev, xdev.iProduct)
                # stx = '%6d %6d: '+str(xdev._manufacturer).strip()+' = '+str(xdev._product).strip()
                # print(stx) % (dev.idVendor,dev.idProduct)
                # print(f"manufacturer: {xdev._manufacturer} / product: {xdev._product}")
                # print(f"manufacturer: {xdev.idVendor} / product: {xdev.idProduct}")

            except:
                pass