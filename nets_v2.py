import re

class Net():
    def __init__(self, ip_address, subnetMask):

        if self.is_correct_address(self, ip_address) :
            self.ip = ip_address
        else:
            return 'incorrect IP adress'
        if self.is_correct_subnet(self. subnetMask):
            self.subnetMask = subnetMask
        else:
            return 'incorrect subnet mask'



    def addr_to_decimal(self):
        pass

    def addr_to_bin(self):
        pass

    def broadcast_in_net(self):
        pass

    def first_in_net(self):
        pass

    def last_in_net(self):
        pass

    def is_correct_subnet(self, subnet):
        pass

    def is_correct_address(self, address):
        pass

    def __repr__(self):
        return ('Net address : {} \n'
                'subnet Mask : {} \n'
                'first address in network: {} \n'
                'last address in network : {} \n'
                'broadcast adress in network: {} \n'
                'total nodes in network: {}').format(self.net_addr, self.subnetMask, self.first, self.last, self.broadcast, self.total)



