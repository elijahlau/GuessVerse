# coding=utf-8
from kivy.app import App
from kivy.uix.image import Image, AsyncImage
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core.text import LabelBase
from kivy.resources import resource_add_path, resource_find
from kivy.uix.spinner import Spinner
from kivy.uix.label import Label
import sqlite3
import random
import os
import io

resource_add_path(os.path.abspath('./data/fonts'))
LabelBase.register('Roboto', 'DroidSansFallback.ttf')

conn = sqlite3.connect('forum.db')
c = conn.cursor()
global verse, bookno, chapno, versno, anschar10, anschar20, anschar30, anschar40

chapmax = {
    '创世记': '50',
    '出埃及记': '40',
    '利未记': '27',
    '民数记': '36',
    '申命记': '34',

    '约书亚记': '24',
    '士师记': '21',
    '路得记': '4',
    '撒母耳记上': '31',
    '撒母耳记下': '24',
    '列王记上': '22',
    '列王记下': '25',
    '历代志上': '29',
    '历代志下': '36',
    '以斯拉记': '10',
    '尼希米记': '13',
    '以斯帖记': '10',

    '约伯记': '42',
    '诗篇': '150',
    '箴言': '31',
    '传道书': '12',
    '雅歌': '8',

    '以赛亚书': '66',
    '耶利米书': '52',
    '耶利米哀歌': '5',
    '以西结书': '48',
    '但以理书': '12',

    '何西阿书': '14',
    '约珥书': '3',
    '阿摩司书': '9',
    '俄巴底亚书': '1',
    '约拿书': '4',
    '弥迦书': '7',
    '那鸿书': '3',
    '哈巴谷书': '3',
    '西番亚书': '3',
    '哈该书': '2',
    '撒迦利亚书': '14',
    '玛拉基书': '4',

    '马太福音': '28',
    '马可福音': '16',
    '路加福音': '24',
    '约翰福音': '21',
    '使徒行传': '28',

    '罗马书': '16',
    '哥林多前书': '16',
    '哥林多后书': '13',
    '加拉太书': '6',
    '以弗所书': '6',
    '腓立比书': '4',
    '歌罗西书': '4',
    '帖撒罗尼迦前书': '5',
    '帖撒罗尼迦后书': '3',
    '提摩太前书': '6',
    '提摩太后书': '4',
    '提多书': '3',
    '腓利门书': '1',

    '希伯来书': '13',
    '雅各书': '5',
    '彼得前书': '5',
    '彼得后书': '3',
    '约翰一书': '5',
    '约翰二书': '1',
    '约翰三书': '1',
    '犹大书': '1',
    '启示录': '22'}

bookdict = {
    '创世记': '1',
    '出埃及记': '2',
    '利未记': '3',
    '民数记': '4',
    '申命记': '5',

    '约书亚记': '6',
    '士师记': '7',
    '路得记': '8',
    '撒母耳记上': '9',
    '撒母耳记下': '10',
    '列王记上': '11',
    '列王记下': '12',
    '历代志上': '13',
    '历代志下': '14',
    '以斯拉记': '15',
    '尼希米记': '16',
    '以斯帖记': '17',

    '约伯记': '18',
    '诗篇': '19',
    '箴言': '20',
    '传道书': '21',
    '雅歌': '22',

    '以赛亚书': '23',
    '耶利米书': '24',
    '耶利米哀歌': '25',
    '以西结书': '26',
    '但以理书': '27',

    '何西阿书': '28',
    '约珥书': '29',
    '阿摩司书': '30',
    '俄巴底亚书': '31',
    '拿鸿书': '32',
    '弥迦书': '33',
    '约拿书': '34',
    '哈巴谷书': '35',
    '西番亚书': '36',
    '哈该书': '37',
    '撒迦利亚书': '38',
    '玛拉基书': '39',

    '马太福音': '40',
    '马可福音': '41',
    '路加福音': '42',
    '约翰福音': '43',
    '使徒行传': '44',

    '罗马书': '45',
    '哥林多前书': '46',
    '哥林多后书': '47',
    '加拉太书': '48',
    '以弗所书': '49',
    '腓立比书': '50',
    '歌罗西书': '51',
    '帖撒罗尼迦前书': '52',
    '帖撒罗尼迦后书': '53',
    '提摩太前书': '54',
    '提摩太后书': '55',
    '提多书': '56',
    '腓利门书': '57',

    '希伯来书': '58',
    '雅各书': '59',
    '彼得前书': '60',
    '彼得后书': '61',
    '约翰一书': '62',
    '约翰二书': '63',
    '约翰三书': '64',
    '犹大书': '65',
    '启示录': '66'}




# class Background:
#     pass

def recre_booklist():
    #    conn = sqlite3.connect('forum.db')
    #    c = conn.cursor()     #create table booklist (chinese)
    conn = sqlite3.connect('C:/Users/Aero/PycharmProjects/forum.db')
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS booklist")
    c.execute("CREATE TABLE booklist(Id int, BookName text)")
    conn.commit()
    print("recre booklist done")


def write_booklist():
    #    conn = sqlite3.connect('forum.db')
    #    c = conn.cursor()
    f11 = open("booklist backup 1.txt", "r", encoding='GBK')
    for x in range(1, 67):
        text_line = f11.readline()
        text_line = text_line.rstrip('\n')
        print(type(text_line), text_line)
        c.execute("INSERT INTO booklist (Id, BookName) VALUES (?,?)",
                  [x, text_line])
        conn.commit()
    f11.close()
    print("write booklist done")


def recre_verse_hhb():
    # create table: Verse_hhb
    #    conn = sqlite3.connect('forum.db')
    #    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS verse_hhb")
    c.execute("CREATE TABLE verse_hhb (Id INT, BookNo INT, ChapNo INT, VersNo INT, Verse Text)")
    #    c.execute("CREATE TABLE verse_hhb (Id INT AUTO_INCREMENT PRIMARY KEY, "
    #                     "BookNo INT, ChapNo INT, VersNo INT, Verse Text)")
    conn.commit()
    print("recre verse hhb done")


def write_verse_hhb():
    conn = sqlite3.connect('forum.db')
    c = conn.cursor()
    f1 = open("hhb.txt", "r", encoding='GBK')  # format text line： gen 1:1 起初。。。
    x = 0
    for x in range(1, 31103):
        text_line1 = f1.readline()
        text_line1 = text_line1.rstrip("\n")
        textsepa = text_line1.split(" ", 2)
        verse = textsepa[2]
        c.execute("INSERT INTO verse_hhb (Id, Verse) VALUES (?,?)",
                  [x, verse])
    print("write verse hhb done")
    f1.close()
    conn.commit()


def write_bkchvr_hhb():
    conn = sqlite3.connect('forum.db')
    c = conn.cursor()
    f2 = open("index.txt", "r", encoding='GBK')
    x = 0
    for x in range(1, 31103):
        index_line = f2.readline()
        index_line = index_line.rstrip("\n")
        bkchver = index_line.split(":", 2)
        bookno = bkchver[0]
        chapno = bkchver[1]
        versno = bkchver[2]
        #        c.execute("UPDATE verse_hhb set (BookNo, ChapNo, VersNo) VALUES (?,?,?)",
        #                  [bookno, chapno, versno])
        query1 = """UPDATE verse_hhb SET BookNo=? WHERE Id = ?"""
        query2 = """UPDATE verse_hhb SET ChapNo=? WHERE Id = ?"""
        query3 = """UPDATE verse_hhb SET VersNo=? WHERE Id = ?"""
        data1 = (bookno, x)
        data2 = (chapno, x)
        data3 = (versno, x)
        c.execute(query1, data1)
        c.execute(query2, data2)
        c.execute(query3, data3)
    print("write bkchvr done")
    f2.close()
    conn.commit()


def try_print_booklist():
    conn = sqlite3.connect('forum.db')
    c = conn.cursor()
    cursor = c.execute("SELECT * from booklist WHERE id = 55")
    mybookrow = c.fetchone()
    for row in cursor:
        print("type of mybookrow is = ", mybookrow)
        print(row)
    conn.commit()


def pick_rand_verse(booksltfn, chapsltfn):
    global myverse, verse, bookno, chapno, versno
    conn = sqlite3.connect('forum.db')
    c = conn.cursor()
    c.execute("SELECT * from verse_hhb where bookno=? AND chapno=? ORDER BY Random() LIMIT 1", (booksltfn, chapsltfn,))
    myverse = c.fetchone()
    #    print("myverse is :", myverse)
    #    print("type of myverse is :", type(myverse))
    bookno = int(myverse[1])
    chapno = int(myverse[2])
    versno = int(myverse[3])
    verse = str(myverse[4])
    print("pick rand verse done, verse is : ", verse)
    conn.commit()
    return myverse, verse, bookno, chapno, versno

def pick_lookfor_verse(lookforraw):
    global myverse, verse, bookno, chapno, versno
    conn = sqlite3.connect('forum.db')
    c = conn.cursor()
    lookstr = lookforraw.replace(lookforraw, ("%"+lookforraw+"%"))
    print("PICK LOOKFOR FUNC lookstr:", lookstr)
#    abc = lookforraw
#    abc = str("耶稣")
#    c.execute("SELECT * from verse_hhb where verse LIKE ? ORDER BY Random() LIMIT 1", (abc,))
    c.execute("SELECT * from verse_hhb where verse LIKE ? ORDER BY Random() LIMIT 1", (lookstr,))
    myverse = c.fetchone()
    print("LOOKFOR FUNC  myverse is :", myverse)
    #    print("type of myverse is :", type(myverse))
    bookno = int(myverse[1])
    chapno = int(myverse[2])
    versno = int(myverse[3])
    verse = str(myverse[4])
    print("pick LOOKFOR verse done, verse is : ", verse)
    conn.commit()
    return myverse, verse, bookno, chapno, versno


def repick_verse():  # ensure verse not too short
    conn = sqlite3.connect('forum.db')
    c = conn.cursor()
    global myverse, verse, bookno, chapno, versno
    pick_rand_verse()
    while (int(len(verse)) < 12) or (int(len(verse)) > 40):
        pick_rand_verse()
        verse = str(myverse[4])
        bookno = int(myverse[1])
    else:
        verse = str(myverse[4])
        bookno = int(myverse[1])
        pass
    #    print("verse is repicked= ")
    conn.commit()
    return myverse, verse, bookno, chapno, versno


def call_book_name(bookno):
    #    global bookno, mybookrow, bookname
    with conn:
        #    conn = sqlite3.connect('forum.db')
        #    c = conn.cursor()
        c.execute("SELECT * FROM booklist WHERE Id=?", (bookno,))
    mybookrow = c.fetchone()
    bookname = str(mybookrow[1])
    conn.commit()
    #    print("mybookrow is : ", mybookrow)
    return bookname

def call_book_no(bookname):
    #    global bookno, mybookrow, bookname
    with conn:
        #    conn = sqlite3.connect('forum.db')
        #    c = conn.cursor()
        c.execute("SELECT * FROM booklist WHERE BookName=?", (bookname,))
    mybookrow = c.fetchone()
    print("CALL BOOK NO FUNC mybookrow:", mybookrow)
    #    bookname = mybookrow[1]
    bookno = int(mybookrow[0])
    conn.commit()
    print("bookno is : ", bookno)
    return bookno


def make_qverse(verse, bookname, chapno, versno):
    global ansloc1
    symbol = str(' ．’！ - 、、；”（（） ） 《  》 a b c d e f g h i j k l m n o p q r s '
                 't u v w x y z ， ： “ ？ ‘  。 , . 1 2 3 4 5 6 7 8 9 0 : ')
    a = 0
    symloclist = []
    symlist = []
    # symloclist.append(0)
    print("0 make qverse func; verse: ", verse)
    for x in verse:
        a = a + 1
        if x in symbol:
            symloclist.append(a)
            symlist.append(x)
    if len(verse) not in symloclist: symloclist.append(len(verse))
    print("1 make qverse func symloclist is:", symloclist, "; and symlist is: ", symlist)
    print("2 make qverse func length of the symloclist is :", len(symloclist))
    # how many cho in the verse?
    n = -1
    cho = 0
    slotcholist = []
    avalcho = []  # ensure the symbols cannot be too closed to each other.
    if symloclist[0] >= 5:
        avalcho.append(symloclist[0])
        print("1.9 make qverse func first append ", x)
    for x in symloclist:  ###symloclist content the index of the symbol's locations of verse
        if x == symloclist[0]: continue
        n = n + 1
        dif = x - symloclist[n]
        # dif btwn symloclist() and the previous symloclist()
        print("2 make qverse func n is:", n, "     and   x is :", x)
        if dif > 4:
            slotcholist.append(x)
            avalcho.append(x)
            print("2.1 make qverse func APPEND X ", x)
        else:
            slotcholist.append("-1")
    print("3 make qverse func the slotcholist is :  ", slotcholist)
    print("4 make qverse func the avalcho is :  ", avalcho)
    print("5 make qverse func length of the avalcho is :", len(avalcho))
    if avalcho != []:
        selcho = random.randint(1, len(avalcho))  # avalcho =[] means comma too close...
        print("6 make qverse func selcho is :    ", selcho)
        selarea1 = avalcho[selcho - 1]  # selcho is a small int, selarea is ind of the verse
        print("7 make qverse func selarea1  :", selarea1)
        a = 0
        for x in symloclist:  # define ansloc1 range, between selarea1 and selarea0
            if x == selarea1: selarea0 = a
            a = x
        # now select chars within selarea0 to selarea1.
        print("8 make qverse func selarea range from (the num is symloc or front/end):", selarea0, "to", selarea1)
        if selarea1 - selarea0 == 5:
            ansloc1 = selarea0
        elif selarea1 - selarea0 < 5:
            ansloc1 = 0
        else:
            ansloc1 = selarea0 + random.randint(0, (selarea1 - selarea0 - 5))
        print("9 make qverse func ansloc1 is :", ansloc1)

    if avalcho == []:
        ansloc1 = 0
    qverse_raw = verse.replace(verse[ansloc1:ansloc1 + 4], "__ __ __ __", 1)
    qverse = "《" + bookname + str(chapno) + "章" + str(versno) + "节》\n " + qverse_raw
    print("10 make qverse func : qverse is   ", qverse)
    return qverse, ansloc1


def make_sugg():
    sugg = ""
    ##print("before, sugg length is ", len(str(sugg)))
    # build a random 40 chars string, non repeat chars, cannot include answer chars
    ## to prevent repeat selection
    ## to prevent repeat selection

    symbollist = ('．，’ - ！、；”（ ） 《  》 a b c d e f g h i j k l m n o p q r s '
                  't u v w x y z ， ： “ ？ ‘  。 , . 1 2 3 4 5 6 7 8 9 0 : ' +
                  anschar10 + anschar20 + anschar30 + anschar40)
    aaa = 0
    while len(str(sugg)) < 40:
        def pickrchar():
            global myrchar1, myrchar2, myrchar3
            conn = sqlite3.connect('forum.db')
            c = conn.cursor()
            c.execute("SELECT * FROM verse_hhb ORDER BY Random() LIMIT 1 ")
            myrdata = c.fetchone()
            myrvraw = str(myrdata[4])
            myrv = myrvraw
            #            print("myrv is :   ", myrv)
            rd1 = random.randint(0, (len(myrv) - 1))
            rd2 = random.randint(0, (len(myrv) - 1))
            rd3 = random.randint(0, (len(myrv) - 1))
            #            print("rd1 rd2 rd3:   ", rd1, rd2, rd3)
            myrchar1 = myrv[rd1]
            myrchar2 = myrv[rd2]
            myrchar3 = myrv[rd3]
            return myrchar1, myrchar2, myrchar3

        pickrchar()
        stchar = myrchar1.strip(symbollist)
        if stchar not in sugg: sugg = sugg + stchar
        stchar = myrchar2.strip(symbollist)
        if stchar not in sugg: sugg = sugg + stchar
        stchar = myrchar3.strip(symbollist)
        if stchar not in sugg: sugg = sugg + stchar
        aaa = aaa + 3  # #print("stchar = ", stchar)
    return sugg


def make_suggfn(sugg):
    global anschar10, anschar20, anschar30, anschar40, qverse
    global suggfn, ansind10, ansind20, ansind30, ansind40
    # recre_booklist()
    # write_booklist()
    # recre_verse_hhb()
    # write_verse_hhb()
    # write_bkchvr_hhb()
    #    verse = str(pick_rand_verse(booksltfn)[1])
    # print("verse = str(pick_rand_verse()[1]) :  ", verse)
    # myverse = pick_rand_verse()[1]
    # print("myverse = str(pick_rand_verse()[1]) :  ", verse)
    # if int(len(verse)) >= 50 or (int(len(verse)) <= 12):
    # #    print("verse out of range FOUND!")
    #     while True:
    # #        print("len out of range, then repick")
    # #        print("verse is :", verse)
    #         pick_rand_verse(booksltfn)
    #         if int(len(verse)) < 50 and (int(len(verse)) > 12):
    #             break

    # print("bookname is ", call_book_name(bookno))
    #    myverse = (call_book_name(bookno)+""+str(chapno)+":" + str(versno) + " " + verse)
    # print("Full verse is :", myverse)
    #    bookname = call_book_name(bookno)
    #    qverse_raw = make_qverse(verse, bookname)
    #    qverse = qverse_raw[0]
    # print("qverse is   ", qverse)
    ## build 4 anschars
    answer = "答案123"
    anschar10 = verse[ansloc1 + 0]  # anschar is a single char, anchar10 is the first char
    anschar20 = verse[ansloc1 + 1]  # anchar can be a symbol ， 。 ； ：
    anschar30 = verse[ansloc1 + 2]
    anschar40 = verse[ansloc1 + 3]
    anschar1234 = anschar10 + anschar20 + anschar30 + anschar40

    ansind10 = random.randint(1, 10)
    ansind20 = random.randint(11, 20)
    ansind30 = random.randint(21, 30)
    ansind40 = random.randint(31, 40)

    sugg = make_sugg()
    suggfn = sugg.replace(sugg[ansind10 - 1], anschar10, 1)
    suggfn = suggfn.replace(suggfn[ansind20 - 1], anschar20, 1)
    suggfn = suggfn.replace(suggfn[ansind30 - 1], anschar30, 1)
    suggfn = suggfn.replace(suggfn[ansind40 - 1], anschar40, 1)
    return suggfn, ansind10, ansind20, ansind30, ansind40


def make_anschar(qverse, ansloc1):
    global anschar1234, anschar10, anschar20, anschar30, anschar40
    anschar10 = verse[ansloc1 + 0]  # anschar is a single char, anchar10 is the first char
    anschar20 = verse[ansloc1 + 1]  # anchar can be a symbol ， 。 ； ：
    anschar30 = verse[ansloc1 + 2]
    anschar40 = verse[ansloc1 + 3]
    anschar1234 = anschar10 + anschar20 + anschar30 + anschar40
    #    print()
    return anschar1234, anschar10, anschar20, anschar30, anschar40

defaultbook = "马太福音"
booksltfn = 40
if chapmax[defaultbook] == 1:
    chapsltfn = 1
else:
    chapsltfn = random.randint(1, int(chapmax[defaultbook]))
print("001 MAIN chapmax(defaultbook) and chapsltfn : ", chapmax[defaultbook], chapsltfn)

bookname = call_book_name(booksltfn)
pick_rand_verse(booksltfn, chapsltfn)  # return myverse, verse, bookno, chapno, versno
qverse_ansloc1 = make_qverse(verse, bookname, chapno, versno)  # return qverse, ansloc1
qverse = qverse_ansloc1[0]
ansloc1 = qverse_ansloc1[1]

res_anschar = make_anschar(qverse, ansloc1)
anschar1234 = res_anschar[0]
anschar10 = res_anschar[1]
anschar20 = res_anschar[2]
anschar30 = res_anschar[3]
anschar40 = res_anschar[4]

ansind10 = random.randint(1, 10)
ansind20 = random.randint(11, 20)
ansind30 = random.randint(21, 30)
ansind40 = random.randint(31, 40)

print("0 MAIN scripts; anschar 5 items", anschar1234, anschar10, anschar20, anschar30, anschar40)
answer = "答案"
sugg = make_sugg()
suggfn = make_suggfn(sugg)[0]
print("0 MAIN scripts; suggfn is :", suggfn)

global slt1, slt2, slt3, slt4
slt1 = 0
slt2 = 0
slt3 = 0
slt4 = 0
ansclick = 0
runnum = -1

# answer = "答案123"
# rev = "显示123"
# print("anschar1234  :", anschar10, anschar20, anschar30, anschar40)

messagelist = [
    "要更了解如何使用，请点击[再来一题]按钮",
    "有40个答案选项，第一行(十个选项)对应第一个空格，以此类推",
    "如果没有选择特定书本，这程序默认只从[马太福音]提取经文做填充题",
    "点击程序顶部的按钮，可以改变经文提取范围",
    "点击[摩西五经]，点击[全选]，程序就会从这五本书提取经文",
    "想取消已经选择的书，就点击[不选]",
    "如果要从正本圣经随机提取经文，八个按钮都点击[全选]",
    "你可以缩小某书的经文提取范围，而不是整本书",
    "可以在[从第几章?]和[从第几章?]的格子填入数字",
    "如果填入的不是数字，程序会报错，闪退",
    "如果只是要从一章里面提取经文，两个格子都填同一个数",
    "4个绿色格子是答案栏，它们会显示您的选择",
    "通过[指定字节]可以缩小经文提取范围，仅选择有这关键词的经文",
    "有输入法问题的，需要从其他文本复制，然后粘贴进来",
    "[指定字节]中可以填写\"耶稣\"，不包括\"符号，程序只提取有\"耶稣\"的经文",
    "[指定字节]中有输入的时候，限制书范围是无效的",
    "不要在[指定字节]中输入空格",
    "欢迎反馈：elijahlaukokchai@hotmail.com",
    "愿上帝赐福你"]

class MyGrid(Widget):
    global slt1, slt2, slt3, slt4, chapno, bookno, versno, bookname
#    spi1 = ObjectProperty(None)
    ans1 = ObjectProperty(None)
    ans2 = ObjectProperty(None)
    ans3 = ObjectProperty(None)
    ans4 = ObjectProperty(None)
    inst = ObjectProperty(None)
    rev = ObjectProperty(None)
    qverse = ObjectProperty(None)
    qverse = qverse
    answer = answer


    def restart(self):
        global verse, bookno, bookname, qverse, ansind10, ansind20, ansind30, ansind40
        global ansclick, booksltfn, ansloc1, slt1, slt2, slt3, slt4, runnum
        #global spi1, spi2, spi3, spi4, spi5, spi6, spi7, spi8
        #print("-1 restart func. BEFORE reset, self.spi.text", self.spi1.text)
        #print("-1 restart func. BEFORE reset, self.spi", self.spi1)
        booksltfn = 40
        ansclick = 0
        bookslt1= []
        print("-003 RESTART FUNC  self", self)
        print("-003 RESTART FUNC  self.spi1", self.spi1)
        print("-003 RESTART FUNC  MyApp.spi1.text", self.spi1.text)

        if self.spi1.text == '(不选)':
            self.spi1.text = '摩西五经'
            self.spi1.outline_color = (0.1, 0.1, 0.1)
        elif self.spi1.text == '摩西五经':
            pass
        elif self.spi1.text == '(全选)':
            self.spi1.text = '(全选)'
            bookslt1 = [1, 2, 3, 4, 5]
            self.spi1.outline_color= (0, 0, 1)
        else:
            self.spi1.outline_color= (0, 0.3, 0)
            print("-001 RESTART FUNC  MyApp.spi1.spi1txt", self.spi1.text)
            spi1 = self.spi1.text
            bookslt1 = [bookdict[spi1]]
        print("000 RESTART FUNC MyApp.spi1   :", self.spi1)
        print("000 RESTART FUNC MyApp.spi1.spi1txt   :", self.spi1.text)
        spislt1 = self.spi1.text

        bookslt2= []
        if self.spi2.text == '(不选)':
            self.spi2.text = '历史书'
        elif self.spi2.text == '历史书':
            pass
        elif self.spi2.text == '(全选)':
            bookslt2 = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
            self.spi2.outline_color = (0.0, 0.5, 0.5, 1)
        else:
            self.spi2.outline_color = (0.0, 0.5, 0.5, 1)
            spi2 = self.spi2.text
            print("spi2 is : ", spi2)
            print("-01 RESTART FUNC  MyApp.spi2.spi2txt", self.spi2.text)
            bookslt2 = [bookdict[spi2]]
        spislt2 = self.spi2.text

        bookslt3= []
        if self.spi3.text == '(不选)':
            self.spi3.text = '诗歌智慧'
        elif self.spi3.text == '诗歌智慧':
            pass
        elif self.spi3.text == '(全选)':
            bookslt3 = [18, 19, 20, 21, 22]
        else:
            spi3 = self.spi3.text
            print("spi3 is : ", spi3)
            bookslt3 = [bookdict[spi3]]
        spislt3 = self.spi3.text

        bookslt4= []
        if self.spi4.text == '(不选)':
            self.spi4.text = '大先知书'
        elif self.spi4.text == '大先知书':
            pass
        elif self.spi4.text == '(全选)':
            bookslt4 = [23, 24, 25, 26, 27]
        else:
            spi4 = self.spi4.text
            print("spi4 is : ", spi4)
            bookslt4 = [bookdict[spi4]]
        spislt4 = self.spi4.text


        bookslt5= []
        if self.spi5.text == '(不选)':
            self.spi5.text = '小先知书'
        elif self.spi5.text == '小先知书':
            pass
        elif self.spi5.text == '(全选)':
            bookslt5 = [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
        else:
            spi5 = self.spi5.text
            print("spi5 is : ", spi5)
            bookslt5 = [bookdict[spi5]]
        spislt5 = self.spi5.text

        bookslt6 = []
        if self.spi6.text == '(不选)':
            self.spi6.text = '福音.历史'
        elif self.spi6.text == '福音.历史':
            pass
        elif self.spi6.text == '(全选)':
            bookslt6 = [40, 41, 42, 43, 44]
        else:
            spi6 = self.spi6.text
            print("spi6 is : ", spi6)
            bookslt6 = [bookdict[spi6]]
        spislt6 = self.spi6.text

        bookslt7 = []
        if self.spi7.text == '(不选)':
            self.spi7.text = '保罗书信'
        elif self.spi7.text == '保罗书信':
            pass
        elif self.spi7.text == '(全选)':
            bookslt7 = [45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57]
        else:
            spi7 = self.spi7.text
            print("spi7 is : ", spi7)
            bookslt7 = [bookdict[spi7]]
        spislt7 = self.spi7.text

        bookslt8 = []
        if self.spi8.text == '(不选)':
            self.spi8.text = '其他启示'
        elif self.spi8.text == '其他启示':
            pass
        elif self.spi8.text == '(全选)':
            bookslt8 = [58, 59, 60, 61, 62, 63, 64, 65, 66]
        else:
            spi8 = self.spi8.text
            print("spi8 is : ", spi8)
            bookslt8 = [bookdict[spi8]]
        spislt8 = self.spi8.text

        print("bookslt1234 is : ", bookslt1, bookslt2, bookslt3)
        bookcho = []
        bookcho = bookslt1 + bookslt2 + bookslt3 + bookslt4 + bookslt5 + bookslt6 + bookslt7 + bookslt8
        print("booklist is : ", bookcho)
        random.shuffle(bookcho)
        if len(bookcho)== 0:
            booksltfn = 40
        else:
            booksltfn = int(bookcho[0])
        print("0 RESTART FUNC  booksltfn:", booksltfn)
        print("00 RESTART CHAP self.chapstart.text", self.chapstart.text)
        bookname = call_book_name(booksltfn)
        print("***00 RESTART FUNC Bookname : ", bookname)
        chapstartraw = self.chapstart.text
        chapendraw = self.chapend.text
        if ((chapstartraw == "") or (chapendraw == "")) and chapmax[bookname] != 1:
            chapsltfn = random.randint(1, int(chapmax[bookname]))
            print("010 RESTART FUNC chapsltfn chapsltfn chapsltfn", chapsltfn)
            chapstartraw = ""
            chapendraw = ""
        else:
            chapstartint = int(chapstartraw)
            chapendint = int(chapendraw)
            if chapstartint == chapendint:
                chapsltfn = chapstartint
            else:
                chapsltfn = random.randint(chapstartint, chapendint)

        lookforraw = self.lookfor.text

        self.clear_widgets()

        # reset verse, if LOOKFOR is TRUE, priority to use LOOKFOR
        verse = "-"
        while verse == "-":
            if lookforraw != "":  # if LOOKFOR is True
                resultlk = pick_lookfor_verse(lookforraw) # return myverse, verse, bookno, chapno, versno
                verse = resultlk[1]
                bookno = resultlk[2]
                chapno = resultlk[3]
                versno = resultlk[4]
                bookname = call_book_name(bookno)
                print("RESTART FUNC WHILE LOOK looforraw :", lookforraw)
                print("RESTART FUNC WHILE LOOK resultlk :", resultlk)
            else:  # if LOOKFOR is FALSE
                result = pick_rand_verse(booksltfn, chapsltfn)
                verse = result[1]  # return myverse, verse, bookno, chapno, versno
                bookno = result[2]
                chapno = result[3]
                versno = result[4]
                print("RESTART FUNC WHILE ELSE booksltfn :", booksltfn)
                print("RESTART FUNC WHILE ELSE chapsltfn :", chapsltfn)
                bookname = call_book_name(bookno)


        print("2 restart func verse", verse)
        qverse_ansloc1 = make_qverse(verse, bookname, chapno, versno)  # return qverse, ansloc1
        qverse = qverse_ansloc1[0]
        ansloc1 = qverse_ansloc1[1]
        print("3 restart func qverse", qverse)
        ansind10 = random.randint(1, 10)
        print("3.1 ansind10 is : ", ansind10)
        ansind20 = random.randint(11, 20)
        ansind30 = random.randint(21, 30)
        ansind40 = random.randint(31, 40)
        print("4 restart func. bookname", bookname)
        qverse = make_qverse(verse, bookname, chapno, versno)[0]  # return qverse, ansloc1
        print("5 restart func. qverse", qverse)
        anschar10 = verse[ansloc1 + 0]  # anschar is a single char, anchar10 is the first char
        anschar20 = verse[ansloc1 + 1]  # anchar can be a symbol ， 。 ； ：
        anschar30 = verse[ansloc1 + 2]
        anschar40 = verse[ansloc1 + 3]
        anschar1234 = anschar10 + anschar20 + anschar30 + anschar40
        print("5.1 restart func. anschar1234,10,20,30,40  :", anschar1234, anschar10, anschar20, anschar30, anschar40)
        answer = "答案"
        sugg = make_sugg()
        suggfn = make_suggfn(sugg)[0]
        MyApp.qverse = qverse
        MyApp.chapstart = chapstartraw
        MyApp.chapend = chapendraw
        MyApp.lookfor = lookforraw
        MyApp.spi1 = spislt1
        MyApp.spi2 = spislt2
        MyApp.spi3 = spislt3
        MyApp.spi4 = spislt4
        MyApp.spi5 = spislt5
        MyApp.spi6 = spislt6
        MyApp.spi7 = spislt7
        MyApp.spi8 = spislt8
        MyApp.btn1 = suggfn[0]
        MyApp.btn2 = suggfn[1]
        MyApp.btn3 = suggfn[2]
        MyApp.btn4 = suggfn[3]
        MyApp.btn5 = suggfn[4]
        MyApp.btn6 = suggfn[5]
        MyApp.btn7 = suggfn[6]
        MyApp.btn8 = suggfn[7]
        MyApp.btn9 = suggfn[8]
        MyApp.btn10 = suggfn[9]
        MyApp.btn11 = suggfn[10]
        MyApp.btn12 = suggfn[11]
        MyApp.btn13 = suggfn[12]
        MyApp.btn14 = suggfn[13]
        MyApp.btn15 = suggfn[14]
        MyApp.btn16 = suggfn[15]
        MyApp.btn17 = suggfn[16]
        MyApp.btn18 = suggfn[17]
        MyApp.btn19 = suggfn[18]
        MyApp.btn20 = suggfn[19]
        MyApp.btn21 = suggfn[20]
        MyApp.btn22 = suggfn[21]
        MyApp.btn23 = suggfn[22]
        MyApp.btn24 = suggfn[23]
        MyApp.btn25 = suggfn[24]
        MyApp.btn26 = suggfn[25]
        MyApp.btn27 = suggfn[26]
        MyApp.btn28 = suggfn[27]
        MyApp.btn29 = suggfn[28]
        MyApp.btn30 = suggfn[29]
        MyApp.btn31 = suggfn[30]
        MyApp.btn32 = suggfn[31]
        MyApp.btn33 = suggfn[32]
        MyApp.btn34 = suggfn[33]
        MyApp.btn35 = suggfn[34]
        MyApp.btn36 = suggfn[35]
        MyApp.btn37 = suggfn[36]
        MyApp.btn38 = suggfn[37]
        MyApp.btn39 = suggfn[38]
        MyApp.btn40 = suggfn[39]
        runnum = (runnum + 1) % 19
        MyApp.inst = messagelist[runnum]
        slt1 = 0
        slt2 = 0
        slt3 = 0
        slt4 = 0
#        MyApp.spi1.background_color = (0.9, 0.3, 1, 1)
#        MyApp.spi1.spi1txt = "0.9, 0.3, 1, 1"
        self.parent.add_widget(MyGrid())



        print("6 restart func. AFTER BUILD, MyApp.spi1", MyApp.spi1)
        print("----------------------------------------------------------------")
        return booksltfn, suggfn, ansind10, ansind20, ansind30, ansind40, ansclick, slt1, slt2, slt3, slt4



    def rev(self):
        global ansclick, anschar1234
        ansclick = ansclick + 1
        if ansclick == 1:
            anschar1234 = anschar10
        elif ansclick == 2:
            anschar1234 = anschar10 + anschar20
        elif ansclick == 3:
            anschar1234 = anschar10 + anschar20 + anschar30
        elif ansclick >= 4:
            anschar1234 = anschar10 + anschar20 + anschar30 + anschar40
        self.inst.text = anschar1234
        self.inst.font_size = 26
        self.inst.outline_color = (0, 0, 0.7)
        self.inst.outline_width = 2

    def submit(self):
        global slt1, slt2, slt3, slt4, ansind10, ansind20, ansind30, ansind40
        print("SUBMIT func: ansind10,20,30,40", ansind10, ansind20, ansind30, ansind40)
        print("SUBMIT func: slt 1,2,3,4:   ", slt1, slt2, slt3, slt4)
        if ((slt1 == ansind10) + (slt2 == ansind20) + (slt3 == ansind30) + (slt4 == ansind40)) == 4:
            # print("哇！答对了！")
            self.inst.text = "哇！答对了！"
            self.inst.font_size = 34
            self.inst.outline_color = (0.7, 0, 0)
            self.inst.outline_width = 2
        elif ((slt1 == ansind10) + (slt2 == ansind20) + (slt3 == ansind30) + (slt4 == ansind40)) == 3:
            # print("只差一个了！")
            self.inst.text = "只差一个了！"
            self.inst.font_size = 30
        elif ((slt1 == ansind10) + (slt2 == ansind20) + (slt3 == ansind30) + (slt4 == ansind40)) == 2:
            # print("不错，继续努力吧！")
            self.inst.text = "不错，继续努力吧！！"
            self.inst.font_size = 30
        elif ((slt1 == ansind10) + (slt2 == ansind20) + (slt3 == ansind30) + (slt4 == ansind40)) == 1:
            # print("只对一个，加油！")
            self.inst.text = "只对一个，加油！"
            self.inst.font_size = 30
        else:
            # print("太惨了…………全错了！")
            self.inst.text = "太惨了………全错了！"
            self.inst.font_size = 30


    def btn1(self):
        global slt1
        slt1 = 1
        self.ans1.text = suggfn[slt1 - 1]

    def btn2(self):
        global slt1
        slt1 = 2
        self.ans1.text = suggfn[slt1 - 1]

    def btn3(self):
        global slt1
        slt1 = 3
        self.ans1.text = suggfn[slt1 - 1]

    def btn4(self):
        global slt1
        slt1 = 4
        self.ans1.text = suggfn[slt1 - 1]

    def btn5(self):
        global slt1
        slt1 = 5
        self.ans1.text = suggfn[slt1 - 1]

    def btn6(self):
        global slt1
        slt1 = 6
        self.ans1.text = suggfn[slt1 - 1]

    def btn7(self):
        global slt1
        slt1 = 7
        self.ans1.text = suggfn[slt1 - 1]

    def btn8(self):
        global slt1
        slt1 = 8
        self.ans1.text = suggfn[slt1 - 1]

    def btn9(self):
        global slt1
        slt1 = 9
        self.ans1.text = suggfn[slt1 - 1]

    def btn10(self):
        global slt1
        slt1 = 10
        self.ans1.text = suggfn[slt1 - 1]

    def btn11(self):
        global slt2
        slt2 = 11
        self.ans2.text = suggfn[slt2 - 1]

    def btn12(self):
        global slt2
        slt2 = 12
        self.ans2.text = suggfn[slt2 - 1]

    def btn13(self):
        global slt2
        slt2 = 13
        self.ans2.text = suggfn[slt2 - 1]

    def btn14(self):
        global slt2
        slt2 = 14
        self.ans2.text = suggfn[slt2 - 1]

    def btn15(self):
        global slt2
        slt2 = 15
        self.ans2.text = suggfn[slt2 - 1]

    def btn16(self):
        global slt2
        slt2 = 16
        self.ans2.text = suggfn[slt2 - 1]

    def btn17(self):
        global slt2
        slt2 = 17
        self.ans2.text = suggfn[slt2 - 1]

    def btn18(self):
        global slt2
        slt2 = 18
        self.ans2.text = suggfn[slt2 - 1]

    def btn19(self):
        global slt2
        slt2 = 19
        self.ans2.text = suggfn[slt2 - 1]

    def btn20(self):
        global slt2
        slt2 = 20
        self.ans2.text = suggfn[slt2 - 1]

    def btn21(self):
        global slt3
        slt3 = 21
        self.ans3.text = suggfn[slt3 - 1]

    def btn22(self):
        global slt3
        slt3 = 22
        self.ans3.text = suggfn[slt3 - 1]

    def btn23(self):
        global slt3
        slt3 = 23
        self.ans3.text = suggfn[slt3 - 1]

    def btn24(self):
        global slt3
        slt3 = 24
        self.ans3.text = suggfn[slt3 - 1]

    def btn25(self):
        global slt3
        slt3 = 25
        self.ans3.text = suggfn[slt3 - 1]

    def btn26(self):
        global slt3
        slt3 = 26
        self.ans3.text = suggfn[slt3 - 1]

    def btn27(self):
        global slt3
        slt3 = 27
        self.ans3.text = suggfn[slt3 - 1]

    def btn28(self):
        global slt3
        slt3 = 28
        self.ans3.text = suggfn[slt3 - 1]

    def btn29(self):
        global slt3
        slt3 = 29
        self.ans3.text = suggfn[slt3 - 1]

    def btn30(self):
        global slt3
        slt3 = 30
        self.ans3.text = suggfn[slt3 - 1]

    def btn31(self):
        global slt4
        slt4 = 31
        self.ans4.text = suggfn[slt4 - 1]

    def btn32(self):
        global slt4
        slt4 = 32
        self.ans4.text = suggfn[slt4 - 1]

    def btn33(self):
        global slt4
        slt4 = 33
        self.ans4.text = suggfn[slt4 - 1]

    def btn34(self):
        global slt4
        slt4 = 34
        self.ans4.text = suggfn[slt4 - 1]

    def btn35(self):
        global slt4
        slt4 = 35
        self.ans4.text = suggfn[slt4 - 1]

    def btn36(self):
        global slt4
        slt4 = 36
        self.ans4.text = suggfn[slt4 - 1]

    def btn37(self):
        global slt4
        slt4 = 37
        self.ans4.text = suggfn[slt4 - 1]

    def btn38(self):
        global slt4
        slt4 = 38
        self.ans4.text = suggfn[slt4 - 1]

    def btn39(self):
        global slt4
        slt4 = 39
        self.ans4.text = suggfn[slt4 - 1]

    def btn40(self):
        global slt4
        slt4 = 40
        self.ans4.text = suggfn[slt4 - 1]

    def ansc1(self):
        global slt1
        # print("Name: ", self.ans1.text)
        self.ans1.text = ""
        slt1 = 0
        return slt1

    def ansc2(self):
        global slt2
        # print("Name: ", self.ans1.text)
        self.ans2.text = ""
        slt2 = 0
        return slt2

    def ansc3(self):
        global slt3
        # print("Name: ", self.ans1.text)
        self.ans3.text = ""
        slt3 = 0
        return slt3

    def ansc4(self):
        global slt4
        # print("Name: ", self.ans1.text)
        self.ans4.text = ""
        slt4 = 0
        return slt4


class MyApp(App):
    #    global qverse
    chapstart = str("")
    chapend = str("")
    lookfor = str("")
    qverse = qverse
    submit = str("提交")
    title = str("圣经经文填充")
    restart = str("再来一题")
    rev = str("显示答案")
    inst = str("第一次使用，可以点击再来一题看提示")
    spi1 = str("摩西五经")
    spi2 = str("历史书")
    spi3 = str("诗歌智慧")
    spi4 = str("大先知书")
    spi5 = str("小先知书")
    spi6 = str("福音.历史")
    spi7 = str("保罗书信")
    spi8 = str("其他启示")
    btn1 = suggfn[0]
    btn2 = suggfn[1]
    btn3 = suggfn[2]
    btn4 = suggfn[3]
    btn5 = suggfn[4]
    btn6 = suggfn[5]
    btn7 = suggfn[6]
    btn8 = suggfn[7]
    btn9 = suggfn[8]
    btn10 = suggfn[9]
    btn11 = suggfn[10]
    btn12 = suggfn[11]
    btn13 = suggfn[12]
    btn14 = suggfn[13]
    btn15 = suggfn[14]
    btn16 = suggfn[15]
    btn17 = suggfn[16]
    btn18 = suggfn[17]
    btn19 = suggfn[18]
    btn20 = suggfn[19]
    btn21 = suggfn[20]
    btn22 = suggfn[21]
    btn23 = suggfn[22]
    btn24 = suggfn[23]
    btn25 = suggfn[24]
    btn26 = suggfn[25]
    btn27 = suggfn[26]
    btn28 = suggfn[27]
    btn29 = suggfn[28]
    btn30 = suggfn[29]
    btn31 = suggfn[30]
    btn32 = suggfn[31]
    btn33 = suggfn[32]
    btn34 = suggfn[33]
    btn35 = suggfn[34]
    btn36 = suggfn[35]
    btn37 = suggfn[36]
    btn38 = suggfn[37]
    btn39 = suggfn[38]
    btn40 = suggfn[39]

    def build(self):
        # img = Image(source="cross.jpg")
        #        img = AsyncImage(source="cross.jpg")
        #        value = TextInput(text="Enter Book Number Here")
        #        time.sleep(5)
        return MyGrid()


# print("zz")
if __name__ == "__main__":
    MyApp().run()
# print("final repicked bookno is :", bookno)
# print("final repicked chapno is :", chapno)
# print("final repicked versno is :", versno)
# print("final repicked verse is :", verse)
