print('Vui long nhap vao 2 so nguyen')
try:
    so_1 = int(input('Nhap so nguyen thu nhat: '))
    so_2 = int(input('Nhap so nguyen thu hai: '))
    tong = so_1 + so_2
    print('Tong 2 so la: ', tong)
except:
    print('dinh dang dau vao khong hop le!')
