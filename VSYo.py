import sqlite3
import pygame, sys
import ctypes 
import random
import os
import sys
from PIL import Image
import time as systime
from time import ctime as stime

## Функция импортирования картинки
def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Не удаётся загрузить:', name)
        raise SystemExit(message)
    if name.split('.')[1] == "png":
        image = image.convert_alpha()
        if color_key is not None:
            if color_key is -1:
                color_key = image.get_at((0, 0))
            image.set_colorkey(color_key)
    return image

## Функция загрузки игры
def loading():
    for i in range(100):
        systime.sleep(0.01)
        screen.blit(load_image("zagryzka.png"), (0, 0))
        pygame.draw.rect(screen, (0, 255, 0), (300, 500, 3 * i, 75), 0)
        pygame.draw.rect(screen, (255, 255, 255), (300, 500, 300, 75), 6)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
    screen.fill((255, 255, 255))
    return True


pygame.init()
size = width, height = 900, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
screen.fill(pygame.Color('white'))

months = {"Jan": 0, "Feb": 31, "Mar": 59, "Apr": 90, "May": 120, "Jun": 151,
          "Jul": 181, "Aug": 212, "Sep": 243, "Oct": 273, "Nov": 303, "Dec": 334,
          }

cvit_1 = 9
cvit_2 = 5
cvit_3 = 3
cpis_Ordinary_2 = ['LB - 510', 'BP - 120', 'MP - 420', 'FM - 340', 'FB - 310', 'MB - 410', 
                   'LF - 530', 'LP - 520', 'PF - 230']
cpis_Ordinary_3 = ['BPF - 1230']
cpis_Rare_2 = ['FE - 370', 'GB - 610', 'EB - 710', 'BE - 170', 'GL - 650', 'GM - 640', 
               'FG - 360', 'EP - 720', 'EM - 740', 'EG - 760']
cpis_Rare_3 = ['BLE - 1570', 'EBP - 7120', 'LEF - 5730', 'MEB - 4710', 'PGL - 2650',
               'GBF - 6130', 'GBL - 6150', 'FBE - 3170']
cpis_Rare_4 = ['MPLE - 42570', 'GBFL - 61350']
cpis_Epic_2 = ['AG - 860', 'AE - 870']
cpis_Epic_3 = ['MEG - 4760', 'GBA - 6180', 'LBA - 5180', 'MFG - 3460', 'LGE - 5670']
cpis_Epic_4 = ['BGEA - 16780', 'PFME - 23470', 'BMEA - 14780']
cpis_Legendary_2 = ['AZ - 890']
cpis_Legendary_3 = ['AEG - 9760', 'LEZ - 5790', 'MGZ - 4690']
cpis_Legendary_4 = ['FMGA - 34680', 'LGEA - 56780', 'BPLE - 12570', 'MFAZ - 34890', 'PFLE - 23570',
                    'BPAZ - 12890']
clovar_fight = {
"Удар кулаком": 100, 
"Бросок": 300,
"Подсечка": 400,
"Режим Ярость": 700,
"Гроза": 500,
"Шторм": 800, 
"Цунами": 1200,
"Угреродная бомба": 550,
"Токсичные бутылки": 850,
"Бомба из LEGO": 1250,
"Удар катаной": 600,
"Бензопила": 900,
"Сюрикены": 1300,
"Завезти Запорожец": 650,
"Взрывные машинки": 950,
"Беспилотники": 1350,
"Лазерная сеть": 700,
"Ультралуч": 950,
"Джедайский меч": 1400,
"Магнитная буря": 850,
"Смена полярности": 1150,
"Магнитное поле": 1450,
"Молния": 900,
"Взрыв ЭС": 1200,
"Луч Теслы": 1500,
"Война": 950,
"Генезис": 1250,
"Эра Альтрона": 1550,
"Удар частицами": 1000,
"Искажение пространства": 1300,
"Черная дыра": 1600
}

cpis_buy_robot = ['PF - 230', 'MB - 410', 'BPF - 1230', 'EB - 710', 'BLE - 1570', 
            'GBF - 6130', 'MEB - 4710', 'FBE - 3170', 'GBFL - 61350', 'AG - 860', 'MEG - 4760', 
            'BGEA - 16780', 'BMEA - 14780', 'ZA - 980', 'AEG - 9760', 'LEZ - 5790', 
            'MGZ - 4690', 'FMGA - 34680', 'BPLE - 12570', 'MFAZ - 34890', 'BPAZ - 12890']   

clovar_krit = {
"Удар кулаком": 'Z', 
"Бросок": 'Z',
"Подсечка": 'Z',
"Режим Ярость": 'Z',
"Гроза": 'L',
"Шторм": 'L', 
"Цунами": 'L',
"Угреродная бомба": 'G',
"Токсичные бутылки": 'G',
"Бомба из LEGO": 'G',
"Удар катаной": 'M',
"Бензопила": 'M',
"Сюрикены": 'M',
"Завезти Запорожец": 'E',
"Взрывные машинки": 'E',
"Беспилотники": 'E',
"Лазерная сеть": 'P',
"Ультралуч": 'P',
"Джедайский меч": 'P',
"Магнитная буря": 'F',
"Смена полярности": 'F',
"Магнитное поле": 'F',
"Молния": 'B',
"Взрыв ЭС": 'B',
"Луч Теслы": 'B',
"Война": ' ',
"Генезис": ' ',
"Эра Альтрона": ' ',
"Удар частицами": 'A',
"Искажение пространства": 'A',
"Черная дыра": 'A'
}

clovar_pobot = {
'LB - 510': ['Удар кулаком', 'Лазерная сеть', 'Бросок', 'Шторм'],
'BP - 120': ['Удар кулаком', 'Гроза', 'Бросок', 'Токсичные бутылки'],
'MP - 420': ['Удар кулаком', 'Завезти Запорожец', 'Бросок', 'Токсичные бутылки'],
'FM - 340': ['Удар кулаком', 'Удар катаной', 'Бросок', 'Взрывные машинки'],
'FB - 310': ['Удар кулаком', 'Удар катаной', 'Бросок', 'Токсичные бутылки'],
'MB - 410': ['Удар кулаком', 'Гроза', 'Бросок', 'Взрывные машинки'],
'LF - 530': ['Удар кулаком', 'Лазерная сеть', 'Бросок', 'Удар катаной'],
'LP - 520': ['Удар кулаком', 'Токсичные бутылки', 'Бросок', 'Ультралуч'],
'PF - 230': ['Удар кулаком', 'Угреродная бомба', 'Бросок', 'Бензопила'],
'BPF - 1230': ['Бросок', 'Шторм', 'Бомба из LEGO', 'Бензопила'],
'FE - 370': ['Бросок', 'Бензопила', 'Подсечка', 'Молния'],
'GB - 610': ['Бросок', 'Магнитная буря', 'Подсечка', 'Шторм'],
'EB - 710': ['Бросок', 'Молния', 'Подсечка', 'Шторм'],
'BE - 170': ['Бросок', 'Гроза', 'Подсечка', 'Взрыв ЭС'],
'GL - 650': ['Бросок', 'Смена полярности', 'Подсечка', 'Лазерная сеть'],
'GM - 640': ['Бросок', 'Магнитная буря', 'Подсечка', 'Взрывные машинки'],
'FG - 360': ['Бросок', 'Удар катаной', 'Подсечка', 'Смена полярности'],
'EP - 720': ['Бросок', 'Взрыв ЭС', 'Подсечка', 'Угреродная бомба'],
'EM - 740': ['Бросок', 'Молния', 'Подсечка', 'Взрывные машинки'],
'EG - 760': ['Бросок', 'Взрыв ЭС', 'Подсечка', 'Смена полярности'],
'BLE - 1570': ['Подсечка', 'Гроза', 'Ультралуч', 'Взрыв ЭС'],
'EBP - 7120': ['Подсечка', 'Молния', 'Цунами', 'Токсичные бутылки'],
'LEF - 5730': ['Подсечка', 'Ультралуч', 'Бензопила', 'Взрыв ЭС'],
'MEB - 4710': ['Подсечка', 'Взрывные машинки', 'Шторм', 'Молния'],
'PGL - 2650': ['Подсечка', 'Угреродная бомба', 'Смена полярности', 'Ультралуч'],
'GBF - 6130': ['Подсечка', 'Магнитная буря', 'Шторм', 'Бензопила'],
'GBL - 6150': ['Подсечка', 'Смена полярности', 'Гроза', 'Ультралуч'],
'FBE - 3170': ['Подсечка', 'Удар катаной', 'Шторм', 'Взрыв ЭС'],
'MPLE - 42570': ['Беспилотники', 'Токсичные бутылки', 'Ультралуч', 'Молния'],
'GBFL - 61350': ['Магнитная буря', 'Шторм', 'Бензопила', 'Лазерная сеть'],
'AG - 860': ['Бросок', 'Война', 'Подсечка', 'Магнитное поле'],
'AE - 870': ['Бросок', 'Война', 'Подсечка', 'Взрыв ЭС'],
'MEG - 4760': ['Подсечка', 'Взрывные машинки', 'Взрыв ЭС', 'Смена полярности'],
'GBA - 6180': ['Подсечка', 'Магнитная буря', 'Цунами', 'Генезис'],
'LBA - 5180': ['Подсечка', 'Джедайский меч', 'Шторм', 'Генезис'],
'MFG - 3460': ['Подсечка', 'Беспилотники', 'Смена полярности', 'Бензопила'],
'LGE - 5670': ['Подсечка', 'Ультралуч', 'Магнитное поле', 'Луч Теслы'],
'BGEA - 16780': ['Шторм', 'Смена полярности', 'Луч Теслы', 'Война'],
'PFME - 23470': ['Токсичные бутылки', 'Сюрикены', 'Беспилотники', 'Взрыв ЭС'],
'BMEA - 14780': ['Цунами', 'Взрывные машинки', 'Луч Теслы', 'Генезис'],
'ZA - 980': ['Подсечка', 'Эра Альтрона', 'Режим Ярость', 'Искажение пространства'],
'AEG - 9760': ['Режим Ярость', 'Эра Альтрона', 'Взрыв ЭС', 'Магнитное поле'],
'LEZ - 5790': ['Режим Ярость', 'Луч Теслы', 'Ультралуч', 'Удар частицами'],
'MGZ - 4690': ['Режим Ярость', 'Беспилотники', 'Магнитное поле', 'Искажение пространства'],
'FMGA - 34680': ['Сюрикены', 'Беспилотники', 'Смена полярности', 'Эра Альтрона'],
'LGEA - 56780': ['Джедайский меч', 'Магнитное поле', 'Взрыв ЭС', 'Генезис'],
'BPLE - 12570': ['Цунами', 'Бомба из LEGO', 'Джедайский меч', 'Искажение пространства'],
'MFAZ - 34890': ['Сюрикены', 'Беспилотники', 'Эра Альтрона', 'Искажение пространства'],
'PFLE - 23570': ['Токсичные бутылки', 'Сюрикены', 'Джедайский меч', 'Взрыв ЭС'],
'BPAZ - 12890': ['Шторм', 'Бомба из LEGO', 'Эра Альтрона', 'Черная дыра']
}
con = sqlite3.connect("robot.db")
cur = con.cursor() 
arena = cur.execute("""SELECT arena FROM resources""").fetchall()   
arena = arena[0][0]
ups = False
nach = 0
konech = 2
zoloto = 1000000000
magazin_l_r = 0
magaz = False
vub = False
boy = False
compani = False
priz = False
sklad = False
screen_ocnov = True
mail = False
mail_up_down = 0
sklad_left_right = 0
running = loading()
sprites_screens = 1
cpis_rarity = ['Ordinary', 'Ordinary', 'Ordinary', 'Rare', 'Rare', 'Rare', 
               'Rare', 'Rare', 'Rare', 'Epic', 'Epic', 'Epic', 'Epic', 'Legendary',
               'Legendary', 'Legendary', 'Legendary', 'Legendary', 'Legendary', 'Legendary', 'Legendary']
cpis_buy_zoloto = [1000000, 3000000, 5000000, 10000000, 20000000, 100000000, 500000000,
                   700000000, 900000000]
cpis_buy_gem = [100, 300, 700, 1000, 1500, 3000, 10000, 17000, 25000, 40000, 50000, 99000]
# база
def magaz_buy():
    con = sqlite3.connect("robot.db")
    cur = con.cursor()    
    global magazin_l_r
    not_none = False
    if magazin_l_r < 10:
        if zoloto >= cpis_buy_zoloto[magazin_l_r - 1]:
            robot = cpis_buy_robot[magazin_l_r - 1]
            rarity = cpis_rarity[magazin_l_r - 1]
            not_none = True
    else:
        if gem >= cpis_buy_gem[magazin_l_r - 10]:
            not_none = True
            robot = cpis_buy_robot[magazin_l_r - 1]
            rarity = cpis_rarity[magazin_l_r - 1]
    if not_none:
        cur.execute("""INSERT INTO robot(name, lvl, rarity, hp) VALUES(?, 1, ?, 2500)""", (robot, rarity)).fetchall()
    con.commit()
    con.close() 

def draw_image(name, scale, position):
    image = pygame.image.load(name).convert()
    image = pygame.transform.scale(image, scale)
    screen.blit(image, position)

def draw_rec(name, scale, position):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    image = pygame.transform.scale(image, scale)
    screen.blit(image, position)
 
def draw_robot(name, scale, position):
    fullname = os.path.join('Роботы', name)
    image = pygame.image.load(fullname)
    image = pygame.transform.scale(image, scale)
    screen.blit(image, position)

def draw_robot_2(name, scale, position):
    fullname = os.path.join('Роботы', name)
    image = pygame.image.load(fullname)
    image = pygame.transform.scale(image, scale)
    image = pygame.transform.flip(image, 1, 0)
    screen.blit(image, position)

def otzilcal(image):
    image = pygame.image.load(image)
    image =  pygame.transform.scale(image, (-1, 1))    
    return image
    
def sprite_screen():
    draw_image("robot_prob.png", (200, 300), (100, 100))

def magazin():
    global sen1, sen2, sen3
    f = pygame.font.Font(None, 40)
    draw_image("mazin.png", size, (0, 0))
    if magazin_l_r < 4:
        sen1 = 1000000
        sen2 = 3000000
        sen3 = 5000000
        draw_rec("gold.png", (50, 50), (65, 490))
        draw_rec("gold.png", (50, 50), (330, 490))
        draw_rec("gold.png", (50, 50), (625, 490))
        draw_robot("PF - 230.png", (250, 351), (50, 100))
        draw_robot("MB - 410.png", (250, 351), (330, 100))
        draw_robot("BPF - 1230.png", (250, 351), (610, 100))
        text = f.render('1M', 1, pygame.Color('yellow'))
        screen.blit(text, (120, 500))  
        text = f.render('3M', 1, pygame.Color('yellow'))
        screen.blit(text, (390, 500))  
        text = f.render('5M', 1, pygame.Color('yellow'))
        screen.blit(text, (680, 500))
    elif magazin_l_r < 7:
        sen1 = 10000000
        sen2 = 20000000
        sen3 = 100000000
        draw_rec("gold.png", (50, 50), (65, 490))
        draw_rec("gold.png", (50, 50), (330, 490))
        draw_rec("gold.png", (50, 50), (625, 490))
        draw_robot("EB - 710.png", (250, 351), (50, 100))
        draw_robot("BLE - 1570.png", (250, 351), (330, 100))
        draw_robot("GBF - 6130.png", (250, 351), (610, 100))
        text = f.render('10M', 1, pygame.Color('yellow'))
        screen.blit(text, (120, 500))  
        text = f.render('20M', 1, pygame.Color('yellow'))
        screen.blit(text, (390, 500))  
        text = f.render('100M', 1, pygame.Color('yellow'))
        screen.blit(text, (680, 500))
    elif magazin_l_r < 10:
        sen1 = 500000000
        sen2 = 700000000
        sen3 = 900000000
        draw_rec("gold.png", (50, 50), (65, 490))
        draw_rec("gold.png", (55, 50), (330, 490))
        draw_rec("gold.png", (50, 50), (625, 490))
        draw_robot("MEB - 4710.png", (250, 351), (50, 100))
        draw_robot("FBE - 3170.png", (250, 351), (330, 100))
        draw_robot("GBFL - 61350.png", (250, 351), (610, 100))
        text = f.render('500M', 1, pygame.Color('yellow'))
        screen.blit(text, (120, 500))  
        text = f.render('700M', 1, pygame.Color('yellow'))
        screen.blit(text, (390, 500))  
        text = f.render('900M', 1, pygame.Color('yellow'))
        screen.blit(text, (680, 500))
    elif magazin_l_r < 13:
        sen1 = 100
        sen2 = 300
        sen3 = 700
        draw_rec("almaz.png", (55, 50), (65, 490))
        draw_rec("almaz.png", (55, 50), (330, 490))
        draw_rec("almaz.png", (55, 50), (625, 490))
        draw_robot("AG - 860.png", (250, 351), (50, 100))
        draw_robot("MEG - 4760.png", (250, 351), (330, 100))
        draw_robot("BGEA - 16780.png", (250, 351), (610, 100))
        text = f.render('100', 1, pygame.Color('blue'))
        screen.blit(text, (125, 500))  
        text = f.render('300', 1, pygame.Color('blue'))
        screen.blit(text, (395, 500))  
        text = f.render('700', 1, pygame.Color('blue'))
        screen.blit(text, (685, 500))
    elif magazin_l_r < 16:
        sen1 = 1000
        sen2 = 1500
        sen3 = 3000     
        draw_rec("almaz.png", (55, 50), (65, 490))
        draw_rec("almaz.png", (55, 50), (330, 490))
        draw_rec("almaz.png", (55, 50), (625, 490))
        draw_robot("BMEA - 14780.png", (250, 351), (50, 100))
        draw_robot("ZA - 980.png", (250, 351), (330, 100))
        draw_robot("AEG - 9760.png", (250, 351), (610, 100))
        text = f.render('1K', 1, pygame.Color('blue'))
        screen.blit(text, (125, 500))  
        text = f.render('1.5K', 1, pygame.Color('blue'))
        screen.blit(text, (395, 500))  
        text = f.render('3K', 1, pygame.Color('blue'))
        screen.blit(text, (685, 500))    
    elif magazin_l_r < 19:
        sen1 = 10000
        sen2 = 17000
        sen3 = 25000
        draw_rec("almaz.png", (55, 50), (65, 490))
        draw_rec("almaz.png", (55, 50), (330, 490))
        draw_rec("almaz.png", (55, 50), (625, 490))
        draw_robot("LEZ - 5790.png", (250, 351), (50, 100))
        draw_robot("MGZ - 4690.png", (250, 351), (330, 100))
        draw_robot("FMGA - 34680.png", (250, 351), (610, 100))
        text = f.render('10K', 1, pygame.Color('blue'))
        screen.blit(text, (125, 500))  
        text = f.render('17K', 1, pygame.Color('blue'))
        screen.blit(text, (395, 500))  
        text = f.render('25K', 1, pygame.Color('blue'))
        screen.blit(text, (685, 500))    
    elif magazin_l_r < 22:
        sen1 = 40000
        sen2 = 50000
        sen3 = 99000
        draw_rec("almaz.png", (55, 50), (65, 490))
        draw_rec("almaz.png", (55, 50), (330, 490))
        draw_rec("almaz.png", (55, 50), (625, 490))
        draw_robot("BPLE - 12570.png", (250, 351), (50, 100))
        draw_robot("MFAZ - 34890.png", (250, 351), (330, 100))
        draw_robot("BPAZ - 12890.png", (250, 351), (610, 100))
        text = f.render('40K', 1, pygame.Color('blue'))
        screen.blit(text, (125, 500))  
        text = f.render('50K', 1, pygame.Color('blue'))
        screen.blit(text, (395, 500))  
        text = f.render('99K', 1, pygame.Color('blue'))
        screen.blit(text, (685, 500))       
    if magazin_l_r % 3 == 1:
        draw_rec("magazin_button.png", (220, 60), (60, 485))
    elif magazin_l_r % 3 == 2:
        draw_rec("magazin_button.png", (236, 61), (328, 485))    
    elif magazin_l_r % 3 == 0 and magazin_l_r != 0:
        draw_rec("magazin_button.png", (218, 61), (620, 485))      

def sklads():
    global sklad_left_right, nach, konech
    draw_image('sklad.png', size, (0, 0))
    con = sqlite3.connect("robot.db")
    cur = con.cursor()
    kolvo = cur.execute("""SELECT COUNT(id) FROM robot""").fetchall()   
    cpis_robotov = cur.execute("""SELECT name FROM robot""").fetchall()
    x = 270
    now = 0
    if kolvo[0][0] != 0:
        now = (sklad_left_right + 1) // 2
        now *= 2
        if kolvo[0][0] >= 1 and now == 0:
            now = 2
    if kolvo[0][0] >= 1:
        if now > kolvo[0][0]:
            now = kolvo[0][0]
            for i in cpis_robotov[now - 1:now]:
                name = i[0] + '.png'
                draw_robot(name, (250, 351), (x, 120))
                x += 300
        else:
            for i in cpis_robotov[now - 2:now]:
                name = i[0] + '.png'
                draw_robot(name, (250, 351), (x, 120))
                x += 300            
    con.commit()
    con.close()     

def slad_r_l(number):
    con = sqlite3.connect("robot.db")
    if number % 2 == 0:
        draw_rec('sklad_button.png', (200, 50), (560, 500))
    elif number == 0:
        sklads()
    elif number % 2 != 0 and number != 0:          
        draw_rec('sklad_button.png', (200, 50), (260, 500))
                    
def mails():
    draw_image('mail.png', (width - 200, height - 200), (100, 100))
    con = sqlite3.connect("robot.db")
    cur = con.cursor()
    kolvo = cur.execute("""SELECT COUNT(id) FROM mail""").fetchall()
    x = 143
    y = 140
    if kolvo[0][0] > 3:
        draw = 3
        stranic = kolvo[0][0] // 3
        if kolvo[0][0] % 3 != 0:
            stranic += 1
    else:
        draw = kolvo[0][0]
        stranic = 1
    now = mail_up_down // 3
    if mail_up_down % 3 != 0:
        now += 1
    if now == 0:
        now = 1
    if now == stranic:
        draw = kolvo[0][0] % 3
        if draw == 0:
            if kolvo[0][0] == 0:
                draw = 0
            else:
                draw = 3
        for i in range(draw):
            draw_image("mailpismo.png", (270, 100), (x, y))
            y += 110           
    else:
        for i in range(draw):
            draw_image("mailpismo.png", (270, 100), (x, y))
            y += 110
    stran = (str(now) + '/' + str(stranic))
    f = pygame.font.Font(None, 30)
    stran = f.render(stran, 1, pygame.Color('white'))
    screen.blit(stran, (100, 480))    
    con.commit()
    con.close()    
    
def mail_append(text, prize):
    con = sqlite3.connect("robot.db")
    cur = con.cursor()
    cur.execute("""INSERT INTO mail(text, prize) VALUES(?, ?)""", (text, prize)).fetchall()
    con.commit()
    con.close()    
    
def mail_del(ids):
    con = sqlite3.connect("robot.db")
    cur = con.cursor()
    id_mail = cur.execute("""SELECT id FROM mail""").fetchall()
    print(id_mail[ids - 1][0])
    prize = cur.execute("""SELECT prize FROM mail where id = ?""", (id_mail[ids - 1][0],)).fetchall() 
    cur.execute("""DELETE from mail where id = ?""", (id_mail[ids - 1][0],)).fetchall()
    cur.execute("""INSERT INTO sklad(object) VALUES(?)""", (prize[0])).fetchall()
    con.commit()
    con.close()    
    global mail_up_down
    mail_up_down = 0
    

def mail_uping_downing(number):
    if number % 3 == 1:
        draw_image("mailpismoup_down.png", (5, 75), (117, 150))
    elif number % 3 == 2:
        draw_image("mailpismoup_down.png", (5, 75), (117, 255))
    else:
        draw_image("mailpismoup_down.png", (5, 75), (117, 360))
    con = sqlite3.connect("robot.db")
    cur = con.cursor()
    texts = cur.execute("""SELECT text FROM mail""").fetchall()  
    prizes = cur.execute("""SELECT prize FROM mail""").fetchall()  
    if texts != []:
        f = pygame.font.Font(None, 24)
        text = texts[number - 1][0]
        prize = prizes[number - 1][0]
        text = f.render(text, 1, pygame.Color('black'))    
        prize = f.render(prize, 1, pygame.Color('black'))
        screen.blit(text, (470, 150))    
        screen.blit(prize, (570, 250))
    con.commit()
    con.close()     

def Compani(name):
    global Fight, compani, camp, chs, vub
    con = sqlite3.connect("robot.db")
    cur = con.cursor()
    vub = False
    camp = False
    chs = False
    compani = True 
    lvl = cur.execute("""SELECT lvl FROM robot WHERE name = ?""", (name,)).fetchall()
    hp = cur.execute("""SELECT hp FROM robot WHERE name = ?""", (name,)).fetchall()
    screen.fill(pygame.Color('white'))
    cpis1 = [name, lvl[0][0], hp[0][0]]
    name = cur.execute("""SELECT robot FROM arena WHERE id = ?""", (arena,)).fetchall()
    lvl = cur.execute("""SELECT lvl FROM arena WHERE id = ?""", (arena,)).fetchall()
    hp = cur.execute("""SELECT hp FROM arena WHERE id = ?""", (arena,)).fetchall()
    Fight = Fights(cpis1, [name[0][0], lvl[0][0], hp[0][0]])


class Fights:
    def __init__(self, cpis1, cpis2):
        self.name1 = cpis1[0]
        self.lvl1 = cpis1[1]
        self.hp1 = cpis1[2]
        self.cpis_at_1 = clovar_pobot[self.name1]
        self.name2 = cpis2[0]
        self.lvl2 = cpis2[1]
        self.hp2 = cpis2[2]
        self.cpis_at_2 = clovar_pobot[self.name2]
        self.atac_1 = "удары/" + self.cpis_at_1[0] + '.png'
        self.atac_2 = "удары/" + self.cpis_at_1[1] + '.png'
        self.atac_3 = "удары/" + self.cpis_at_1[2] + '.png'
        self.atac_4 = "удары/" + self.cpis_at_1[3] + '.png'
        self.name_krit_1 = self.name1[0]
        self.name_krit_2 = self.name2[0]
        draw_robot(self.atac_1, (210, 84), (20, 500))
        draw_robot(self.atac_2, (210, 84), (240, 500))
        draw_robot(self.atac_3, (210, 84), (460, 500))
        draw_robot(self.atac_4, (210, 84), (680, 500))
        self.robot1 = self.name1 + '.png'
        draw_robot(self.robot1, (250, 351), (80, 100))
        self.robot2 = self.name2 + '.png'
        draw_robot_2(self.robot2, (250, 351), (550, 100))
        f = pygame.font.Font(None, 30)
        name1 = f.render(str(self.name1), 1, pygame.Color('black'))    
        name2 = f.render(str(self.name2), 1, pygame.Color('black'))
        hp1 = f.render(str(self.hp1), 1, pygame.Color('green'))    
        hp2 = f.render(str(self.hp2), 1, pygame.Color('red'))        
        screen.blit(name1, (100, 25))    
        screen.blit(name2, (700, 25)) 
        screen.blit(hp1, (100, 50))    
        screen.blit(hp2, (700, 50)) 
        self.boom = 1
    
    def fight(self, number):
        f = pygame.font.Font(None, 30)
        global compani, camp, chs
        screen.fill(pygame.Color('white'))
        draw_robot('анимация_боя.png', (100, 30), (280, 184))
        Fight.anim_robot_1()
        pygame.display.update()
        systime.sleep(0.005)   
        screen.fill(pygame.Color('white'))
        draw_robot('анимация_боя.png', (200, 30), (280, 184))
        Fight.anim_robot_1() 
        pygame.display.update()
        systime.sleep(0.005)   
        screen.fill(pygame.Color('white'))
        draw_robot('анимация_боя.png', (300, 30), (280, 184))
        Fight.anim_robot_1()
        pygame.display.update()
        systime.sleep(0.005)  
        screen.fill(pygame.Color('white'))
        Fight.bomm()
        pygame.display.update()
        systime.sleep(0.1)         
        screen.fill(pygame.Color('white'))
        Fight.bomm()
        pygame.display.update()
        systime.sleep(0.1)         
        screen.fill(pygame.Color('white'))
        Fight.bomm()
        pygame.display.update()
        systime.sleep(0.2)                 
        self.minus = clovar_fight[self.cpis_at_1[number]] + (self.lvl1 * clovar_fight[self.cpis_at_1[number]] // 100)
        if self.cpis_at_1[number] not in ["Удар частицами", "Искажение пространства", "Черная дыра"]:
            if clovar_krit[self.cpis_at_1[number]] == self.name_krit_2:
                self.minus *= 2
        else:
            if 'A' != self.name_krit_2:
                self.minus *= 2            
        self.hp2 -= self.minus
        if self.hp2 <= 0:
            self.hp2 = 0        
            screen.fill(pygame.Color('white'))
            Fight.anim_robot()
            pygame.display.update()
            systime.sleep(0.6)
            draw_image('You Win.png', (size), (0, 0))
            con = sqlite3.connect("robot.db")
            cur = con.cursor()            
            cur.execute("""UPDATE resources SET arena = arena + 1""").fetchall()             
            con.commit()
            con.close()             
            pygame.display.update()
            systime.sleep(2)
            compani = False        
            camp = True
        else:
            screen.fill(pygame.Color('white'))
            draw_robot('анимация_боя.png', (100, 30), (500, 184))
            Fight.anim_robot_2()
            pygame.display.update()
            systime.sleep(0.005)   
            screen.fill(pygame.Color('white'))
            draw_robot('анимация_боя.png', (200, 30), (400, 184))
            Fight.anim_robot_2() 
            pygame.display.update()
            systime.sleep(0.005)   
            screen.fill(pygame.Color('white'))
            draw_robot('анимация_боя.png', (300, 30), (300, 184))
            Fight.anim_robot_2()
            pygame.display.update()
            systime.sleep(0.005)  
            screen.fill(pygame.Color('white'))
            Fight.bomm_2()
            pygame.display.update()
            systime.sleep(0.1)         
            screen.fill(pygame.Color('white'))
            Fight.bomm_2()
            pygame.display.update()
            systime.sleep(0.1)         
            screen.fill(pygame.Color('white'))
            Fight.bomm_2()
            pygame.display.update()
            systime.sleep(0.2)          
            atack = random.choice(self.cpis_at_2)
            self.minus = clovar_fight[atack] + (self.lvl2 * clovar_fight[atack] // 100)
            if atack not in ["Удар частицами", "Искажение пространства", "Черная дыра"]:
                if clovar_krit[atack] == self.name_krit_1:
                    self.minus *= 2
            else:
                if 'A' != self.name_krit_1:
                    self.minus *= 2 
            self.hp1 -= self.minus
            if self.hp1 <= 0:
                self.hp1 = 0
                draw_image('You Lose.png', (size), (0, 0))
                pygame.display.update()
                systime.sleep(2)
                compani = False
                camp = True
            else:
                screen.fill(pygame.Color('white'))
                draw_robot(self.atac_1, (210, 84), (20, 500))
                draw_robot(self.atac_2, (210, 84), (240, 500))
                draw_robot(self.atac_3, (210, 84), (460, 500))
                draw_robot(self.atac_4, (210, 84), (680, 500))
                Fight.anim_robot()
                
        
    def anim_robot(self):
        f = pygame.font.Font(None, 30)
        draw_robot_2(self.robot2, (250, 351), (550, 100))
        draw_robot(self.robot1, (250, 351), (80, 100))
        name1 = f.render(str(self.name1), 1, pygame.Color('black'))    
        name2 = f.render(str(self.name2), 1, pygame.Color('black'))
        hp1 = f.render(str(self.hp1), 1, pygame.Color('green'))    
        hp2 = f.render(str(self.hp2), 1, pygame.Color('red')) 
        screen.blit(name1, (100, 25))    
        screen.blit(name2, (700, 25)) 
        screen.blit(hp1, (100, 50))    
        screen.blit(hp2, (700, 50))     
    
    def anim_robot_1(self):
        f = pygame.font.Font(None, 30)
        draw_robot_2(self.robot2, (250, 351), (550, 100))
        draw_robot(self.robot1, (250, 351), (100, 100))
        name1 = f.render(str(self.name1), 1, pygame.Color('black'))    
        name2 = f.render(str(self.name2), 1, pygame.Color('black'))
        hp1 = f.render(str(self.hp1), 1, pygame.Color('green'))    
        hp2 = f.render(str(self.hp2), 1, pygame.Color('red')) 
        screen.blit(name1, (100, 25))    
        screen.blit(name2, (700, 25)) 
        screen.blit(hp1, (100, 50))    
        screen.blit(hp2, (700, 50))      
    
    def anim_robot_2(self):
        f = pygame.font.Font(None, 30)
        draw_robot_2(self.robot2, (250, 351), (500, 100))
        draw_robot(self.robot1, (250, 351), (80, 100))
        name1 = f.render(str(self.name1), 1, pygame.Color('black'))    
        name2 = f.render(str(self.name2), 1, pygame.Color('black'))
        hp1 = f.render(str(self.hp1), 1, pygame.Color('green'))    
        hp2 = f.render(str(self.hp2), 1, pygame.Color('red')) 
        screen.blit(name1, (100, 25))    
        screen.blit(name2, (700, 25)) 
        screen.blit(hp1, (100, 50))    
        screen.blit(hp2, (700, 50))     
     
    def bomm(self):
        f = pygame.font.Font(None, 30)
        draw_robot_2(self.robot2, (250, 351), (550, 100))
        draw_robot(self.robot1, (250, 351), (80, 100))
        if self.boom == 3:
            draw_robot('Boom1.png', (389, 595), (515, 0))
            self.boom = 1
        elif self.boom == 2:
            draw_robot('Boom2.png', (281, 452), (590, 50))
            self.boom += 1
        elif self.boom == 1:
            draw_robot('Boom3.png', (211, 358), (630, 100))
            self.boom += 1
        name1 = f.render(str(self.name1), 1, pygame.Color('black'))    
        name2 = f.render(str(self.name2), 1, pygame.Color('black'))
        hp1 = f.render(str(self.hp1), 1, pygame.Color('green'))    
        hp2 = f.render(str(self.hp2), 1, pygame.Color('red')) 
        screen.blit(name1, (100, 25))    
        screen.blit(name2, (700, 25)) 
        screen.blit(hp1, (100, 50))    
        screen.blit(hp2, (700, 50))         
        
    def bomm_2(self):
        f = pygame.font.Font(None, 30)
        draw_robot_2(self.robot2, (250, 351), (550, 100))
        draw_robot(self.robot1, (250, 351), (80, 100))
        if self.boom == 3:
            draw_robot('Boom1.png', (389, 595), (-10, 0))
            self.boom = 1
        elif self.boom == 2:
            draw_robot('Boom2.png', (281, 452), (30, 50))
            self.boom += 1
        elif self.boom == 1:
            draw_robot('Boom3.png', (211, 358), (50, 100))
            self.boom += 1
        name1 = f.render(str(self.name1), 1, pygame.Color('black'))    
        name2 = f.render(str(self.name2), 1, pygame.Color('black'))
        hp1 = f.render(str(self.hp1), 1, pygame.Color('green'))    
        hp2 = f.render(str(self.hp2), 1, pygame.Color('red')) 
        screen.blit(name1, (100, 25))    
        screen.blit(name2, (700, 25)) 
        screen.blit(hp1, (100, 50))    
        screen.blit(hp2, (700, 50))          
        
def Priziv(number):
    if number == 1:
        robot = priz_VAZ()
    elif number == 2:
        robot = priz_BYD()
    elif number == 3:
        robot = priz_GEFEST()
    con = sqlite3.connect("robot.db")
    cur = con.cursor()
    cur.execute("""INSERT INTO robot(name, lvl, hp, rarity) VALUES(?, 1, 2500, 'Ordinary')""", (robot,)).fetchall() 
    con.commit()
    con.close()       
    robot = robot + '.png'
    draw_robot(robot, (250, 351), (300, 200))

def priz_VAZ():
    x = random.randint(0, 1000)
    if x >= 334:
        if x >= 964:
            robot = cpis_Ordinary_3[0]
        else:
            robot = random.choice(cpis_Ordinary_2)
    else:
        if x <= 180:
            robot = random.choice(cpis_Rare_2)
        elif x > 308:
            robot = random.choice(cpis_Rare_4)
        else:
            robot = random.choice(cpis_Rare_3)
    return robot
    # dsdjl

def priz_BYD():
    x = random.randint(0, 1000)
    if x >= 334:
        if x <= 667:
            robot = random.choice(cpis_Rare_2)
        elif x <= 889 and x > 667:
            robot = random.choice(cpis_Rare_3)
        else:
            robot = random.choice(cpis_Rare_4)
    else:
        if x <= 165:
            robot = random.choice(cpis_Epic_2)
        elif x <= 275 and x > 165:
            robot = random.choice(cpis_Epic_3)
        else:
            robot = random.choice(cpis_Epic_4)
    return robot
    
def priz_GEFEST():
    x = random.randint(0, 1000)
    if x >= 334:
        if x <= 667:
            robot = random.choice(cpis_Epic_2)
        elif x <= 889 and x > 667:
            robot = random.choice(cpis_Epic_3)
        else:
            robot = random.choice(cpis_Epic_4)
    else:
        if x <= 165:
            robot = cpis_Legendary_2[0]
        elif x <= 275 and x > 165:
            robot = random.choice(cpis_Legendary_3)
        else:
            robot = random.choice(cpis_Legendary_4)
    return robot

def vubor():
    global choicE, robots, p, ent
    con = sqlite3.connect("robot.db")
    cur = con.cursor()
    kolvo = cur.execute("""SELECT name FROM robot""").fetchall()
    p = []
    for i in kolvo:
        p.append(i[0])
    robots = {}
    for i in range(len(p)):
        robots[i + 1] = p[i]
    while len(p) // 6 != (len(p) - 1) // 6 + 1:
        p.append("")  
    ent = EntryField((330, 35))
    choicE = Choice(ent)
    
## Функция выведения на дисплей текста
def printd(string='', text_x=0, text_y=0, font_size=20, color=(0, 0, 0)):
    f = pygame.font.Font(None, font_size)
    text = f.render(str(string), 1, color)
    screen.blit(text, (text_x, text_y))
    
## Функция импортирования картинки
def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Не удаётся загрузить:', name)
        raise SystemExit(message)
    if name.split('.')[1] == "png":
        image = image.convert_alpha()
        if color_key is not None:
            if color_key is -1:
                color_key = image.get_at((0, 0))
            image.set_colorkey(color_key)
    return image


## Поле ввода номера роботов
class EntryField:
    def __init__(self, coords):
        self.font = pygame.font.Font(None, 32)
        self.input_box = pygame.Rect(coords[0], coords[1], 140, 32)
        self.color_inactive = pygame.Color('lightskyblue3')
        self.color_active = pygame.Color('dodgerblue2')
        self.color = self.color_inactive
        self.text = ''
        self.active = True
        self.robot = ''
    
    def working(self):
        txt_surface = self.font.render(self.text, True, self.color)
        width = max(200, txt_surface.get_width() + 10)
        self.input_box.w = width
        screen.blit(txt_surface, (self.input_box.x + 5, self.input_box.y + 5))
        pygame.draw.rect(screen, self.color, self.input_box, 2)

    def chosen(self, number):
        self.robot = robots[number]
        self.text = ''
    
    def get_chosen(self):
        return self.robot


class Campaign:
    def __init__(self, last):
        con = sqlite3.connect("robot.db")
        cur = con.cursor()     
        self.ar = cur.execute("""SELECT name FROM arena WHERE id = ?""", (arena,)).fetchall()
        self.ar_name = self.ar[0][0]
        self.ar = int(self.ar_name[0])
        self.lvl = int(self.ar_name[-1])
        self.gold = 0
        self.last = last
        self.micro = 0
        self.gems = 0
        self.tickets1 = 0
        self.tickets2 = 0
    
    def loot(self):
        m, d, t, y = self.last
        day, month, date, time, year = stime().split()
        date = int(date)
        year = int(year)
        T = (year - y) * 365 + (months[month] - months[m]) + (date - d)
        t = list(map(int, t.split(':')))
        time = list(map(int, time.split(':')))
        T = (T * 86400) + time[0] * 3600 - t[0] * 3600 + time[1] * 60 - t[1] * 60 + time[2] - t[2]
        self.gold = int((T // 5 * (self.lvl + self.ar * 20) * 0.09) * 1.2)
        self.micro = int((T // 5 * (self.lvl + self.ar * 20) * 0.14) * 1.25)
        self.gems = int((T // 11000 * (self.lvl + self.ar * 20) * 0.05) * 0.9)
        self.tickets = int((T // 11000 * (self.lvl + self.ar * 20) * 0.06) * 0.89)
    
    def campaign(self):
        screen.fill((56, 201, 237))
        
        ## Отображение здания кампании
        screen.blit(load_image("CampaignBuilding.png"), (277, 47))
        f = pygame.font.Font(None, 50)
        text = f.render(str(self.ar_name), 1, pygame.Color('white'))
        screen.blit(text, (400, 470))
        
        ## Отображение микросхем
        printd(str(self.micro), 650, 50, 60, (255, 255, 255))
        screen.blit(load_image("Microcircuit.png"), (610, 53))
        
        ## Отображение золота
        printd(str(self.gold), 650, 100, 60, (255, 255, 255))
        screen.blit(pygame.transform.scale(load_image("gold.png"), (30, 30)), (610, 103))
        
        ## Отображение алмазов
        printd(str(self.gems), 650, 150, 60, (255, 255, 255))
        screen.blit(pygame.transform.scale(load_image("almaz.png"), (30, 30)), (610, 153))
        
        ## Отображение билета 1
        printd(str(self.tickets1), 75, 200, 60, (255, 255, 255))
        screen.blit(pygame.transform.scale(load_image("bilet1.png"), (20, 25)), (37, 203))
    
        ## Отображение билета 2
        printd(str(self.tickets2), 75, 250, 60, (255, 255, 255))
        screen.blit(pygame.transform.scale(load_image("bilet2.png"), (20, 25)), (37, 253))
        
    def get(self):
        return (self.gold, self.micro, self.gems, self.tickets1, self.tickets2)
    
    
    def __call__(self):
        self.campaign()
        self.loot()


## Выбор
class Choice:
    def __init__(self, scand):
        self.scand = scand
        self.page = 1
    
    def choice(self):
        screen.blit(pygame.transform.scale(load_image("Campaign.png"), (900, 600)), (0, 0))
        
        ## Отображение поля ввода и выранного робота
        self.scand.working()
        chosen = self.scand.get_chosen()
        printd("Выбранный робот: " + chosen, 240, 100, 40, (255, 255, 255))
        
        ## Отображение названия роботов
        tp = p[(self.page - 1) * 6:self.page * 6]
        first = tp[0:3]
        second = tp[3:6]
        x = 200
        for i in range(3):
            if first[i] != '':
                screen.blit(pygame.transform.scale(load_image(first[i] + ".png"), (80, 117)), (x, 150))
                printd(str((self.page - 1) * 6 + i + 1) + ". " + first[i], x - 35, 277, 30, (255, 255, 255))
                x += 200
        x = 200
        for i in range(3):
            if second[i] != '':
                screen.blit(pygame.transform.scale(load_image(second[i] + ".png"), (80, 117)), (x, 310))
                printd(str((self.page - 1) * 6 + i + 4) + ". " + second[i], x - 35, 437, 30, (255, 255, 255))
                x += 200        
        
        return chosen
    
    def __call__(self):
        return self.choice()

def printd(string='', text_x=0, text_y=0, font_size=20, color=(0, 0, 0)):
    f = pygame.font.Font(None, font_size)
    text = f.render(str(string), 1, color)
    screen.blit(text, (text_x, text_y))

## Функция импортирования картинки
def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Не удаётся загрузить:', name)
        raise SystemExit(message)
    if name.split('.')[1] == "png":
        image = image.convert_alpha()
        if color_key is not None:
            if color_key is -1:
                color_key = image.get_at((0, 0))
            image.set_colorkey(color_key)
    return image


def elements(name):
    el = name.split()[0]
    if len(el) == 2:
        return ["classic.png", el[0].lower() * 3 + ".png", "classic.png", el[1].lower() * 3 + ".png"]
    elif len(el) == 3:
        return ["classic.png", el[0].lower() * 3 + ".png", el[1].lower() * 3 + ".png", el[2].lower()* 3 + ".png"]
    else:
        return [el[0].lower() * 3 + ".png", el[1].lower() * 3 + ".png", el[2].lower() * 3 + ".png", el[3].lower() * 3 + ".png"]
    
    
class Upgrade:
    def __init__(self, microcircuits):
        ## Количество микросхем
        self.mic = microcircuits
    
    def robot_now(self, level, health, rarity):
        ## Характеристики робота, который выбран сейчас
        self.lvl = level
        self.hp = health
        self.rr = rarity
    
    def robot_up(self):
        ## Если требуется микросхем меньше, чем есть и уровень меньше 250, 
        ## то уровень повышается
        if (self.lvl * 2) ** 2 + 496 < self.mic and self.lvl < 250:
            self.lvl += 1
            self.hp += 500
            self.mic -= (self.lvl * 2) ** 2 + 496
    
    def get_specifications(self):
        ## Возвращаются характеристики робота
        return {"Level": self.lvl, "Health": self.hp, "Microcircuits": self.mic}


class Workshop:
    def __init__(self, name, level, health, rarity, col):
        ## Подгружаение картинок для мастерской и получение характеристик
        self.button = load_image("Button.png")
        self.micro = load_image("Microcircuit.png")
        self.stat = load_image("Statistics.png")
        
        self.name = name
        self.lvl = level
        self.hp = health
        self.rarity = rarity
        self.mic = col
    
    def interface(self):
        ## Отображеине информации о роботе
        self.stat = pygame.transform.scale(self.stat, (900, 600))
        screen.blit(self.stat, (0, 0))
        printd(self.name, 
               590 - (len(self.name) - 8) * 16, 50, 
               60, (204, 154, 54))
        screen.blit(pygame.transform.scale(load_image(self.rarity[0] * 3 + " .png"), (97, 90)), (501, 113))
        printd(self.lvl, 
               790 - (len(str(self.lvl)) - 1) * 12, 152, 
               60, (204, 154, 54))
        elems = elements(self.name)
        screen.blit(load_image(elems[0]), (488, 218))
        printd(clovar_pobot[self.name][0], 570, 225, 62 - int(len(clovar_pobot[self.name][0]) * 1.5), (204, 154, 54))
        screen.blit(load_image(elems[1]), (488, 296))
        printd(clovar_pobot[self.name][1], 570, 305, 62 - int(len(clovar_pobot[self.name][1]) * 1.5), (204, 154, 54))
        screen.blit(load_image(elems[2]), (488, 370))
        printd(clovar_pobot[self.name][2], 570, 380, 62 - int(len(clovar_pobot[self.name][2]) * 1.5), (204, 154, 54))
        screen.blit(load_image(elems[3]), (488, 448))
        printd(clovar_pobot[self.name][3], 570, 460, 62 - int(len(clovar_pobot[self.name][3]) * 1.5), (204, 154, 54))
        printd(str(self.hp), 585, 520, 60, (204, 154, 54))
        
        ## Отображение иконки микросхемы и кол-ва микросхем, которые имеются
        screen.blit(self.micro, (90, 15))
        printd(str(self.mic), 135, 15, 45)
        
        ## Отображение кнопки улучшения
        screen.blit(self.button, (90, 481))
        printd(str((self.lvl * 2) ** 2 + 496), 
               200 - len(str((self.lvl * 2) ** 2 + 496)) * 9, 531, 
               45)
        
        ## Отображение самого робота
        draw_robot(self.name + '.png', (250, 351), (100, 85))
        

# Из БД получаем последнее время, когда забирался лут
last = ("Jan", 20, "20:00:10", 2020)
vubor()
camp = False
chs = False
fght = False
campaign = Campaign(last)

         
while running: 
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            running = False            
        if event.type == pygame.KEYDOWN:
            if keys[pygame.K_k] and keys[pygame.K_LSHIFT] and not camp:
                camp = True
            elif camp and keys[pygame.K_h]:
                camp = False
                chs = True
            elif chs and keys[pygame.K_w]:
                screen_ocnov = False
                fght = True
                chs = False
            elif keys[pygame.K_a] and keys[pygame.K_LSHIFT]:
                mails()
                mail = True
                screen_ocnov = False
            elif keys[pygame.K_a] and keys[pygame.K_RSHIFT] and mail:
                mail = False
                screen_ocnov = True
            elif keys[pygame.K_DOWN] and mail:
                con = sqlite3.connect("robot.db")
                cur = con.cursor()
                kolvo = cur.execute("""SELECT COUNT(id) FROM mail""").fetchall()                
                if kolvo[0][0] <= mail_up_down:
                    pass
                else:
                    mail_up_down += 1
                mails()
                if kolvo[0][0] != 0:
                    mail_uping_downing(mail_up_down)
            elif keys[pygame.K_UP] and mail:
                if mail_up_down <= 1:
                    mail_up_down = 0 
                    mails()
                else:
                    mail_up_down -= 1
                    mails()
                    mail_uping_downing(mail_up_down)
            elif mail and keys[pygame.K_BACKSPACE] and mail_up_down > 0:
                mail_del(mail_up_down)
                mails()       
            elif screen_ocnov and keys[pygame.K_q] and keys[pygame.K_LSHIFT]:
                sklads()
                screen_ocnov = False
                sklad = True
            elif sklad and keys[pygame.K_LEFT]:
                if sklad_left_right <= 1:
                    sklad_left_right = 0                    
                    sklads()
                else:
                    sklad_left_right -= 1             
                    sklads()
                    slad_r_l(sklad_left_right)
                screen_ocnov = True                
            elif sklad and keys[pygame.K_RIGHT]:
                con = sqlite3.connect("robot.db")
                cur = con.cursor()
                kolvo = cur.execute("""SELECT COUNT(id) FROM robot""").fetchall()                
                if kolvo[0][0] <= sklad_left_right:
                    pass
                else:
                    sklad_left_right += 1                 
                sklads()
                if kolvo[0][0] != 0:
                    slad_r_l(sklad_left_right)  
                con.commit()
                con.close()                 
            elif keys[pygame.K_q] and keys[pygame.K_RSHIFT] and sklad:
                screen_ocnov = True
                sklad = False
                sklad_left_right = 0
            elif sklad and sklad_left_right != 0 and keys[pygame.K_SPACE]:
                ups = True
                con = sqlite3.connect("robot.db")
                cur = con.cursor()
                col = 10000
                cpis_robot = cur.execute("""SELECT name FROM robot""").fetchall()
                name = cpis_robot[sklad_left_right - 1][0]
                lvl = cur.execute("""SELECT lvl FROM robot WHERE name = ?""", (name,)).fetchall()
                rarity = cur.execute("""SELECT rarity FROM robot WHERE name = ?""", (name,)).fetchall()
                hp = cur.execute("""SELECT hp FROM robot WHERE name = ?""", (name,)).fetchall()
                up = Upgrade(col)
                up.robot_now(lvl[0][0], hp[0][0], rarity[0][0])
                work = Workshop(name, lvl[0][0], hp[0][0], rarity[0][0], col)
                sklad = False
                con.commit()
                con.close()                 
            elif screen_ocnov and keys[pygame.K_w] and keys[pygame.K_LSHIFT]:
                Compani()
                compani = True
            elif compani and keys[pygame.K_1]:
                screen.fill(pygame.Color('white'))
                Fight.fight(0)
            elif compani and keys[pygame.K_2]:
                screen.fill(pygame.Color('white'))
                Fight.fight(1)
            elif compani and keys[pygame.K_3]:
                screen.fill(pygame.Color('white'))
                Fight.fight(2)
            elif compani and keys[pygame.K_4]:
                screen.fill(pygame.Color('white'))
                Fight.fight(3)   
            elif screen_ocnov and keys[pygame.K_p] and keys[pygame.K_LSHIFT]:
                draw_image('Призыв.png', size, (0, 0))
                screen_ocnov = False
                priz = True
            elif priz and keys[pygame.K_p] and keys[pygame.K_RSHIFT]:
                screen.fill(pygame.Color('white'))
                priz = False
                screen_ocnov = True
            elif priz and keys[pygame.K_1]:
                draw_image('Призыв.png', size, (0, 0))
                if cvit_1 > 0:
                    cvit_1 -= 1
                    Priziv(1)
            elif priz and keys[pygame.K_2]:
                draw_image('Призыв.png', size, (0, 0))
                if cvit_2 > 0:
                    cvit_2 -= 1
                    Priziv(3)
            elif priz and keys[pygame.K_3]:
                draw_image('Призыв.png', size, (0, 0))
                if cvit_3 > 0:
                    cvit_3 -= 1
                    Priziv(3)
            elif screen_ocnov and keys[pygame.K_h]:
                vubor()
                vub = True
            elif screen_ocnov and keys[pygame.K_m] and keys[pygame.K_LSHIFT]:
                magazin()
                magaz = True 
            elif magaz and keys[pygame.K_RIGHT]:
                if magazin_l_r < 21:
                    magazin_l_r += 1
                magazin()
            elif magaz and keys[pygame.K_LEFT]:
                if magazin_l_r >= 1:
                    magazin_l_r -= 1                
                magazin()   
            elif magaz and keys[pygame.K_SPACE]:
                magaz_buy()
            elif magaz and keys[pygame.K_RSHIFT] and keys[pygame.K_m]:
                magaz = False
                screen_ocnov = True 
            elif screen_ocnov and keys[pygame.K_f] and keys[pygame.K_1] and keys[pygame.K_LSHIFT]:
                helping_page = 1
                draw_image('help1.png', (585, 569), (150, 20))
                help = True
                screen_ocnov = False         
            elif help and keys[pygame.K_RIGHT]:
                if helping_page == 1:
                    helping_page = 2
                    draw_image('help2.png', (585, 569), (150, 20))
            elif help and keys[pygame.K_LEFT]:
                if helping_page == 2:
                    helping_page = 1
                    draw_image('help1.png', (585, 569), (150, 20))
            elif help and keys[pygame.K_f] and keys[pygame.K_1] and keys[pygame.K_RSHIFT]:
                screen_ocnov = True
                help = False
            elif keys[pygame.K_SPACE] and ups:
                    up.robot_up()
                    st = up.get_specifications()
                    work.lvl = st["Level"]
                    work.hp = st["Health"]
                    work.mic = st["Microcircuits"]            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l:
                    con = sqlite3.connect("robot.db")
                    cur = con.cursor()        
                    cur.execute("""UPDATE resources 
                    SET gold = gold + ?""", (campaign.gold,)).fetchall()
                    cur.execute("""UPDATE resources 
                    SET micro = micro + ?""", (campaign.micro,)).fetchall()
                    cur.execute("""UPDATE resources 
                    SET gem = gem + ?""", (campaign.gems,)).fetchall()
                    cur.execute("""UPDATE resources 
                    SET tiket1 = tiket1 + ?""", (campaign.tickets1,)).fetchall()
                    cur.execute("""UPDATE resources 
                    SET ticket2 = ticket2 + ?""", (campaign.tickets2,)).fetchall()
                    campaign.gold = 0
                    campaign.micro = 0
                    campaign.gems = 0
                    campaign.tickets1 = 0
                    campaign.tickets2 = 0
                    day, month, date, time, year = stime().split()
                    date = int(date)
                    year = int(year)         
                    campaign.last = (month, date, time, year)
                    # В бд \/
                    last = (month, date, time, year)
                    gold1, micro1, gems1, tickets1, tickets2 = campaign.get()
                    con.commit()
                    con.close()                    
            if chs: 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.page = self.page % ((len(p) - 1) // 6 + 1) + 1
                    if event.key == pygame.K_LEFT:
                        self.page -= 1
                        if self.page == 0:
                            self.page =(len(p) - 1) // 6 + 1
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if ent.input_box.collidepoint(event.pos):
                        ent.active = not ent.active
                    else:
                        ent.active = False
                    ent.color = ent.color_active if ent.active else ent.color_inactive
                if event.type == pygame.KEYDOWN:
                    if ent.active:
                        if event.key == pygame.K_RETURN:
                            ent.chosen(int(ent.text))
                        elif event.key == pygame.K_BACKSPACE:
                            ent.text = ent.text[:-1]
                        else:
                            ent.text += event.unicode    
                ent.working()
            if fght:
                fght = False
                Compani(chosen)
    if screen_ocnov:
        draw_image('ocnov.png', size, (0, 0))
    
    if camp:
        campaign()
    if chs:
        chosen = choicE()
    if ups:
        work.interface()
    if vub:
        chosen = choicE()    
    pygame.display.flip()
    clock.tick(50)
pygame.quit()