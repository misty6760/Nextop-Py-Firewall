import pydivert

BLOCK_IP = "192.168.0.54"

filter_str = f"ip.SrcAddr == {BLOCK_IP}"

# cnt = 0
with pydivert.WinDivert(filter_str) as w:
    for packet in w:
        # cnt = cnt + 1
        print(f"Dropped packet from {packet.src_addr}")
        # print(f"Packet count: {cnt}")