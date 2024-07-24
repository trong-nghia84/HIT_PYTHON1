import re
chuoi_ho_ten = input("Nhập chuỗi họ tên cần chuẩn hóa: ")
chuoi_ho_ten = re.sub(r'\s+', ' ', chuoi_ho_ten)
chuoi_ho_ten = chuoi_ho_ten.title()
ten_dem = re.findall(r'(\s+[A-Z][^A-Z]*$)', chuoi_ho_ten)
if ten_dem:
    chuoi_ho_ten = re.sub(r'(\s+[A-Z][^A-Z]*$)', ten_dem[0].lower(), chuoi_ho_ten)
print(f"Chuỗi họ tên sau khi chuẩn hóa: {chuoi_ho_ten}")