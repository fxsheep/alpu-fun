ALPUM_I2C_ADDR = 0x3d

# Operation value ('sub-address') bits
OPV_ENC_ENABLE = (1 << 7)

class ALPUM:
    def __init__(self, dev):
        self.dev = dev

    def write(self, opval, data):
        return self.dev.writeto(ALPUM_I2C_ADDR, bytearray([opval]) + bytearray(data))

    def read(self, opval, length):
        self.dev.writeto(ALPUM_I2C_ADDR, bytearray([opval]))
        return self.dev.readfrom(ALPUM_I2C_ADDR, length)

    # Bypass mode, bytewise XOR with 0x01, max 8 bytes
    def bypass(self, data):
        length = len(data)
        opv = OPV_ENC_ENABLE
        self.write(opv, data)
        return self.read(opv, length)

