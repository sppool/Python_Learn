def func1():
    print("this func from 'func.py'")


print('thks use func.py')

if __name__ == '__main__':  # 要在本程式內執行, 別的檔案import這個檔案不會執行！
    def func2():
        print("this func from 'func.py'")
    print('just func.py')
