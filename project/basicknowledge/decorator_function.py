def decorator_function(original_fun):
    def wrapper_fun():
        print("デコレーたで機能を追加")
        original_fun()
        print("デコレーたで機能を終了")

    return wrapper_fun

@decorator_function
def show():
    print("元の関数が実行されました")

show()