import re


def to_bit(number):
    """ returns binary representation of a decimal number
    in octet format """
    if number in range(256):
        binary = bin(number)[2::]
        return '0' * (8 - len(binary)) + binary
    return '-1'


def to_decimal(binary):
    """ returns decimal representation of the string binary  with 0 and 1 only
    and not longer than 8 symbols"""
    if len(re.findall('[0-1]+', binary)[0]) < 9:
        return int('0b' + binary, 2)
    return -1


def address_to_bin(address):
    bin_address = ''
    if is_correct_address(address):
        octet_list = address.split('.')
        for octet in octet_list:
            bin_address += to_bit(int(octet))
        return bin_address


def address_to_decimal(bin_address):
    """returns decimal representation of binary 32 long bin_address"""
    if len(bin_address) == 32:
        if re.match('[0-1]+', bin_address):
            return (str(to_decimal(bin_address[0:8])) + '.'
                    + str(to_decimal(bin_address[8:16])) + '.'
                    + str(to_decimal(bin_address[16:24])) + '.'
                    + str(to_decimal(bin_address[24:32])))
    return '-1'


def is_correct_address(address):
    """
    :return: True if the current address is correct, or False if not
    """
    pattern = '\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}'
    if re.match(pattern, address):
        octet = address.split('.')
        for item in octet:
            if int(item) > 255 or int(item) < 0:
                # print ('item '+item+' incorrect')
                return False

        return True
    else:
        return False


def is_correct_subnet(subnet):
    """
    :param subnet: subnetmask
    :return: return subnet prefix , if subnet mask is correct , or
    return -1 if incorrect
    """
    if is_correct_address(subnet):
        binary = address_to_bin(subnet)
        if len(binary) == 32:
            find = binary.find('10')
            if find == binary.rfind('10'):
                return find + 1
        return -1
    return -1


def subnetMask(prefix):
    """returns an IP-subnet mask with prefix"""
    if prefix < 32:
        binarySubnet = '1' * prefix + '0' * (32 - prefix)
        return address_to_decimal(binarySubnet)

    return '-1'


class Net():
    def __init__(self, ip_address, subnet_mask):

        if is_correct_address(ip_address):
            self.ip = ip_address
            self.ip_binary = address_to_bin(ip_address)
        else:
            return 'incorrect IP adress'

        subnet = is_correct_subnet(subnet_mask)
        if subnet != -1:
            self.subnet_mask = subnet_mask
            self.subnet_mask_binary = address_to_bin(subnet_mask)
            self.host_len = 32 - subnet
            self.net_len = subnet
        else:
            return 'incorrect subnet mask'

    def net(self):
        net_name = ''
        for i in range(self.net_len):
            net_name += self.ip_binary[i]
        for i in range(self.host_len):
            net_name += '0'
        return net_name

    def broadcast(self):
        broadcast_in_net=''
        for i in range(self.net_len):
            broadcast_in_net += self.ip_binary[i]
        for i in range(self.host_len):
            broadcast_in_net += '1'
        return broadcast_in_net

    def first(self):
        net_name = self.net()
        return net_name[:31]+ '1'

    def last(self):
        broadcast = self.broadcast()
        return broadcast[:31]+'0'

    def total_nodes(self):
        host_len = 32 - is_correct_subnet(self.subnet_mask)
        return 2 ** host_len - 2

    def __repr__(self):
        net_addr = address_to_decimal(self.net())
        first = address_to_decimal(self.first())
        last = address_to_decimal(self.last())
        broadcast = address_to_decimal(self.broadcast())
        total = self.total_nodes()

        return ('Net address : {} \n'
                'subnet Mask : {} \n'
                'first address in network: {} \n'
                'last address in network : {} \n'
                'broadcast adress in network: {} \n'
                'total nodes in network: {}').format(net_addr, self.subnet_mask, first, last,
                                                     broadcast, total)


def run_test():
    ip_dictionary = ('172.12.123.234',
                     '1gr485ytkekt,y',
                     '265.345.123.123',
                     '255.255.255.240',
                     '255.240.129.123',
                     '255.255.0.0',
                     '128.0.0.0')
    for address in ip_dictionary:
        correct = is_correct_address(address)
        print ('{} is correct addres - {}'.format(address, correct))
        if correct:
            # print (address_to_bin(address))
            print('   is_correct_subnet - {}'.format(is_correct_subnet(address)))

run_test()