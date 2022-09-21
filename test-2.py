Test_Case = int(input("Enter Test case: "))
for i in range(Test_Case):
    Test_Case, Hight = map(int, input().split()) #space-separated integers to list plyer
    list_of_hight = list(map(int, input().split())) # stage user multiple integers input, each separated space.
    count_slot_player = 0 #add number of plyer
    for i in list_of_hight: #check in plyer hight
        if i > Hight: #check hight of plyer # based on noted in problem statement
            count_slot_player = count_slot_player + 1 #count
    print("\n",count_slot_player)  #print count of player
