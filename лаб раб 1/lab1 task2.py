# TODO Найдите количество книг, которое можно разместить на дискете
bit = 1.44*1024*1024
pages = 100
lines = 50
symbols = 25
amount = int(bit//(lines*symbols*pages*4))
print("Количество книг, помещающихся на дискету:", amount)
