jam = 17
tagihan_ke = 'Mr. Yoyo'
warehousing = {"harga_harian": 1000000, "total_hari": 15}
cleansing = {"harga_harian": 1500000, "total_harian": 10}
integration = {"harga_harian": 2000000, "total_hari": 15}
transform = {"harga_harian": 2500000, "total_harian":10}
sub_warehousing = warehousing["harga_harian"]* warehousing["total_hari"]
sub_cleansing = cleansing["harga_harian"]* cleansing["total_harian"]
sub_integration = integration["harga_harian"]* integration["total_hari"]
sub_transform = transform["harga_harian"]* transform["total_harian"]
total_harga = sub_warehousing + sub_cleansing + sub_integration + sub_transform
print("Tagihan kepada:")
print(tagihan_ke)
if jam > 19:
    print("Selamat malam, Anda harus membayat tagihan sebesar:")
elif jam > 17:
    print("Selamat sore, Anda harus membayar tagihan sebesar:")
elif jam > 12:
    print("Selamat siang, Anda harus membayar tagihan sebesar:")
else:
    print("Selamat pagi, Anda harus membabyar tagihan sebesar:") 
print(total_harga)