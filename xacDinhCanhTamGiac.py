try:
    a, b, c = map(float, input().split())
    if a <= 0 or b <= 0 or c <= 0:
        print("Các cạnh của tam giác phải lớn hơn 0")
    elif a + b > c and a + c > b and b + c > a:
        print(a, b, c, "là cạnh của tam giác")
    else:
        print(a, b, c, "không là cạnh của tam giác")
except:
    print("Định dạng đầu vào không hợp lệ")
    


# map(hàm, có thể lặp lại)