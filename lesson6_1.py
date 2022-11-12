def sayhello(): #沒有參數的funtion
    print("Hello!") 

def sayhello_withname(name): #參數是一個變數，name僅可使用於程式區塊，別的地方無法使用，有一個參數的FUNtion
    print(f"Hello﹑{name}")

def square_area(side): #有一個參數 
    area = side**2      
    return area  # funtion內的變數

def rectangle(width,height):
    area = width * height
    return area
         


if __name__ =="__main__":
    side = eval(input("請輸入正方形的邊"))
    area = square_area(side) #引數值傳遞到參數內   area 、side 為文件變數
    print(f"正方形,一邊為{side},面積為{area}")

    area = rectangle(15.5,20.9)
    print(f"矩形的寬是15.5,高是20.9,面積為{area}")
    