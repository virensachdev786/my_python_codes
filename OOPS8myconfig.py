class MyConfig(object):

    with open("/Users/virensachdev786/Desktop/term/bankdata.txt", "r") as f:
        a = f.read()

    b = a.split(":")

    print(b)

    c = list()

    for i in b:
        if "\n" in i:
            d = i.split("\n")

            for k in d:
                c.append(k)
        else:
            c.append(i)

    print(c)

    username = list()
    password = list()

    for i in range(len(c)):
        if i % 2 == 0:
            username.append(c[i])
        else:
            password.append(c[i])

    print("Username: {0}".format(username))
    print("Password: {0}".format(password))

    USERS = dict()

    i = 0
    for i in username:
        for j in password:
            USERS[i] = j
            password.remove(j)
            break




    print("Value of users is: {0}".format(USERS))
    print("Keys os users is: {0}".format(USERS.keys()))
    print("values of users is : {0}".format(USERS.values()))











    # with open("/Users/virensachdev786/Desktop/Term/bankdata.txt", "w")as f:
    #     f.write("Manish:hello123\n")
    #     f.write("Mukesh:world123")

    # USERS = {'Rakesh' : {'userid'  : 'hello',
    #                     'password': 'hello123'}
    #
    #         ,'Mukesh' : {'userid' : 'world',
    #                     'password': 'world123'}
    #         }