user = [
    {"nama": "arsene lupin", "nik": 1234, "jenis_kelamin": "male", "tanggal_lahir": "1902-03-23"},
    {"nama": "sherlock holmes", "nik": 4321, "jenis_kelamin": "male", "tanggal_lahir": "1876-08-16"},
    {"nama": "irene adler", "nik": 6789, "jenis_kelamin": "female", "tanggal_lahir": "1884-10-07"}
]

nama = input("Masukkan nama yang ingin dicari: ")

for i in user:
    if i["nama"].lower() == nama.lower():
        print(f"Data lengkap {nama}:")
        print(f"NIK            : {i['nik']}")
        print(f"Jenis Kelamin  : {i['jenis_kelamin']}")
        print(f"Tanggal Lahir  : {i['tanggal_lahir']}")
        break
else:
    print("Data tidak ada")
