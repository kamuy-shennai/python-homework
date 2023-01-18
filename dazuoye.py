def rule():
    needRule = input("是否需要游戏规则介绍(Y/N):")
    if needRule == "Y" :
        print("\n两个玩家,一个打圈(O),一个打叉(X),轮流在3乘3的棋盘上上打自己的符号,最先以横、直、斜连成一线则为胜。如果双方都下得正确无误，棋盘将会被填满而和局。")
        print(" 7 | 8 | 9 ")
        print("-----------")
        print(" 4 | 5 | 6 ")
        print("-----------")
        print(" 1 | 2 | 3 ")
        print("你需要输入1-9来选择落子的位置\n")

def choice():
    player1_choice = ' '
    player2_choice = ' '
    #选择执子
    while player1_choice != 'X' or player1_choice != 'O':

        player1_choice = input(f"\n{player1},选择'X'还是'O'? 请输入英文字母:")[0].upper()
        #由于可能输入小写，故使用upper方法
        if player1_choice == 'X' or player1_choice == 'O':
        #如果是合规的选择，跳出循环继续
            break
        #如果不合规，重新选择
        print("无效的选择，请重新选择") 
    
    if player1_choice == 'X':
        player2_choice = 'O'
    else: 
        player2_choice = 'X'
    return player1_choice, player2_choice

def first_player():
    #生成一个随机数来确定player1先落子还是player2先落子;
    import random
    return random.choice((0, 1))

def play():
    return input("准备好开始游玩了吗?(Y/N)").startswith("Y")

def display_board(board,avail): 
    print("    " + " {} | {} | {} ".format(board[7],board[8],board[9]) + "            " + " {} | {} | {} ".format(avail[7],avail[8],avail[9]))
    print("    " + "-----------" + "            " + "-----------")
    print("    " + " {} | {} | {} ".format(board[4],board[5],board[6]) + "            " + " {} | {} | {} ".format(avail[4],avail[5],avail[6]))
    print("    " + "-----------" + "            " + "-----------")
    print("    " + " {} | {} | {} ".format(board[1],board[2],board[3]) + "            " + " {} | {} | {} ".format(avail[1],avail[2],avail[3]))


def player_choice(board,name,choice):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input(f'\n{name} ({choice}), 选择你想要落子的位置: (1-9) \t'))
        if position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position) or position == "": 
            #检查输入的位置是否合规
            print(f"无效的位置，请重新输入!\n")   
    print("\n")        
    return position

def win_check(board, choice):
    #检查是否当前玩家赢得了比赛
    
    #横
    return ( 
       ( board[1] == choice and board[2] == choice and board[3] == choice )
    or ( board[4] == choice and board[5] == choice and board[6] == choice )
    or ( board[7] == choice and board[8] == choice and board[9] == choice )
    #竖
    or ( board[1] == choice and board[4] == choice and board[7] == choice )
    or ( board[2] == choice and board[5] == choice and board[8] == choice )
    or ( board[3] == choice and board[6] == choice and board[9] == choice )
    #斜
    or ( board[1] == choice and board[5] == choice and board[9] == choice )
    or ( board[3] == choice and board[5] == choice and board[7] == choice )  )

def selectRandom(board):
    import random
    #随机选择一个可用的位置落子
    num = len(board)
    #生成一个随机数来决定落子在哪里
    pos = random.randrange(0,num)
    return board[pos]



def Computer_choice(board, name, choice):
    position = 0

    #所有可以落子的可能
    possibilities = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]

    #判断是否有距胜利只有一步之遥的位置
    for let in ['O', 'X']:
        for i in possibilities:
            #复制一个当前状态的棋盘判断自己下一步能否取得胜利，或者对手下一步能否取得胜利
            boardCopy = board[:]
            #如果落子在i位置的话
            boardCopy[i] = let
            if(win_check(boardCopy, let)):
                position = i
                return position


    #如果不能一步到达胜利，优先放在角落里        
    openCorners = [x for x in possibilities if x in [1, 3, 7, 9]]
    if len(openCorners) > 0:
        position = selectRandom(openCorners)
        return position
    
    #其次放在中间格子里
    if 5 in possibilities:
        position = 5
        return position

    #最后选择其他位置
    openEdges = [x for x in possibilities if x in [2, 4, 6, 8]]
    
    if len(openEdges) > 0:
        position = selectRandom(openEdges)
        return position




def space_check(board,position):
    #检查位置是否为空
    return board[position] == ' '

def place_marker(board, avail, choice, position):
    #修改棋盘
    board[position] = choice
    #把当前位置从可用列表里去掉（修改为空）
    avail[position] = ' '

def full_board_check(board):
    #如果此时棋盘满了，那么平局，游戏结束
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def replay():
    return input('\n想要再玩一次吗?:(Y/N)').startswith('Y')






print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("\t\t 健康游戏忠告 \n")
print("\t 抵制不良游戏，拒绝盗版游戏。")
print("\t 注意自我保护，谨防受骗上当。")
print("\t 适度游戏益脑，沉迷游戏伤身。")
print("\t 合理安排时间，享受健康生活。")
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("按回车键开始")
print("\n欢迎游玩井字棋\n")

rule()

while True:
    #创建棋盘
    board = [' ']*10
    #可落子的位置
    available = [str(num) for num in range(0,10)]
    #选择游戏模式
    print("[0] 人类 对战 人类")
    print("[1] 人类 对战 电脑")
    print("[2] 电脑 对战 电脑")
    mode = int(input("请选择游戏模式："))
    
    if mode == 0:
        print("\n注意:玩家1可以选择他想要的棋子\n")
        player1 = input("请输入玩家1的名字:")
        player2 = input("请输入玩家2的名字:")
        player1_choice, player2_choice = choice()
        print(f"\n{player1}:", player1_choice)
        print(f"{player2}:", player2_choice)

    elif mode == 1:
        player1 = input("请输入您的名字:")
        player2 = "电脑"
        player1_choice, player2_choice = choice()
        print(f"\n{player1}:", player1_choice)
        print(f"{player2}:", player2_choice)

    elif mode == 2:
        player1 = "电脑1"
        player2 = "电脑2"
        player1_choice, player2_choice = 'X','O'

    else:
        print("无效的选择，请重新选择")
        continue

    #随机选择先手
    if first_player():
        turn = player1
    else:
        turn = player2

    print(f"\n{turn}将会先落子")

    if mode == 2:
        input("电脑与电脑之间的对弈会很迅速，你准备好了吗？按回车以开始观看这精彩的对局")
        play_game = 1
    else:
        play_game = play()   

    while play_game:
        if turn == player1:

            display_board(board,available)
            if mode != 2:
                position = player_choice(board, player1, player1_choice)
            else:
                position = Computer_choice(board, player1, player1_choice)
                print(f'\n{player1} ({player1_choice}) 在 {position}处落子\n')

            #落子后修改棋盘
            place_marker(board, available, player1_choice, position)

            #落子后是否玩家1是否赢得比赛
            if win_check(board, player1_choice):
                #玩家1赢了 打印棋盘
                display_board(board, available)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                
                print(f'\n\n恭喜 {player1}赢得了这场对局\n\n')
                
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                #游戏结束
                play_game = False
            else:
                #检查棋盘是否已经满了
                if full_board_check(board):
                    #如果已经满了，打印棋盘
                    display_board(board, available)
                    print("~~~~~~~~~~~~~~~~~~")
                    print('\n平局!\n')
                    print("~~~~~~~~~~~~~~~~~~")
                    break
                #如果没满，轮到player2了    
                else:
                    turn = player2

        else:
                display_board(board,available)
                if mode == 0:
                    position = player_choice(board, player2, player2_choice)
                else:
                    position = Computer_choice(board, player2, player2_choice)
                    print(f'\n{player2} ({player2_choice}) 在 {position}处落子\n')

                #落子后修改棋盘
                place_marker(board, available, player2_choice, position)

                #落子后是否玩家2是否赢得比赛
                if win_check(board, player2_choice):
                #玩家2赢了 打印棋盘
                    display_board(board, available)
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    if mode == 1:
                        print('\n\n很遗憾!你被电脑击败了!\n\n')
                    else:
                        print(f'\n\n恭喜 {player2}赢得了这场对局\n\n')
                
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    #游戏结束
                    play_game = False
                else:
                #检查棋盘是否已经满了
                    if full_board_check(board):
                    #如果已经满了，打印棋盘
                        display_board(board, available)
                        print("~~~~~~~~~~~~~~~~~~")
                        print('\n平局!\n')
                        print("~~~~~~~~~~~~~~~~~~")
                        break
                    #如果没满，轮到player1了    
                    else:
                        turn = player1

    #游戏结束是否重新开始
    if replay():
        continue
    else:
        break
print("\n\n\n\n\n\n\t再见!\n\n\n\n\n\n")