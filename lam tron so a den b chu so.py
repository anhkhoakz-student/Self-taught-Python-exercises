try:
    so = float(input('Nhap so so muon lam tron: '))
    don_vi = int(input('Nhap so don vi muon lam tron: '))

    print('{0:.{1}f}'.format(so, don_vi))
except:
    print('Dinh dang dau vao khong hop le!')