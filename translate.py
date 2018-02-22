#! /usr/bin/python 
# -*- coding: utf-8 -*- 

import urllib2, json, sys
import unicodedata
import commands
import re

def translate(phrase):
    try:
        phrase=phrase.decode('utf-8')
    except UnicodeDecodeError:
        phrase=phrase.decode('cp932')

    if is_japanese(phrase):
        from_lang = u"ja"# English   
        dest_lang = u"en"# Japanese 
    else:
        from_lang = u"en"# English   
        dest_lang = u"ja"# Japanese 

    url = u"https://glosbe.com/gapi/translate?from=" \
        + from_lang + u"&dest=" + dest_lang \
        + u"&format=json&phrase=" + phrase + u"&pretty=true"
    response = urllib2.urlopen(url.encode("utf-8"))
    json_data = response.read()
    json_dict = json.loads(json_data)
    return_txt = "" 
    tuc = json_dict["tuc"]# tuc: list   
    for i in range(len(tuc)):
        if u"phrase" in tuc[i].keys():
            #if is_hiragana(match_word):
            return_txt = tuc[i]["phrase"]["text"]
            break
    check = commands.getoutput("sudo sh /home/pi/open-jtalk/AquesTalkPi/aquestalkpi/talkpi.sh " + phrase)
    check = commands.getoutput("sudo sh /home/pi/open-jtalk/AquesTalkPi/aquestalkpi/talkpi.sh " + return_txt.encode("utf-8"))
    return "complete translation !!!"

def is_japanese(string):
    for ch in string:
        name = unicodedata.name(ch) 
        if "CJK UNIFIED" in name \
        or "HIRAGANA" in name \
        or "KATAKANA" in name:
            return True
    return False

#def is_hiragana(string):
#    all_hiragana = "ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをん"
#    return all([ch in all_hiragana for ch in string])

if __name__ == '__main__':
    argvs = sys.argv
    argc = len(argvs)

    if argc == 2:
        phrase=sys.argv[1]

    else:
        # 使い方を教える                                                 
        print "Usage: python translate.py 'word'"
        phrase = ""
    if phrase:
        phrase = translate(phrase)
        if phrase:
            print phrase
        else:
            print "Not Found. "
