
import constant as c
import os

FILE_NAME = os.path.abspath('sozai/welcomeText.txt')

class WelcomeText:
    def __init__(self):
        pass

    def convert_ID(self, con_text): # チャンネル名をＩＤに変更
        for i in range(len(c.CH_ID)):
            con_text = con_text.replace(c.CH_NAME[i],c.CH_ID[i])
        return con_text

    def get_text(self, file_name): # ファイルをテキストに格納して返す
        f = open(file_name, 'r', encoding="utf-8_sig")
        line = f.readline()
        read_text = ''
        while line:
            line = f.readline()
            read_text += line
        f.close()
        return self.convert_ID(read_text)

class Dice:
    def __init__(self):
        self.output = 0

    def dice(self, dice_text):
        import random
        if "d" in dice_text or "D" in dice_text:
            pass
        elif "GO" in dice_text: # ガーデンオーダー
            go = int(dice_text[len("GO"):])
            self.output = random.randrange(100)
            print("1D100<=",end="")
            print(go,end="@")
            print(int(go*0.2),end="->")
            print(self.output,end="->")
            if self.output < go*0.2:
                print("クリティカル")
            elif self.output > 95:
                print("ファンブル")
            elif self.output < go:
                print("成功")
            else :
                print("失敗")
        elif "CC" in dice_text: # クトゥルフ
            pass
        elif "CCB" in dice_text: # クトゥルフ
            pass
                
        


a = Dice()
a.dice("GO80")
a.dice("GO60")

"""
DICE

1. CC<=80 CCB<=80
2. GO80
3. D100
4. k10[13] k10@13 
"""