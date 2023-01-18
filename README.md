# 《Python编程与实践》课程大作业——井字棋游戏
作者：单博骥2021213241

### 一、设计目标

#### 1.项目背景介绍

井字棋（Tic-Tac-Toe），中国大陆、台湾又称为井字游戏、圈圈叉叉、大告圆圈（上海话“大告”就是叉）；另外也有打井游戏、○×棋的称呼，香港多称井字过三关、过三关，是种纸笔游戏，另有多种派生变化玩法。

井字棋是一种玩法非常简单的游戏，本项目中只涉及到其传统玩法。两个玩家，一个打圈(◯)，一个打叉（✗），轮流在3乘3的格上打自己的符号，最先以横、直、斜连成一线则为胜。

#### 2.选题介绍

由于井字棋的逻辑十分简单，可以轻松的设计出电脑玩家来与人类玩家进行对战，作为Python语言的初学者，将此项目来练习Python编程是一个很好的选择。

#### 3.设计目标

根据井字棋的规则，实现人类vs电脑，人类vs人类，电脑vs电脑功能。



### 二、设计思路及大体介绍

#### 1.设计思路

井字棋是双人对战游戏，所以我们需要创建两个玩家，玩家1和玩家2，玩家可以是人类也可以是电脑，这由游戏模式决定。

游戏过程是双方依次落子，因此可以选择一个大的循环来执行这一过程，当游戏结果出来的时候跳出循环。

如何让电脑来玩井字棋游戏是这个项目的关键，我采用的策略是，如果下一步没有人会取得胜利，优先选择落子在四个角的位置，其次选择落子在正中间，最后选择剩下的位置。

#### 2.一些重要的变量/参数介绍

##### （1）board

存放棋盘情况的列表，记录每个位置的是否有棋子，如果有是哪种棋子。

##### （2）player1，player2

玩家1和玩家2的名字，不一定是人类。

##### （3）player1_choice, player2_choice

玩家1和玩家2的棋子类型。

##### （4）available

当前可用的落子位置。

##### （5）turn

用来确定当前是轮到玩家1落子了还是玩家2落子了。

##### （6）mode

游戏模式，人类vs电脑 or 人类vs人类 or 电脑vs电脑。

#### 3.主体函数介绍

###### 按照游戏进程顺序

##### （1）rule()

尽管这是一个很简单的游戏，但是我觉得依然有必要介绍一下规则，这是一个完整的游戏应该做的。当然，如果你不想看规则，可以选择退出此环节。

```python
def rule(x):
    if x == "Y" :
        print("\n两个玩家,一个打圈(O),一个打叉(X),轮流在3乘3的棋盘上上打自己的符号,最先以横、直、斜连成一线则为胜。如果双方都下得正确无误，棋盘将会被填满而和局。")
        print(" 7 | 8 | 9 ")
        print("-----------")
        print(" 4 | 5 | 6 ")
        print("-----------")
        print(" 1 | 2 | 3 ")
        print("你需要输入1-9来选择落子的位置")
```

##### （2）choice()

在选择游戏模式以及输入名字之后，我们需要为每个人（无论是人类还是电脑）分配棋子类型（X还是O），该项目默认由玩家1来选择棋子类型，玩家2只能使用剩下的棋子类型。

为了方便，我使用了大写字母“X”和“O”，来代表两种类型的棋子。

```python
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
```

##### （3）first_player()

在分配完棋子类型之后，我们需要确定由那位玩家先落子，由于只有两个玩家，因此我们采用**从0和1中随机选择一个数**的方法来确定谁来先手。

```python
def first_player():
    #生成一个随机数来确定player1先落子还是player2先落子;
    import random
    return random.choice((0, 1))
```

##### （4）play()

完成所有准备工作后，我们会询问玩家是否准备好开始游玩。这是为了防止突然开始游戏导致玩家不知所措。如果玩家还没准备好，那么会直接结束本次对局。

```python
def play():
    return input("准备好开始游玩了吗?(Y/N)").startswith("Y")
```

##### （5）display_board()

打印棋盘函数，是项目中比较重要的函数，无论是选择落子位置还是显示落子后的棋盘状态，都会用到他。他的原理也很简单，调用函数后会显示两个棋盘，一个代表现在的情况，另一个代表剩余的可用位置，通过board变量导入现在的状态，avail导入可用的位置信息。

```python
def display_board(board,avail): 
    print("    " + "    棋局" + "            " + "    剩余的位置 ")
    print("    " + " {} | {} | {} ".format(board[7],board[8],board[9]) + "            " + " {} | {} | {} ".format(avail[7],avail[8],avail[9]))
    print("    " + "-----------" + "            " + "-----------")
    print("    " + " {} | {} | {} ".format(board[4],board[5],board[6]) + "            " + " {} | {} | {} ".format(avail[4],avail[5],avail[6]))
    print("    " + "-----------" + "            " + "-----------")
    print("    " + " {} | {} | {} ".format(board[1],board[2],board[3]) + "            " + " {} | {} | {} ".format(avail[1],avail[2],avail[3]))
```

##### （6）player_choice()

虽然名字很像，但是该函数与[choice()](#choice)没有什么联系，该函数是供玩家选择落子位置，首先我们需要检查还有哪些位置是空的、是可以落子的，这就需要用到[space_check()](#space_check)函数。该模块设置了一个**while**循环，这是为了当玩家不小心输入错误时能够有再输入一次的机会。

```python
def player_choice(board,name,choice):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input(f'\n{name} ({choice}), 选择你想要落子的位置: (1-9) \t'))
        if position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position) or position == "": 
            #检查输入的位置是否合规
            print(f"无效的位置，请重新输入!\n")   
    print("\n")        
    return position
```

##### （7）space_check()

一个简单的函数，用来检查输入的位置是否为空。

```python
def space_check(board,position):
    #检查位置是否为空
    return board[position] == ' '
```

##### （8）place_maker()

当进行落子后，我们要修改棋盘。我们需要做两件事，首先是把棋盘对应的位置放上对应的棋子，然后再把该位置从可用列表中去掉。

```python
def place_marker(board, avail, choice, position):
    #修改棋盘
    board[position] = choice
    #把当前位置从可用列表里去掉（修改为空）
    avail[position] = ' '
```

##### （9）computer_choice()

最重要的函数之一，它的作用是让电脑来选择落子的位置，首先电脑会列出当前所有可以落子的位置，然后它会通过在所有空位置落子（该过程在一个复制的棋盘上进行），然后调用[win_check()](#win_check)来进行判断，有没有玩家距离胜利只有一步之遥了，如果是对手，那么电脑会去阻止他，如果是自己，电脑会走那一步来让自己胜利。

如果下一步不能决定胜负，那么电脑会优先走四个角，如果都被占满了，则先考虑正中心的位置，再考虑其他位置。如果在此阶段，有多个位置可以下，比如四个角都是空的，那么会调用[select_random()](#select_random)来随机选择一个位置。

```python
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
```

##### （10）select_random()

这个函数供电脑在已经确定大致落子位置之后来随机选择落子的具体位置，这里的board不是整个棋盘，而是当前需要进行随机选择的范围。

```python
def select_random(board):
    import random
    #随机选择一个可用的位置落子
    num = len(board)
    #生成一个随机数来决定落子在哪里
    pos = random.randrange(0,num)
    return board[pos]
```

##### （11）win_check

在每一次落子之后都会进行检查，判断是否已经出现了赢家，进行判断的方式也非常简单，一共只有2*8种获胜方式，而且我们这里只判断刚刚落子结束的玩家的能否获胜的情况，所以全部判断一遍也不会很费时间。

```python
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
```

##### （12）full_board_check()

在井字棋中，取得平局的概率更大，如果在进行[win_check()](#win_check)之后没有人赢得游戏，还会进行[full_board_check()](#full_board_check)来判断是否平局。平局的条件就是当前棋盘已经下满了，但是没有玩家达成胜利条件。

```python
def full_board_check(board):
    #如果此时棋盘满了，那么平局，游戏结束
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True
```

##### （13）replay()

如果玩家意犹未尽，那么他可以选择再来一局。

```python
def replay():
    return input('\n想要再玩一次吗?:(Y/N)').startswith('Y')
```



### 三、过程问题

#### 1.存在的缺陷

玩家“在酒吧里点炒饭”是一个很头疼的事情，因为本项目有很多地方需要玩家自己输入选择内容，所以如果玩家输入了意料之外的内容，处理起来就会很麻烦，虽然可能是不小心输入错误，本项目只有在选择落子时可以给玩家重新选择的机会，其他地方大部分时候程序会直接崩溃。

#### 2.调试也是一个问题

每次检查修改代码后的成果时都要从头走一遍流程，这很费时间，尤其是在怎么改也改不好的时候。



### 四、总结

本项目是作者的第一个python项目，并没有使用python丰富的库函数，这也是项目的缺点，但是起到了很好的练习语法以及基本操作的作用，这对于初学者来说是很重要的。

尽管项目看起来很简单，但是依然花了作者很多时间，包括但不限于寻找合适的项目、查询错误代码、查询没有报错的错误（让人崩溃的就是程序不崩溃）等等。

井字棋稍加改进似乎可以变成五子棋，想要实现五子棋人类vs人类是和井字棋一样简单的，然而电脑的逻辑就要复杂很多了，这是本项目的未来发展方向之一。



