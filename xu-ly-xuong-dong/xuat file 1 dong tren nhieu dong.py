try:
    with open('input.inp', 'r') as fileInp:
        toanBoFile = fileInp.read()

    danhSachCacDong = toanBoFile.splitlines()

    cauHoanChinh = ' '.join(danhSachCacDong)
    
    danhSachCacTu = cauHoanChinh.split()
    
    cauDaXuLy = ' '.join(danhSachCacTu)

    with open('output.out', 'w') as fileOut:
        fileOut.write(cauDaXuLy)
except FileNotFoundError:
    with open('output.out', 'w') as fileOut:
        fileOut.write('Không tìm thấy file "input.inp"')