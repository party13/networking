import re


def to_bit(number):
    """ returns binary representatation of a decimal number
    in octet format """
    if number in range (256):
        binary = bin(number)[2::]
        return '0'*(8-len(binary)) + binary

    return '-1'

def to_decimal(binary):
    """ returns decimal representation of the string binary  with 0 and 1 only
    and not longer than 8 symbols"""
    if len( re.findall('[0-1]+', binary)[0] )< 9:
        return int('0b'+binary, 2)
    return -1

def addr_to_bin(address):
    """returns binary representation of an IP-address from string address"""
    bin_address = ''
    if re.findall('\d', address)[0].isdigit():
        octet = address.split('.')
        for oct in octet:
            bin_address+=to_bit(int(oct))

    return bin_address

def addr_to_decimal(bin_address):
    """returns decimal representation of binary 32 long bin_address"""
    if len(bin_address) == 32:
        if re.match('[0-1]+', bin_address):
            return (str(to_decimal(bin_address[0:8])) + '.'
                    + str(to_decimal(bin_address[8:16])) + '.'
                    + str(to_decimal(bin_address[16:24])) + '.'
                    + str(to_decimal(bin_address[24:32])))
    return '-1'


def subnetMask(length):
    """returns an IP-subnet mask with lngth"""
    if length < 32:
        binarySubnet = '1' * length + '0' * (32 - length)
        return addr_to_decimal(binarySubnet)

    return '-1'


def nodes_quantity(length):
    if length <32:
        return 2**(32-length) - 2


def net_address(ip_address, subnet_address):
    """receive ip address and subnetmask as string and returns
    the net addres in decimal format """

    binary_ip = addr_to_bin(ip_address)
    binary_subnet = addr_to_bin(subnet_address)
    net_addr = ''
    #print (binary_ip)
    #print (binary_subnet)

    for bit in range(32):
        if binary_subnet[bit] == '1':
            net_addr += binary_ip[bit]

        else:
            net_addr+= '0'

    #print (net_addr)
    return addr_to_decimal(net_addr)


def first_in_net(ip_address, subnet_address):
    """receive ip and subnet addresses as strings
    and returns the first addres in this net"""
    netName = net_address(ip_address, subnet_address)
    binaryNet = addr_to_bin(netName)
    #print (binaryNet)
    #print (binaryNet[:31]+'1')
    return addr_to_decimal(binaryNet[:31]+'1')

def broadcast_in_net(ip_address, subnet_address):
    netName = net_address(ip_address, subnet_address)
    binaryNet = addr_to_bin(netName)
    netLen, hostLen =  net_and_host_length(subnet_address)
    broadcast = binaryNet[0:netLen] + '1'*hostLen
    return addr_to_decimal(broadcast)

def last_in_net(ip_address, subnet_address):
    broadcast_addr = broadcast_in_net(ip_address, subnet_address)
    broadcast = addr_to_bin(broadcast_addr)[:31]+'0'
    return (addr_to_decimal(broadcast))

def net_and_host_length(subnet):
    """recieve subnet and
    returns net bit lenght  and host  bitlenght in tuple of two int
    subnet must be a correct subnet in 111100000 format"""
    sub = addr_to_bin(subnet)
    netLen = 0
    hostLen = 0
    for bit in sub:
        if bit=='1':
            netLen+=1
        else:
            hostLen+=1

    return (netLen, hostLen)