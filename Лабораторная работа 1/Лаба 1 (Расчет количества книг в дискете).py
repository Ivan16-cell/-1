
volume_mb = 1.44

pages = 100
strings = 50
symbols = 25

byt = 4 * symbols * strings * pages

kbyt = byt / 1024

mbyt = kbyt / 1024

print("Количество книг, помещающихся на дискету:", int(volume_mb // mbyt))
