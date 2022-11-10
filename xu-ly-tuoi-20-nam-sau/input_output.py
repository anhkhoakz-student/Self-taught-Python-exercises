try:
    with open('input.inp', 'r') as fileInp:
        ten = fileInp.readline().rstrip('\n')
        tuoi = int(fileInp.readline())

    with open('output.out','w') as fileOut:
        fileOut.write('Sau 20 năm nữa, {} sẽ {} tuổi'.format(ten, tuoi + 20))
        
except FileNotFoundError:
    with open('output.out', 'w') as fileOut:
        fileOut.write('Không tim thấy file "input.inp"!')
    userChoice = input('Bạn có muốn tạo tệp tin không? (Y/N').lower()
    if userChoice == 'y':
        with open('input.inp', 'w') as fileOut:
            fileOut.write('')
        with open('output.out', 'w') as fileOut:
            fileOut.write('Vui lòng nhập thông tin trong tệp tin "input.inp"')
    else:
        pass
except:
    with open('output.out', 'w') as fileOut:
        fileOut.write('Định dạng đầu vào không hợp lệ')