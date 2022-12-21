from typing import Optional


def process_input(file_name):
    with open(file_name) as records:
        return records.readline().strip()


def no_repetition(stream: str) -> bool:
    return len({i: 1 for i in stream}.keys()) == len(stream)


def marker_start_index(buffer: str, marker_length: int) -> Optional[int]:
    for idx in range(marker_length, len(buffer)):
        if no_repetition(buffer[idx-marker_length:idx]):
            return idx
    return None


# Tbh I think message should come after the packet marker,
# so the code below would be preferable, but it's not a correct solution
# for part 2 challenge.
def message_start_index(buffer: str) -> Optional[int]:
    packet_marker_length, message_marker_length = 4, 14
    packet_start_idx = marker_start_index(buffer, packet_marker_length)
    packet_buffer = buffer[packet_start_idx:]
    for idx in range(message_marker_length, len(packet_buffer)):
        if no_repetition(packet_buffer[idx-message_marker_length:idx]):
            return idx
    return None


if __name__ == "__main__":
    datastream_buffer = process_input("./input.in")
    print(f"[Part 1] Chars before the first start-of-packet marker is: ", marker_start_index(datastream_buffer, 4))
    print(f"[Part 2] Chars before the first start-of-message marker is: ", marker_start_index(datastream_buffer, 14))
