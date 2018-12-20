def div():
    tuso = int(input("Ban hay nhap gia tri cua tu so:"))
    mauso = int(input("Ban hay nhap gia tri cua mau so:"))

    try:
        ketqua = tuso / mauso

    except ZeroDivisionError:
        print("Mau nhap vao phai khac 0")
    else:
        print("Ket qua la:", ketqua)


def test_raise():
    x = int(input("Nhập vào số trong khoảng 1 đến 10:"))
    if x < 1 or x > 10:
        raise ValueError("Ban vua nhap vuot qua khoang cho phep")
    else:
        print("Ban da nhap hop le")
    return


# test_raise()
# div()
