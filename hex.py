#!/usr/bin/env python3

import re
import sys

# Escape sequences for common control characters
ESCAPE_SEQUENCES = {
    0x00: r"\0",
    0x07: r"\a",
    0x08: r"\b",
    0x09: r"\t",
    0x0A: r"\n",
    0x0B: r"\v",
    0x0C: r"\f",
    0x0D: r"\r",
    0x1B: r"\x1b",  # ESC
    0x7F: r"\d",  # DEL
}


def hexdump_to_ascii(hexdump):
    """
    Convert a hex dump string into ASCII text.
    """

    # Extract all hex byte pairs
    hex_bytes = re.findall(r'\b[0-9a-fA-F]{2}\b', hexdump)

    output = []

    for byte in hex_bytes:
        value = int(byte, 16)

        # Printable ASCII
        if 32 <= value <= 126:
            output.append(chr(value))

        # Known escaped control chars
        elif value in ESCAPE_SEQUENCES:
            output.append(ESCAPE_SEQUENCES[value])

        # Other non-printable bytes
        else:
            output.append(f"\\x{value:02x}")

    return "".join(output)


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} '<hexdump>'")
        sys.exit(1)

    # Hexdump passed directly as command-line argument
    hexdump = sys.argv[1]

    result = hexdump_to_ascii(hexdump)

    print(result)
