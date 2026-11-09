tasks=[]
while True:
    print("Добро пожаловать")
    print("1-Показать список задач")
    print("2-Добавить задачу")
    print("3-Вычеркнуть задачу")
    print("4-Выход")
    choise=input("выберите действие:")
    if choise=="1":
        if len(tasks)==0:
            print("ничего нет)")
        else:
            for i,task in enumerate(tasks,1):
                print(i,"-",task)

    elif choise=="2":
        task=input("какая задача?")
        tasks.append(task)
        print("готово!!")

    elif choise=="3":
        if len(tasks)==0:
            print("ПУсто:(")
        else:
            for i,task in enumerate(tasks,1):
                print(i,"-",task)
            number=int(input("Что вычеркнем?:)"))
            if 1<=number<=len(tasks):
                tasks.pop(number -1)
                print("ЧИРК")
            else:
                print("Нету такого номера!!")

    elif choise=="4":
        print("покаа")
        
        break
    else:
        print("Неизвестная команда")
        
        
        


