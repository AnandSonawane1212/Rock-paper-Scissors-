import random
count=0
choices=["Paper","Rock","Scissors"]
result_calculation=[12,23,31]
player_choice=[0]*4
results=[[0 for j in range(4)] for i in range(4)]
while (count<50):
    print()
    print("Iteration No:-",(count+1))
    print("\t\tPlayer1\t\tPlayer2\t\tPlayer3\t\tPlayer4")
    for i in range(4):
        player_choice[i]=random.randrange(1,4)
    print("\t\t"+choices[player_choice[0]-1]+"\t\t"+choices[player_choice[1]-1]+"\t\t"+choices[player_choice[2]-1]+"\t\t"+choices[player_choice[3]-1])
    print()
    print("\t\tPlayer1\t\tPlayer2\t\tPlayer3\t\tPlayer4")
    for i in range(4):
        for j in range(5):
            if(j==0):
                print("Player"+str(i+1),end="\t\t")
                continue
            elif(i==(j-1)):
                print("_",end="\t\t\t")
                continue
            elif(int(str(player_choice[i])+str(player_choice[j-1]))in result_calculation):
                results[i][j-1]=results[i][j-1]+1
            print(results[i][j-1],end="\t\t\t")
        print()
    count+=1
