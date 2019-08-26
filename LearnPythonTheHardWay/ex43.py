from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()


class Death(Scene):

    quips = [
        "你死了，死于这种情况的你甘心吗",
        "没有人会记得你...与你的战友",
        "真实一场失败的人生",
        "我想宇宙中的任意一个生物都能做的更好",
        "再见了 朋友"
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips) - 1)])
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
            来自小行星带的外星人已经入侵了你的飞船，并摧毁了整个舰队.
            你是最后的幸存者，你明白必须要前往武器工厂，拿到中子炸弹,。
            “安置在舰桥上足以摧毁整座飞船”，你想到，
            这也许就是你能够为你死去的队友做出的最后的复仇。
            “等着吧，入侵者们。”你咬咬牙，开始踏上路程。


            但计划总是赶不上变化，当你仅仅迈出了第一步，走到长廊上时，
            一个红皮黑牙，身穿邪恶小丑服的肥胖怪物发现了你 。
            ----------- Warning ----------
            它堵在你前往武器工厂的必经之路上，并且已经掏出了武器。
            你从未感觉死亡如此之近，你必须做些什么了：

            1. 开火！
            2. 尝试躲避
            3. 笑一笑
            """))

        action = input("> ")

        if action == "1":
            print(dedent("""
                你用你这一生最快的速度拔出了你的枪并向怪物开了火。
                遗憾的是你未能击穿敌人的装甲。
                这显然惹怒了它，它怒火朝天，直接向你进行了一波冲锋 。
                结果怎样想必不需要我多说了。
                这只是发生在宇宙中微不足道的一件小事罢了。
                """))
            return 'death'
        elif action == "2":
            print(dedent("""
                “我可以的”，你对自己说道。
                你从未感觉自己如此灵敏，就像李小龙附体，
                你觉得自己可以躲过一切攻击。

                遗憾的是外星人并不知道李小龙是谁，
                所以它并没有配合你。
                至少我们知道，
                你死的很有尊严。
                """))
            return 'death'
        elif action == "3":
            print(dedent("""
                在这千钧一发之际，你想起一句话
                “爱笑的人运气都不会太差”
                于是突然大笑了起来。
                外星人显然蒙住了，
                “你在笑什么？”
                “我想起高兴的事情”
                “什么事情？”
                “我一发出黑了”
                “？？？？”
                怪兽气坏了，大吼道
                “你个欧洲人，去死吧”
                显然它是个非洲人，而且是最非的那种
                一个平地摔都能将它带走
                """))
            return 'laser_weapon_armory'

        else:
            print("额，虽然我并不清楚你这是在做什么，但这显然没用。但幸好怪兽也没反应过来。")
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
            你溜进了工厂，但事情有些不对
            这里太安静了，安静到你可以清晰的听到自己的心跳声
            你高度警惕，提防着任何阴暗的角落。
            但你最终还是到了，你看到你心心念念的那颗中子炸弹
            就在你面前的盒子中

            这时候挡在你面前的是一道密码锁
            三位数的密码让你陷入了沉思
            显然密码并不会让你尝试 999 次，但应该会有10次左右的机会 。
            “来吧” 你想到，
            “赌命的时候到了”
            """))

        code = f"{randint(1, 9)}{randint(1, 9)}{randint(1, 9)}"
        guess = input("[keypad]> ")
        guesses = 0

        # 官方外挂
        print(code)

        while guess != code and guesses < 10:
            print(f'你尝试了{guess}, 不行，打不开这把锁。\n"还有{10 - guesses}次机会"，你想到')
            guesses += 1
            guess = input('[keypad]> ')

        if guess == code:
            print(dedent("""
                欧洲人的人生总是这么的简单，
                你轻松的打开了锁，
                拿到了【中子炸弹】
                """))
            return 'the_bridge'
        else:
            print(dedent("""
                人生的运气总是守恒的，
                显然，你现在体会到了被你嘲讽的外星人的感觉
                非酋的人生真的是太难了
                于是 你逐渐停止了思考。
                """))
            return 'death'


class TheBridge(Scene):

    def enter(self):
        print(dedent("""
            你带着炸弹走到了舰桥上
            这里有一个大惊喜在等着你
            唔。或者说是五个大惊喜
            好消息是这些大惊喜们忙着控制飞船，并没有在第一之间看到你
            并且武器也仅仅只是挂在身上
            不幸的是人生总有意外
            五分之一的幸运看到了你
            自然，也看到了你的大炸弹
            你要怎么做？

            1. 神圣手雷
            2. 怂一点，问题不大
        """))

        action = input("> ")

        if action == "1":
            print(dedent("""
                你将炸弹抛向怪物们的中间
                他们吓坏了，但总有怪物能在危机时刻冷静下来
                一枪秒了，还能说什么
                你在死去看到的最后一幅画面
                就是怪物们疯狂的试图停止炸弹的引爆
                “没用的，中子爆炸反应不可逆”
                你选择了和侵略者们同归于尽，
                这就是你最后的荣誉
                """))
            return 'death'

        if action == "2":
            print(dedent("""
                你将炸弹拿在手上，缓缓向怪物们逼近
                怪物们显然认出了你手上的危险物品是什么
                它们举起双手，满头大汗，示意自己不会做出什么威胁到你的举动。
                你慢慢的走向桥另一边的大门，怪物和你都十分紧张，
                但好在你们双方都克制住了
                你走到了大门前，将炸弹放下，穿过了大门
                使用你的员工卡锁定了桥两边的大门，使门强制关闭。
                在门关闭的瞬间，你看到了怪物们绝望的向你冲来
                “这门质量不错”，你没想到在怪物的冲锋下这门居然一丝颤动都没有。
                “还好当初升级飞船关键设施的公开投票上你并没有投反对票”
                “该我自己逃跑了，逃生舱就在不远处”
                """))

            return 'escape_pod'
        else:
            print("额，虽然我并不清楚你这是在做什么，但这显然没用。但幸好怪兽也没反应过来。")
            return "the_bridge"


class EscapePod(Scene):

    def enter(self):
        print(dedent("""
            这次你的运气好极了，路上一个外星人都没有
            你快速的跑到逃生设施中
            看起来还有5个逃生舱能使用
            但并不是所有的逃生舱都是安全的
            来吧，命运的抉择
            """))

        good_pod = randint(1, 5)

        # 官方外挂
        print(good_pod)

        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent(f"""
                你选择了 {guess} 号船并猛击了发射键
                飞船发射到了太空中
                但很快，飞船就出现了裂缝
                再见朋友，你即将成为宇宙中无尽漂浮的“垃圾”
                """))
            return 'death'
        else:
            print(dedent(f"""
                你选择了 {guess} 号船并猛击了发射键
                飞船发射到了太空中
                你回头看，看到了飞船的大爆炸
                你逃走了
                """))

            return 'finished'


class Finished(Scene):

    def enter(self):
        print("恭喜生还.")
        return 'finished'


class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
