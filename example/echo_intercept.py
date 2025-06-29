import random
import string
import pydivert

PORT = 12345
filter_Str = f"tcp.DstPort == {PORT} or tcp.SrcPort == {PORT}"

generate_random_string = lambda length: bytes(
    "".join(random.choices(string.ascii_letters + string.digits, k=length)), "utf-8"
)

with pydivert.WinDivert(filter_Str) as w:
    for packet in w:
        if packet.payload:
            if packet.dst_port == PORT:
                packet.payload = generate_random_string(len(packet.payload))
                packet.recalculate_checksums()
        w.send(packet)