tenBan1, chieuCaoBan1 = input("Nhập tên và chiều cao:\n").split()
tenBan2, chieuCaoBan2 = input("Nhập tên và chiều cao:\n").split()

try:
    chieuCaoBan1 = int(chieuCaoBan1)
    chieuCaoBan2 = int(chieuCaoBan2)

    if chieuCaoBan1 <= 0 or chieuCaoBan2 <= 0:
        print("Chiều cao phải lớn hơn 0!")

    elif chieuCaoBan1 > chieuCaoBan2:
        print("%s cao hơn %s" %(tenBan1, tenBan2))

    elif chieuCaoBan1 < chieuCaoBan2:
        print("%s cao hơn %s" %(tenBan2, tenBan1))

    else:
        print("%s cao bằng %s" %(tenBan1, tenBan2))

except:
    print("Định dạng đầu vào không hợp lệ")