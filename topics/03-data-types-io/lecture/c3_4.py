def sizeCount(x):
    return (2**x) - 1
def sizeCountSigned(x):
    return ((2**x) // 2) - 1


if __name__ == "__main__":
    bit8 = sizeCount(8)
    bit8Sig = sizeCountSigned(8)
    print(f"8 bitov: 0 až {bit8}, {-bit8Sig} až {bit8Sig}")
    bit16 = sizeCount(16)
    bit16Sig = sizeCountSigned(16)
    print(f"16 bitov: 0 až {bit16}, {-bit16Sig} až {bit16Sig}")
    bit32 = sizeCount(32)
    bit32Sig = sizeCountSigned(32)
    print(f"32 bitov: 0 až {bit32}, {-bit32Sig} až {bit32Sig}")
    bit64 = sizeCount(64)
    bit64Sig = sizeCountSigned(64)
    print(f"64 bitov: 0 až {bit64}, {-bit64Sig} až {bit64Sig}")