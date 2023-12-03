a = 5
a = a * 2
print(a)

a = 5
a = a + a
print(a)

a = 5
a = a << 1
print(a)

"""
     or    and   xor    not
     или    и  или или  не
ab | a|b | a&b | a^b |  !a
---------------------------------
00 |  0  |  0  |  0  |   1
01 |  1  |  0  |  1  |
10 |  1  |  0  |  1  |   0
11 |  1  |  1  |  0  |

1100 | 1010 = 1110
1100 & 1010 = 1000
1100 ^ 1010 = 0110

print(1100 | 1010) -> 2046
print(1100 & 1010) -> 64
print(1100 ^ 1010) -> 1982

1100_10 = 10001001100_2
1010_10 = 01111110010_2
   |    = 11111111110_2 = 2046_10
   &    = 00001000000_2 = 64_10
   ^    = 11110111110_2 = 1982_10
"""

# link to bitboard https://gekomad.github.io/Cinnamon/BitboardCalculator/

def get_king_bitboard_moves(start_pos):
    """
    | K<<7 | K<<8 | K<<9 |
    | K>>1 |   K  | K<<1 |
    | K>>9 | K>>8 | K>>7 |
    """

    K = 1 << start_pos
    noA = 0xfefefefefefefefe
    noH = 0x7f7f7f7f7f7f7f7f
    no8 = 0xffffffffffffff
    Ka = K & noA
    Kh = K & noH
    K8 = K & no8
    mask = ((Ka & K8) << 7) | (K8 << 8) |  ((Kh & K8) << 9) | \
           (Ka >> 1)      |              (Kh << 1) | \
           (Ka >> 9)      | (K >> 8)  |  (Kh >> 7)

    return mask

valid_positions = get_king_bitboard_moves(56)
print(valid_positions)

def popcnt(mask):
    """
    Count number of unit bits in mask
    00101100110 -> 5

    shift mask one bit to the right and increment cnt if it is 1
    00101100110 >> 1 -> 0010110011

    complexity is O(len(mask))
    """

    cnt = 0
    while (mask > 0):
        if mask & 1 == 1:
            cnt += 1
        mask = mask >> 1
    return cnt

def popcnt2(mask):
    """
     00101100110  -1
     00101100101   &
     ---------------
     00101100100  -1
     00101100011   &
     ---------------
     00101100000  ...

     ---------------
     00000000000

     complexity is O(# of ones)
    """
    cnt = 0
    while (mask > 0):
        cnt += 1
        mask &= mask - 1
    return cnt

bits = []
def fillbits():
    for b in range(256):
        bits.append(popcnt2(b))

def popcnt3(mask):
    """
    bits is a table with correct answers
    bits = [
        00000000 -> 0
        00000001 -> 1
        00000010 -> 1
        00000011 -> 2
        ...
        11111111 -> 8
    ]
    every time take the first 8 bits (mask & 255; 255 is lowest row in bitboard) and look up its correct answer it bits list
    then shift to the right by 1 row
    """
    cnt = 0
    while (mask > 0):
        cnt += bits[mask & 255]
        mask >>= 8

    return cnt

fillbits()
print(popcnt(14374908612776943380))
print(popcnt2(14374908612776943380))
print(popcnt3(14374908612776943380))