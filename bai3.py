for i in range(1, 10):
    # Tạo một list để lưu trữ các số chính phương từ 1 đến i^2
    squares = [j**2 for j in range(1, i+1)]
    # In list ra màn hình
    print(squares)