def output_person_info():
    surname = input("Enter your surname: ")
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    print("Вас зовут " + name.capitalize() + " " +
          surname.capitalize() + ". Ваш возраст: " + age)


output_person_info()
