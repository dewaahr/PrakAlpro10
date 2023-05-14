def hitung_karakter(data_teks):
    for baris in file_teks:
        baris=baris.lower().strip()
        for karakter in baris:
            if karakter.isalpha():
                if karakter not in data_teks:
                    data_teks[karakter]=1
                else:
                    data_teks[karakter]+=1
            elif karakter.isdigit():
                if karakter not in data_teks:
                        data_teks[karakter]=1
                else:
                        data_teks[karakter]+=1
            elif karakter.isspace():
                if 'Spasi' not in data_teks:
                    data_teks['Spasi']=1
                else:
                    data_teks['Spasi']+=1
            else:
                if 'Spesial Karakter' not in data_teks:
                    data_teks['Spesial Karakter']=1
                else:
                    data_teks['Spesial Karakter']+=1

    data_tekssort=dict(sorted(data_teks.items()))

    jenis_karakter=len(data_tekssort.keys())
    total_karakter=sum(data_tekssort.values())
    print(f'Pada Teks Terdapat {jenis_karakter} Jenis Karakter dengan total: {total_karakter} Karater')
    print('1. Karakter alfabet \n2. Karakter Numerik \n3. Spesial Karakter dan Spasi \n4. Karakter Terbanyak dan Tersedikit')
    input_user=input('Masukan Pilihan:')
    print()
    
    if input_user=='1':
        total=0
        for key in data_tekssort:
            if key!='Spesial Karakter' and key!='Spasi' and key.isalpha():
                total=total+data_tekssort[key]
                print(f"Karakter {key} : {data_tekssort[key]}")
        print(f'Total Semua Karakter Alfabet: {total}')
    elif input_user=='2':
        total=0
        for key in data_tekssort:
            if key.isdigit():
                total=total+data_tekssort[key]
                print(f"Karakter {key} : {data_tekssort[key]}")
        print(f'Total Semua Karakter Numerik: {total}')
    elif input_user=='3':
        total=0
        print('Karakter Spasi:', data_tekssort["Spasi"])
        print('Karakter Spesial Karakter:', data_tekssort["Spesial Karakter"])
        print(f'Total Semua Karakter Spesial Karakter dan Spasi: {data_tekssort["Spasi"]+data_tekssort["Spesial Karakter"]}')
    elif input_user=='4':
        key_banyak=max(data_tekssort,key=data_tekssort.get)
        key_sedikit=min(data_tekssort,key=data_tekssort.get)
        val_banyak=data_tekssort[key_banyak]
        val_sedikit=data_tekssort[key_sedikit]
        print(f'Terbanyak: Karakter {key_banyak} dengan banyak {val_banyak}')
        print(f'Tersedikit: Karakter {key_sedikit} dengan banyak {val_sedikit}')

file_teks=(open('lirik.txt','r'))
data_teks={}
hitung_karakter(data_teks)

file_teks.close()
