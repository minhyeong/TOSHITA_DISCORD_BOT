
import constant as c
import os

FILE_NAME = os.path.abspath('sozai/welcomeText.txt')

class WelcomeText:
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