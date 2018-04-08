#! /usr/bin/python

# -*- coding: utf-8 -*-
import urllib.request, json, sys

#英単語を受け取って日本語訳を並べた文字列を返す関数

def translate(phrase):
    #Glosbe API により、　引数に与えられた単語の翻訳を取得

    #set URL

    from_lang = "en"    #English
    dest_lang = "ja"    #Japanese

    url = "https://glosbe.com/gapi/translate?from=" + from_lang + "&dest=" + dest_lang + "&format=json&phrase=" + phrase + "&pretty=true"
    json_data = urllib.request.urlopen(url).read()
    json_dict = json.loads(json_data)

    return_txt = "" #これを返り値にする

    tuc = json_dict["tuc"]  #tuc: list

    for i in range(len(tuc)):
        if u"phrase" in tuc[i].keys():
            return_txt += tuc[i]["phrase"]["text"] + "\n"

    return return_txt

if __name__ == '__main__':
    #sysをもちいてコマンドライン引数を取得

    argvs = sys.argv
    argc = len(argvs)

    if argc == 2:
        phrase = argvs[1]
    else:
        print(" Usage: python translate.py 'word' ")
        phrase = ""

    if phrase:
        phrase_jp = translate(phrase)
        if phrase_jp:   #翻訳が見つかった場合
            print(phrase_jp)
        else:   #翻訳が見つからなかった場合
            print("Not Found.")
