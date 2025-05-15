#!/usr/bin/python3
"""
0. UTF-8 Validation
"""


def validUTF8(data):
    '''
    Determines if a given data set represents a valid UTF-8 encoding.
    '''
    num_bytes = 0

    for byte in data:
        # Mask to get the 8 least significant bits (1 byte)
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            elif (byte >> 7):
                return False  # Invalid leading byte
        else:
            # Check if this is a valid continuation byte (10xxxxxx)
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0
