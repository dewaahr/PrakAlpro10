# buah={"nama":["apel","sawo","jeruk"],"harga":[3000,2000,4000]}

# for buah, harga in zip(buah["nama"],buah["harga"]):
#     print(f"{buah} : {harga}")

# a=[1,2,3,4,5,6,7,8,9,10]
# while len(a)!=1:
#     for i in a:
#         if a.index(i)%2==0:
#             a.remove(i)
# print(a)




# data_nota={"toko":"Toko Buku Aku",
#            "pembeli":"Dewa",
#            "nama barang":["Pensil 2B","Buku",'Penghapus','Penggaris'],
#            'harga': [3500,2500,1000,1000]
# }

# belanja=[2,1,3,2]

# print(f'Nama TOKO:{data_nota["toko"]}')
# print(f'Nama Pembeli:{data_nota["pembeli"]}')
# totalharga=0
# i=0
# for barang in data_nota['nama barang']:
#     print(barang,':',belanja[i],"Buah  |  Total Harga:",(data_nota["harga"][i])*belanja[i])
#     totalharga=totalharga+(data_nota["harga"][i])*belanja[i]
#     i=i+1
# print(totalharga)
# print('jumlah barang:',sum(belanja))
# print('Harga setelah diskon:',totalharga-totalharga*0.2)




angka={"genap":[],"ganjil":[]}

while True:
    angka_input=int(input('Masukan angka (negatif untuk berhenti): '))
    if angka_input<0:
        print(angka)
        break
    if angka_input%2==0:
        angka["genap"].append(angka_input)
    else: angka["ganjil"].append(angka_input)

print(angka)
