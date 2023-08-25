from random import choice as c, sample as s

def simple_fun_game():
    while True:
        my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
        enter = eval(input("Enter your choice to win: "))
        if enter == c(my_list):
            print("You win!")
            break
        else:
            if c(my_list) in s(my_list, 2):
                if enter > c(my_list):
                    print("You are too close to win!")
                else:
                    print("Try again")
            else:
                print("Sorry! You have lost. Your correct choice is {}".format(c(my_list)))
                break
            
            
print(simple_fun_game())