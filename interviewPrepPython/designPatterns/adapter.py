class UsbCable:
    def __init__(self):
        self.isPlugged = False


    def PlugUsb(self):
        self.isPlugged = True


class UsbPort:
    def __init__(self):
        self.portAvailable = True

    
    def plug(self, usb):
        if self.portAvailable:
            usb.plugUsb()
            self.portAvailable = False


usbCable = UsbCable()
usbPort1 = UsbPort()
usbPort1.plug(usbCable)

class MicroUsbCable:
    def __init__(self):
        self.isPlugged = False


    def plugMicroUsb(self):
        self.isPlugged = True

class MicroToUsbAdapter(UsbCable):
    def __init__(self, microUsbCable):
        self.microUsbCable = microUsbCable
        self.microUsbCable.plugMicroUsb()


microTousbAdapter = MicroToUsbAdapter(MicroUsbCable())
usbPort2 = UsbPort()
usbPort2.plug(microTousbAdapter)