import random
#初始化比分
player_wins=0
computer_wins=0
ties=0
print(
    """
=============石头剪刀布=============
        1.石头
        2.剪刀
        3.布
        4.退出并查看此分    
===================================
"""
)
while True:
    player_choice=int(input("请选择你的操作（1-4）："))
    if player_choice not in range(1,5):
        print("输入不合法，请输入1-4中的数字")
        continue
    if player_choice==4:
        print(f"最终比分：玩家 {player_wins} : {computer_wins} 电脑 (平局 {ties})")
        if computer_wins==player_wins:
            print("平局，欢迎下次来战")
        elif computer_wins>player_wins:
            print("电脑获胜，再接再厉")
        else:
            print("恭喜你，太棒了！欢迎下次挑战")
        break
    else:
        computer_choice=random.randint(1,3)
        print(f"电脑的操作为：{computer_choice}")
    if player_choice == computer_choice:
        print("平局！")
        ties+=1
    elif player_choice==1 and computer_choice==2:
        print("恭喜你赢了！")
        player_wins+=1
    elif player_choice==2 and computer_choice==3:
        print("恭喜你赢了！")
        player_wins+=1
    elif player_choice==3 and computer_choice==1:
        print("你赢了！")
        player_wins+=1
    else:
        print("电脑赢了！")
        computer_wins+=1
        
    
