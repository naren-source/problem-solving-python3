def dec_bin(dec: int) -> int:
    bin = 0
    pwr = 1
    while int(dec/2) != 0 :
        r = dec % 2
        bin +=
        dec = int(dec / 2)
    return int(bin)


print(dec_bin(int(input())))