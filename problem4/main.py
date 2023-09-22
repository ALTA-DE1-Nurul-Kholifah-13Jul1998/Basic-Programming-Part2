'''
Input Harga: 370000
Input Diskon: 15
Output: harga yang harus dibayar adalah Rp. 314.500
'''

harga_awal = int(input("Masukkan Harga Barang : "))
diskon = int(input("Diskon Barang : "))

harga_diskon = (diskon/100)*harga_awal
harga_akhir = harga_awal - harga_diskon

print("Harga barang : " + str(harga_awal))
print("Potongan diskon : " + str(harga_diskon))
print("Total pembayaran : " + str(harga_akhir))