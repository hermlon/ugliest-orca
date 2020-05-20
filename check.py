def costas_array(p, g):
    for i in range(p):
        print(hex(g**i % p))
