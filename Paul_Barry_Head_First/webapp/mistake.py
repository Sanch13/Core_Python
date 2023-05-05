try:
    with open("test.txt") as file:
        data = file.read()
        print(data)
except FileNotFoundError as e:
    print("The file in not exists")
except PermissionError:
    print("This is not allow")
except Exception as err:
    print("Some other error occurred", str(err))
