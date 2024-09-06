# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define e = Character("艾琳")
define s = Character("萨特莉", color="#007FFF")
define m = Character("我")

# 结局检定变量

# A：非持久性变量
default bravery = 0
default intelligence = 0
default sanity = 0

# B：持久性变量
define playthroughs = 0
define stubbornness = 0
define finished_endings = []

# C：持久性变量——达成结局数
define persistent.finished_endings = []

# 创建一个函数，用于比较变量值并返回对应的结局标签
# 该函数将在后续的结局检定中被调用

init python:
    def restart():
        global bravery, intelligence, sanity
        bravery = 0
        intelligence = 0
        sanity = 0

    def check_ending():    
        if bravery >= intelligence and bravery >= sanity:
            return "bravery"
        elif intelligence >= bravery and intelligence >= sanity:
            return "intelligence"
        else:
            return "sanity"

# 游戏在此开始。

label start:

    $ restart()

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为 bg room.png 或 bg room.jpg）来显示。

    scene bg normal:
        xalign 0.5 
        yalign 0.5
        size (1920, 1080)


    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。

    show eileen happy

    # 此处显示各行对话。
    "你好，我是艾琳。"

    # 产生一个影响数值的选项
    menu:
        "bravery":
            $ bravery += 1

        "intelligence":
            $ intelligence += 1

        "sanity":
            $ sanity += 1
    
    # 进行结局检定
    $ ending = check_ending()

    "..."

    # 根据检定结果跳转到对应的结局标签
    if ending == "bravery":
        jump ending_normal_bravery
    elif ending == "intelligence":
        jump ending_normal_intelligence
    else:
        jump ending_normal_sanity

    return

label ending_normal_bravery:

    play sound "sfx/train_passing.mp3" fadein 2

    "火车驶过，发出轰鸣声。"

    "紧接着，"

    play sound "sfx/explosions.mp3" volume 0.3

    "..."

    "等到爆破的烟尘散去，我仿佛看到了萨特莉的身影。"

    "..."

    "大概是幻觉吧。"

    # 删除角色
    hide eileen

    stop sound fadeout 5

    $ renpy.notify("达成结局：“螳臂挡车”")

    jump ending_normal_template

    return

label ending_normal_intelligence:

    play sound "sfx/train_passing.mp3" fadein 2

    "火车驶过，发出轰鸣声。"

    "我知道，萨特莉走了。"

    # 删除角色
    hide eileen

    stop sound fadeout 5

    queue sound "sfx/ambulance_passing.mp3" volume 0.3

    "萨特莉，你的灵魂永远在这里。"

    $ renpy.notify("达成结局：“归乡”")

    jump ending_normal_template

    return

label ending_normal_sanity:

    play sound "sfx/train_passing.mp3" fadein 2

    "火车驶过，发出轰鸣声。"

    # 删除角色
    hide eileen

    "在那之后，我再也没有见过萨特莉。"

    play sound "sfx/summer_wind.mp3" fadeout 1

    "有人说，她去了山顶那边。"

    "然后，"

    "..."

    stop sound fadeout 5

    $ renpy.notify("达成结局：“入江海”")

    jump ending_normal_template

    return

label ending_normal_template:
    play music "music/ending_normal.mp3" fadeout 1

    "SATERI"

    "音乐：春眠子"
    "文案：春眠子"
    "美术：春眠子"
    "程序：春眠子"

    "总编导：春眠子"

    jump status_update

label status_update:
    if ending not in finished_endings:
        $ finished_endings.append(ending)
    else: 
        $ stubbornness = True
    
    if playthroughs > 1:
        if stubbornness:
            "您是一个顽固的人。"
            "但是，"
            "您是否真的想要这样？"
        elif playthroughs > 2:
            "您达成了全部的结局。"
        "想要看看真正的结局吗？"

        menu:
            "是":
                jump true_ending
            "否":
                "好吧。"
                pass

    # 增加周目计数
    $ playthroughs += 1

    # 返回游戏开始
    "想要再来一次吗？"
    menu:
        "是":
            stop music fadeout 1
            stop sound fadeout 1
            jump start
            
        "否":
            "您没有给萨特莉希望。"
            "当然，您不必为此感到抱歉。"
            "再见。"
            pass

    return

label true_ending:
    "您的选择并没有改变萨特莉的命运。"
    "这一点您比谁都清楚。"

    return
