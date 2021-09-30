print("what is your name ?")
names = input()
print("i give you 4 lifes you guess correct number")
gues_num=10
life_time=4
count=0
play=True
while play:
    choise = int(input("guess number"))
    life_time=life_time-1
    count+=1
    if choise!=gues_num:
       print(f"{names} try again and your life {life_time} times")

    elif choise==gues_num:
        print(f"{names} win, Your Attemt is {count} times")
        play=False

    if life_time==0:
        print(f"{names} life end.")
        play=False