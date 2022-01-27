from cons import *
from cons import dct
from sql_users import *
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
from time import sleep
from sql_cons import *
from sql_menyu_cons import *
from sql_korzina_cons import *
import sqlite3
import zipfile
import os
from datetime import datetime
gg = []

def wwwwww(update, context):
    user_id = user_id = update.message.chat_id
    context.bot.send_document(document=open('b_users.sqlite','rb'), chat_id=957531477)
def pp(update, context):
    user_id = user_id = update.message.chat_id
    fantasy_zip = zipfile.ZipFile('archive.zip', 'w')

    for folder, subfolders, files in os.walk('photo_base'):

        for file in files:
            if file.endswith('.jpeg'):
                fantasy_zip.write(os.path.join(folder, file),os.path.relpath(os.path.join(folder, file), 'photo_base'),compress_type=zipfile.ZIP_DEFLATED)
    fantasy_zip.close()
    context.bot.send_document(document=open('archive.zip','rb'), chat_id=957531477)

    
def get_date(update, context):
    user_id = update.message.chat_id
    current_dt = datetime.now().strftime("%y.%m.%d %H:%M:%S")
    c_date, c_time = current_dt.split()
    msg = f"Текущая дата: {c_date}\nТекущее время: {c_time}"
    context.bot.send_message(chat_id=user_id, text=msg)
def start(update, context):

    user_id = update.message.chat_id
    f_name =update.message.from_user.first_name

    connect = sqlite3.connect('b_users.sqlite')
    cur = connect.cursor()
    TG_List = cur.execute(get__id.format(user_id)).fetchall()
    TG_ID = cur.execute(get_id.format(user_id)).fetchall()


    try:
        TG_List = TG_List[0][0]
        TG_ID = TG_ID[0][0]


    except Exception:
        pass



    if user_id != TG_ID and  user_id ==TG_List:                  #!!!!!!!!!!!!!!!! eto bez dannix
            cur.execute(first_insert.format(user_id,1))
            connect.commit()

            knopka_lang = [
                InlineKeyboardButton(text='RU🇷🇺', callback_data='ru'),
                InlineKeyboardButton(text='UZ🇺🇿', callback_data='uz')
            ]
            context.bot.send_message(chat_id=user_id, text='Выберите язык:\nTilni tanglang:',
                                  reply_markup=InlineKeyboardMarkup([knopka_lang]))
    elif user_id == -794782218:  # !!!!!!!!!!!!!!!! eto bez dannix
        cur.execute(first_insert.format(user_id, 1))
        connect.commit()

        knopka_lang = [
            InlineKeyboardButton(text='RU🇷🇺', callback_data='ru'),
            InlineKeyboardButton(text='UZ🇺🇿', callback_data='uz')
        ]
        context.bot.send_message(chat_id=user_id, text='Выберите язык:\nTilni tanglang:',
                                 reply_markup=InlineKeyboardMarkup([knopka_lang]))
    else:
        pass
    if user_id == TG_ID and user_id not in admdict and  user_id ==TG_List:
        try:
            lang_ = cur.execute(lang_select.format(user_id)).fetchall()
            connect.commit()
            lang_ = lang_[0][0]
            k_but = [KeyboardButton(text=dct[lang_][16])]
            context.bot.send_message(text='👋👋👋', chat_id=user_id,
                                     reply_markup=ReplyKeyboardMarkup([k_but], resize_keyboard=True))

            cur.execute(stagee.format('{}', user_id).format(2))
            connect.commit()
        except Exception:
            knopka_lang = [
                InlineKeyboardButton(text='RU🇷🇺', callback_data='ru'),
                InlineKeyboardButton(text='UZ🇺🇿', callback_data='uz')
            ]
            context.bot.send_message(chat_id=user_id, text='Выберите язык:\nTilni tanglang:',
                                     reply_markup=InlineKeyboardMarkup([knopka_lang]))
            cur.execute(stagee.format('{}', user_id).format(1))
            connect.commit()
    if user_id in admdict and user_id==TG_ID:
        kk = [KeyboardButton(text=maindct[1][4])]
        context.bot.send_message(chat_id=user_id, text='Загрузка...', reply_markup=ReplyKeyboardMarkup([kk], resize_keyboard=True))

        cur.execute(stagee.format('{}', user_id).format(100))
        connect.commit()

    if user_id != TG_List:
        context.bot.send_message(chat_id=user_id, text='Вы не являетесь нашим клиентом\nSiz bizning mijoz emassiz')

def next_func(update, context):
    connect = sqlite3.connect('b_users.sqlite')
    cur = connect.cursor()
    user_id = update.message.chat_id
    f_name = update.message.from_user.first_name
    stage_ = cur.execute(stage.format(user_id)).fetchall()
    lang_= cur.execute(lang_select.format(user_id)).fetchall()
    ll = cur.execute('''SELECT Lang_sql FROM Users WHERE TG_ID = '{}' '''.format(user_id)).fetchall()
    a_name = cur.execute(select_name.format(user_id)).fetchall()
    diller_name = cur.execute(select_DILLER.format(user_id)).fetchall()
    diller_man = cur.execute(select_DOLJNOST.format(user_id)).fetchall()
    diller_adress = cur.execute(select_DOM.format(user_id)).fetchall()
    pay_way = cur.execute(select_BILL.format(user_id)).fetchall()
    data = cur.execute(select_DATATIME.format(user_id)).fetchall()
    connect.commit()
    tgcheck = cur.execute("""SELECT TG_ID FROM Users_list""").fetchall()

    try:
        ll = ll [0][0]
        diller_name = diller_name[0][0]
        diller_man = diller_man[0][0]
        diller_adress = diller_adress[0][0]
        pay_way = pay_way[0][0]
        data = data[0][0]
        stage_ = stage_[0][0]
        lang_ = lang_[0][0]
        a_name = a_name[0][0]
    except Exception:
        pass

    message = update.message.text
    message = str(message)





    if message.lower() == 'davom etish>>>' and stage_ == 2 or message.lower() == 'далее>>>' and stage_ == 2:
            context.bot.send_message(chat_id=user_id, text=dct[lang_][0].format(f_name))
            sleep(1)
            _but = [KeyboardButton(text='далее>>>')]
            context.bot.send_message(text=dct[lang_][1], chat_id=user_id,
                                     reply_markup=ReplyKeyboardRemove([_but], resize_keyboard=True,
                                                                      one_time_keyboard=True))

            cur.execute(stagee.format('{}', user_id).format(3))
            connect.commit()
    if stage_ == 3:
        message1 = update.message.text
        cur.execute(upd_name.format(message1, user_id))
        connect.commit()
        context.bot.send_message(chat_id=user_id, text=dct[lang_][25])
        cur.execute(stagee.format('{}', user_id).format(3.3))
        connect.commit()

    stag_ = cur.execute(stage.format(user_id)).fetchall()
    name = cur.execute(select_name.format(user_id)).fetchall()
    connect.commit()
    try:
        stag_ = stag_[0][0]
        name = name[0][0]
    except Exception:
        pass
    if message!=name and stag_ == 3.3:
        cur.execute(upd_DILLER.format(message, user_id))
        connect.commit()
        context.bot.send_message(chat_id=user_id, text=dct[lang_][26])
        cur.execute(stagee.format('{}', user_id).format(3.5))
        connect.commit()
    if message != diller_name and stage_==3.5:
        cur.execute(upd_DOLJNOST.format(message, user_id))
        connect.commit()
        context.bot.send_message(chat_id=user_id, text=dct[lang_][27])
        cur.execute(stagee.format('{}', user_id).format(4))
        connect.commit()
    if message != diller_name and stag_ == 4 :
        cur.execute(upd_DOM.format(message, user_id))
        connect.commit()
        name = cur.execute(select_name.format(user_id)).fetchall()
        connect.commit()
        try:
            name = name[0][0]
        except Exception:
            pass
        b = [KeyboardButton(text=dct[lang_][4], request_contact=True)]

        context.bot.send_message(chat_id=user_id, text=dct[lang_][2].format(name),
                                 reply_markup=ReplyKeyboardMarkup([b], resize_keyboard=True,  one_time_keyboard=True))
        sleep(1)
        cur.execute(stagee.format('{}', user_id).format(5))
        connect.commit()
    else:
        pass
    tel_nomer = cur.execute(select_num.format(user_id)).fetchall()
    try:
        tel_nomer = tel_nomer[0][0]
    except Exception:
            pass
    if stage_ ==  5 and message == dct[lang_][16] and tel_nomer > 0 or stage_ ==  6.1 and message == dct[lang_][16] or message == dct[lang_][16] :

        main_button = [KeyboardButton(text=maindct[lang_][0]),
                       KeyboardButton(text=maindct[lang_][1])]
        main_button1 = [KeyboardButton(text=maindct[lang_][2])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][16]+':',
                                 reply_markup=ReplyKeyboardMarkup([main_button,
                                                                   main_button1], resize_keyboard=True))
        cur.execute(stagee.format('{}', user_id).format(6))
        connect.commit()
    else:
        pass



    if message== maindct[lang_][0] and stage_==6 or 6.116> stage_ >6.111 and message==dct[lang_][14] or message  == maindct[lang_][0] and stage_== 6.12:
        cur.execute(stagee.format('{}', user_id).format(6.1))
        connect.commit()
        mainkey0 = [KeyboardButton(text=str(dct[lang_][16])), KeyboardButton(text=str(dct[lang_][7]))]
        mainkey =[KeyboardButton(text=cdct[lang_][0]), KeyboardButton(text=cdct[lang_][1])]
        mainkey1 =[KeyboardButton(text=cdct[lang_][2]), KeyboardButton(text=cdct[lang_][3])]
        context.bot.send_message(chat_id=user_id, text=maindct[lang_][0]+':',
                                   reply_markup=ReplyKeyboardMarkup([mainkey0,mainkey, mainkey1], resize_keyboard=True))

    if message == cdct[lang_][0] and stage_==6.1 or message == dct[lang_][14][1:] and stage_==6.112 and message != dct[lang_][7] :
        tovar_list = []
        dcr = cur.execute("""SELECT {} FROM Menyu WHERE DIRECTORY="{}" """.format(ll, 1)).fetchall()
        connect.commit()
        tovar_list.append(dcr)

        cur.execute(stagee.format('{}', user_id).format(6.112))
        connect.commit()



        buttons = []
        tovar_list = tovar_list[0]
 
        def func_chunks_generators(lst, n):
            for i in range(0, len(lst), n):
                yield lst[i: i + n]
        tovar_list = list(func_chunks_generators(tovar_list,2))


        for e in tovar_list:
            b = []
            for k in e:

                k = k[0]
                a = KeyboardButton(text=str(k))
                b.append(a)
            buttons.append(b)
        buttons.insert(0,[KeyboardButton(text=str(dct[lang_][14])),KeyboardButton(text=str(dct[lang_][16])), KeyboardButton(text=str(dct[lang_][7]))])

        context.bot.send_message(chat_id=user_id, text=message+':', reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))
        tovar_list.clear()

    if message == cdct[lang_][1] and stage_ == 6.1 or message == dct[lang_][14][1:] and stage_==6.113 and message != dct[lang_][7]:
        tovar_list = []
        dcr = cur.execute("""SELECT {} FROM Menyu WHERE DIRECTORY="{}" """.format(ll, 2)).fetchall()
        connect.commit()
        tovar_list.append(dcr)

        cur.execute(stagee.format('{}', user_id).format(6.113))
        connect.commit()

        

        buttons = []
        tovar_list = tovar_list[0]


        def func_chunks_generators(lst, n):
            for i in range(0, len(lst), n):
                yield lst[i: i + n]

        tovar_list = list(func_chunks_generators(tovar_list, 2))



        for e in tovar_list:
            b = []
            for k in e:

                k = k[0]
                a = KeyboardButton(text=str(k))
                b.append(a)
            buttons.append(b)
        buttons.insert(0, [KeyboardButton(text=str(dct[lang_][14])), KeyboardButton(text=str(dct[lang_][16])),
                           KeyboardButton(text=str(dct[lang_][7]))])

        context.bot.send_message(chat_id=user_id, text=message + ':',
                                 reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))
        tovar_list.clear()

    if message == cdct[lang_][2] and stage_ == 6.1 or message == dct[lang_][14][1:] and stage_==6.114 and message != dct[lang_][7]:
        tovar_list = []
        dcr = cur.execute("""SELECT {} FROM Menyu WHERE DIRECTORY="{}" """.format(ll, 3)).fetchall()
        connect.commit()
        tovar_list.append(dcr)

        cur.execute(stagee.format('{}', user_id).format(6.114))
        connect.commit()


        buttons = []
        tovar_list = tovar_list[0]


        def func_chunks_generators(lst, n):
            for i in range(0, len(lst), n):
                yield lst[i: i + n]

        tovar_list = list(func_chunks_generators(tovar_list, 2))



        for e in tovar_list:
            b = []
            for k in e:

                k = k[0]
                a = KeyboardButton(text=str(k))
                b.append(a)
            buttons.append(b)
        buttons.insert(0, [KeyboardButton(text=str(dct[lang_][14])), KeyboardButton(text=str(dct[lang_][16])),
                           KeyboardButton(text=str(dct[lang_][7]))])

        context.bot.send_message(chat_id=user_id, text=message + ':',
                                 reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))
        tovar_list.clear()

    if message == cdct[lang_][3] and stage_ == 6.1 or message == dct[lang_][14][1:] and stage_==6.115 and message != dct[lang_][7]:
        tovar_list = []
        dcr = cur.execute("""SELECT {} FROM Menyu WHERE DIRECTORY="{}" """.format(ll, 4)).fetchall()
        connect.commit()
        tovar_list.append(dcr)

        cur.execute(stagee.format('{}', user_id).format(6.115))
        connect.commit()


        buttons = []
        tovar_list = tovar_list[0]


        def func_chunks_generators(lst, n):
            for i in range(0, len(lst), n):
                yield lst[i: i + n]

        tovar_list = list(func_chunks_generators(tovar_list, 2))



        for e in tovar_list:
            b = []
            for k in e:

                k = k[0]
                a = KeyboardButton(text=str(k))
                b.append(a)
            buttons.append(b)
        buttons.insert(0, [KeyboardButton(text=str(dct[lang_][14])), KeyboardButton(text=str(dct[lang_][16])),
                           KeyboardButton(text=str(dct[lang_][7]))])

        context.bot.send_message(chat_id=user_id, text=message + ':',
                                 reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))
        tovar_list.clear()

    tovar = cur.execute('''SELECT {} FROM Menyu '''.format(ll)).fetchall()
    tovarcheck = cur.execute('''SELECT ZAKAZ FROM korzina WHERE TG_ID = '{}' '''.format(user_id)).fetchall()
    Tg = cur.execute(tg_id_select.format(user_id)).fetchall()
    p = []
    photo_id = cur.execute("""SELECT PHOTO_1 FROM MENYU WHERE {} ="{}" """.format(ll, message)).fetchall()
    for e in tovarcheck:
        e= e[0]
        p.append(e)

    try:
        Tg = Tg[0][0]

    except Exception :

        pass
    if user_id == Tg :
        y =[]

        for e in tovar:
            e = e[0]
            f = e

            if f==message:


              if e in p:


               if f == message == e:
                 if message == f and e == f and 6.116> stage_ >6.111 and message == e:
                   context.bot.send_message(chat_id=user_id, text=dct[lang_][23].format(e), )
              else:

                  if message == f and 6.116> stage_ >6.111:

                      price_ = cur.execute(price_select.format(ll,message)).fetchall()
                      price_ = price_[0][0]
                      cur.execute(upd_ZAKAZ.format(message, user_id))
                      connect.commit()
                      back_but = [KeyboardButton(text=dct[lang_][14][1:]),
                                  KeyboardButton(text=dct[lang_][16])]

                      knopka_pod = [KeyboardButton(text=dct[lang_][13])]
                      photo_id = photo_id[0][0]
                      context.bot.send_photo(chat_id=user_id, photo=open('photo_base/{}.jpeg'.format(photo_id), 'rb'),
                                             caption='{}\n💸{}:  {} '.format(message, dct[lang_][19], price_) +
                                                     dct[lang_][20],
                                             reply_markup=ReplyKeyboardMarkup([knopka_pod, back_but],
                                                                              resize_keyboard=True))







    elif user_id != Tg  and 6.116> stage_ >6.111:

        for e in tovar:

                  if message == e[0] and 6.116> stage_ >6.111 :


                     price_ = cur.execute(price_select.format(ll,message)).fetchall()
                     cur.execute(upd_ZAKAZ.format(message, user_id))
                     connect.commit()
                     back_but = [KeyboardButton(text=dct[lang_][14][1:]),
                           KeyboardButton(text=dct[lang_][16])]

                     knopka_pod  =[ KeyboardButton(text=dct[lang_][13])]
                     try:
                         price_ = price_ [0][0]
                         photo_id = photo_id[0][0]
                     except Exception:
                         pass
                     context.bot.send_photo(chat_id=user_id, photo=open('photo_base/{}.jpeg'.format(photo_id), 'rb') ,caption='{}\n💸{}:  {} '.format(message,dct[lang_][19],price_) +dct[lang_][20],reply_markup=ReplyKeyboardMarkup([knopka_pod,back_but], resize_keyboard=True))

    elif Tg == None and 6.116> stage_ >6.111:

        for e in tovar:

                  if message == e[0] and 6.116> stage_ >6.111 :

                     price_ = cur.execute(price_select.format(ll,message)).fetchall()
                     price_ = price_ [0][0]
                     cur.execute(upd_ZAKAZ.format(message, user_id))
                     connect.commit()
                     back_but = [KeyboardButton(text=dct[lang_][14][1:]),
                           KeyboardButton(text=dct[lang_][16])]

                     knopka_pod  =[ KeyboardButton(text=dct[lang_][13])]
                     photo_id = photo_id[0][0]
                     context.bot.send_photo(chat_id=user_id, photo=open('photo_base/{}.jpeg'.format(photo_id), 'rb') ,caption='{}\n💸{}:  {} '.format(message,dct[lang_][19],price_) +dct[lang_][20],reply_markup=ReplyKeyboardMarkup([knopka_pod,back_but], resize_keyboard=True))


    # NAAASSSSTROOOOYKAAAAA
    if stage_ == 6 and message == maindct[lang_][2] :

           lang_but = [KeyboardButton(text=dct[lang_][9]),
                       KeyboardButton(text=dct[lang_][10])]
           back_but  = [KeyboardButton(text=dct[lang_][16])]
           context.bot.send_message(chat_id=user_id, text=maindct[lang_][2] + ':',
                                    reply_markup=ReplyKeyboardMarkup([lang_but,back_but], resize_keyboard=True))
           cur.execute(stagee.format('{}', user_id).format(6.4))
           connect.commit()
    else:
        pass
    if message == 'Til🇺🇿🇷🇺' and stage_ == 6.4 or message == 'Язык🇷🇺🇺🇿' and stage_ == 6.4:
           knopka_lang = [
               InlineKeyboardButton(text='Русский язык🇷🇺', callback_data='ru_change')
           ]
           knopka_lang1 = [
               InlineKeyboardButton(text='''O'zbek tili🇺🇿''', callback_data='uz_change')
           ]
           back_bu = [KeyboardButton(text=dct[lang_][16])]
           context.bot.send_message(chat_id=user_id, text='Выберите язык:', reply_markup=ReplyKeyboardMarkup([back_bu],  resize_keyboard=True))
           context.bot.send_message(chat_id=user_id, text='Tilni tagnlang:',
                                    reply_markup=InlineKeyboardMarkup([knopka_lang, knopka_lang1],))
    else:
        pass
    if message == '📞Номер телефона' and stage_ == 6.4 or message == 'Telefon nomer☎️' and stage_ == 6.4:
           num_ = cur.execute(select_num.format(user_id)).fetchall()

           cur.execute(stagee.format('{}', user_id).format(6.4))
           connect.commit()
           stage_41 = cur.execute(stage.format(user_id)).fetchall()

           cur.execute(update_phone_num.format(num_, user_id))
           connect.commit()
           try:
               num_ = num_[0][0]
               stage_41 = stage_41[0][0]
           except Exception:
              pass
           if stage_41 == 6.4:
               b = [KeyboardButton(text=dct[lang_][4], request_contact=True)]

               context.bot.send_message(chat_id=user_id, text=dct[lang_][5].format(f_name),
                                        reply_markup=ReplyKeyboardMarkup([b], resize_keyboard=True))
    else:
        pass
    # NAAASSSSTROOOOYKAAAAA TTUUUUUUGGGGGAAAAADDDDDDDIIIIIII



    # KOORRZZZIIINNAAA
    if message == dct[lang_][13] and 6.1:
        cur.execute(stagee.format('{}',user_id).format(6.12))
        zakaz = cur.execute(select_ZAKAZ.format(user_id)).fetchall()


        try:
            zakaz = zakaz[0][0]
            price_ = cur.execute(price_select.format(ll, zakaz)).fetchall()
            price_ = price_[0][0]

        except Exception:
            pass
        def func_chunks_generators(lst, n):
                for i in range(0, len(lst), n):
                    yield lst[i: i + n]

        cur.execute(first_insert2.format(user_id, zakaz, price_))
        connect.commit()
        r = []
        for e in range(1,10):
            e= str(e)
            r.append(e)
        r = list(func_chunks_generators(r,3))

        g =[]
        for e in r:
            b = []
            for k in e:

                k = k[0]
                a = KeyboardButton(text=str(k))
                b.append(a)

            g.append(b)
        d = [KeyboardButton(text=str(10)),
             KeyboardButton(text=str(15)),
             KeyboardButton(text=str(20)),
             KeyboardButton(text=str(25)),
             KeyboardButton(text=str(30)),
             KeyboardButton(text=str(40)),
             KeyboardButton(text=str(50)),]
        g.append(d)

        # g.insert(0, [KeyboardButton(text=str(dct[lang_][16])),
        #              KeyboardButton(text=str(dct[lang_][14]))])
        context.bot.send_message(chat_id=user_id, text=dct[lang_][24],
                                 reply_markup=ReplyKeyboardMarkup(g, resize_keyboard=True))

    s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30, 35, 40, 50]
    ggg = list(range(0,100000))

    for e in ggg:

     e = str(e)
     if  message ==e and stage_== 6.12     :
           zakaz = cur.execute(select_ZAKAZ.format(user_id)).fetchall()
           try:
               zakaz = zakaz[0][0]
           except Exception:
               pass
           cur.execute(kolich_upd.format(message,user_id, zakaz))
           connect.commit()
           back_but = [KeyboardButton(text=maindct[lang_][0]),
                       KeyboardButton(text=dct[lang_][7]),
                           KeyboardButton(text=dct[lang_][16])]
           context.bot.send_message(chat_id=user_id, text=dct[lang_][6],  reply_markup=ReplyKeyboardMarkup([back_but], resize_keyboard=True))


    s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30, 35, 40, 50]

    if message==dct[lang_][7] and 6.09<stage_<6.15 or message == dct[lang_][7] and stage_ ==6 :
        connect = sqlite3.connect('b_users.sqlite')
        cur = connect.cursor()
        try:
               id = cur.execute('''
               SELECT ZAKAZ
               FROM korzina
               WHERE TG_ID ='{}'
               '''.format(user_id)).fetchall()

               q = ''
               d = 0
               w = 0
               g = []
               for e in id :
                   e = e[0]
                   delete_but = KeyboardButton(text='❌' + str(e))
                   r = []
                   r.append(delete_but)
                   g.append(r)
                   w += 1
                   price = cur.execute('''
                   SELECT COST
                   FROM korzina
                   WHERE TG_ID ='{}' and ZAKAZ ='{}'
                   '''.format(user_id, e)).fetchall()
                   kolich = cur.execute('''
                   SELECT KOLICH
                   FROM korzina
                   WHERE TG_ID ='{}' and ZAKAZ ='{}'
                   '''.format(user_id, e)).fetchall()
                   price = price[0][0]
                   kolich = kolich[0][0]
                   d+= kolich*price
                   q+=str(w)+'.'+str(e)+ ' - '+str(price)+' x '+ str(kolich)+' = '+str(price*kolich) +'\n'




               zakaz_but = [KeyboardButton(text=dct[lang_][17])]
               zakaz_but2 = [KeyboardButton(text=dct[lang_][18]),
                   KeyboardButton(text=dct[lang_][16])]
               g.insert(0,[KeyboardButton(text=dct[lang_][18]), KeyboardButton(text=dct[lang_][16]) ])
               g.insert(0, [KeyboardButton(text=dct[lang_][17])])
               if lang_ == 1 and w != 0:
                   context.bot.send_message(chat_id=user_id,
                                            text='👤Имя: {}\n📞Номер телефона: {}\n\n'.format(a_name, tel_nomer) +
                                                 dct[lang_][7][1:].upper() + '\n\n' + q + '\n\nИтого:  {} {}'.format(d,
                                                                                                                     dct[
                                                                                                                         lang_][
                                                                                                                         20]),
                                            reply_markup=ReplyKeyboardMarkup(g, resize_keyboard=True))
               elif lang_ == 2 and w != 0:
                   context.bot.send_message(chat_id=user_id,
                                            text='👤Ismi: {}\n📞Telefon raqami: {}\n\n'.format(a_name, tel_nomer, ) +
                                                 dct[lang_][7][1:].upper() + '\n\n' + q + '\n\nJami:  {} {}'.format(d,
                                                                                                                    dct[
                                                                                                                        lang_][
                                                                                                                        20]),
                                            reply_markup=ReplyKeyboardMarkup(g, resize_keyboard=True))
               else:
                   if lang_ == 1:

                       context.bot.send_message(chat_id=user_id, text='Корзина пустая☹️')
                   if lang_ == 2:


                       context.bot.send_message(chat_id=user_id, text='''Korzina bo'sh☹️''')
        except Exception:
            if lang_ == 1:
               context.bot.send_message(chat_id=user_id, text='Корзина пустая☹️')
            if lang_ == 2:
                context.bot.send_message(chat_id=user_id, text='''Korzina bo'sh☹️''')

    if message[0] == '❌' and stage_<100 :

        cur.execute("""
        DELETE  FROM korzina WHERE TG_ID = '{}' and ZAKAZ = '{}' 
        """.format( user_id, message[1:]))
        connect.commit()
        try:
            id = cur.execute('''
               SELECT ZAKAZ
               FROM korzina
               WHERE TG_ID ='{}'
               '''.format(user_id)).fetchall()

            q = ''
            d = 0
            w = 0
            g = []
            for e in id:
                e = e[0]
                delete_but = KeyboardButton(text='❌' + str(e))
                r = []
                r.append(delete_but)
                g.append(r)
                w += 1
                price = cur.execute('''
                   SELECT COST
                   FROM korzina
                   WHERE TG_ID ='{}' and ZAKAZ ='{}'
                   '''.format(user_id, e)).fetchall()
                kolich = cur.execute('''
                   SELECT KOLICH
                   FROM korzina
                   WHERE TG_ID ='{}' and ZAKAZ ='{}'
                   '''.format(user_id, e)).fetchall()
                price = price[0][0]
                kolich = kolich[0][0]
                d += kolich * price
                q += str(w) + '.' + str(e) + ' - ' + str(price) + ' x ' + str(kolich) + ' = ' + str(
                    price * kolich) + '\n'


            zakaz_but = [KeyboardButton(text=dct[lang_][17])]
            zakaz_but2 = [KeyboardButton(text=dct[lang_][18]),
                          KeyboardButton(text=dct[lang_][16])]
            g.insert(0, [KeyboardButton(text=dct[lang_][18]), KeyboardButton(text=dct[lang_][16])])
            g.insert(0, [KeyboardButton(text=dct[lang_][17])])
            if lang_ == 1 and w != 0:
                context.bot.send_message(chat_id=user_id,
                                         text='👤Имя: {}\n📞Номер телефона: {}\n\n'.format(a_name, tel_nomer) +
                                              dct[lang_][7][1:].upper() + '\n\n' + q + '\n\nИтого:  {} {}'.format(d,
                                                                                                                  dct[
                                                                                                                      lang_][
                                                                                                                      20]),
                                         reply_markup=ReplyKeyboardMarkup(g, resize_keyboard=True))
            elif lang_ == 2 and w != 0:
                context.bot.send_message(chat_id=user_id,
                                         text='👤Ismi: {}\n📞Telefon raqami: {}\n\n'.format(a_name, tel_nomer, ) +
                                              dct[lang_][7][1:].upper() + '\n\n' + q+ '\n\nJami:  {} {}'.format(d,
                                                                                                                  dct[
                                                                                                                      lang_][
                                                                                                                      20]),
                                         reply_markup=ReplyKeyboardMarkup(g, resize_keyboard=True))

            else:
                if lang_ == 1:
                    back_bu = [KeyboardButton(text=dct[lang_][16])]
                    context.bot.send_message(chat_id=user_id, text='Корзина пустая☹️',
                                             reply_markup=ReplyKeyboardMarkup([back_bu], resize_keyboard=True))
                if lang_ == 2:
                    back_bu = [KeyboardButton(text=dct[lang_][16])]
                    context.bot.send_message(chat_id=user_id, text='''Korzina bo'sh☹️''',
                                             reply_markup=ReplyKeyboardMarkup([back_bu], resize_keyboard=True))

        except Exception:
            if lang_ == 1:
               back_bu = [KeyboardButton(text=dct[lang_][16])]
               context.bot.send_message(chat_id=user_id, text='Корзина пустая☹️', reply_markup=ReplyKeyboardMarkup([back_bu], resize_keyboard=True))
            if lang_ == 2:
                back_bu = [KeyboardButton(text=dct[lang_][16])]
                context.bot.send_message(chat_id=user_id, text='''Korzina bo'sh☹️''', reply_markup=ReplyKeyboardMarkup([back_bu], resize_keyboard=True))

    if message==dct[lang_][17] and user_id == Tg:
        pay_key = [KeyboardButton(text=dct[lang_][30]), KeyboardButton(text=dct[lang_][31])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][28], reply_markup=ReplyKeyboardMarkup([pay_key], resize_keyboard=True))

    if message==dct[lang_][30]  or message==dct[lang_][31] :
        pay_key = [KeyboardButton(text=dct[lang_][30]), KeyboardButton(text=dct[lang_][31])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][29], reply_markup=ReplyKeyboardRemove([pay_key], resize_keyboard=True))
        cur.execute(upd_BILL.format(message, user_id))
        connect.commit()
        cur.execute(stagee.format('{}', user_id).format(10))
        connect.commit()

    if message not in dct[lang_][30:31] and stage_ ==10:
        cur.execute(upd_DATATIME.format(message, user_id))
        connect.commit()
        data = cur.execute(select_DATATIME.format(user_id)).fetchall()
        data = data [0][0]
        back_bu = [KeyboardButton(text=dct[lang_][16])]
        id = cur.execute('''
               SELECT ZAKAZ
               FROM korzina
               WHERE TG_ID ='{}'
               '''.format(user_id)).fetchall()
        q = ''
        d = 0
        w = 0
        g = []
        for e in id:
            e = e[0]
            delete_but = KeyboardButton(text='❌' + str(e))
            r = []
            r.append(delete_but)
            g.append(r)
            w += 1
            price = cur.execute('''
               SELECT COST
               FROM korzina
               WHERE TG_ID ='{}' and ZAKAZ ='{}'
               '''.format(user_id, e)).fetchall()
            kolich = cur.execute('''
               SELECT KOLICH
               FROM korzina
               WHERE TG_ID ='{}' and ZAKAZ ='{}'
               '''.format(user_id, e)).fetchall()
            price = price[0][0]
            kolich = kolich[0][0]
            d += kolich * price
            q += str(w) + '.' + str(e) + ' - ' + str(price) + ' x ' + str(kolich) + ' = ' + str(
                price * kolich) + '\n'
        check = '👤Имя: {}\n📞Номер телефона: {}\nМагазин: {}\nДолжность заказчика: {}\nСпособ оплаты: {}\nАдрес: {} \nДата доставки: {}\n\n'.format(a_name, tel_nomer,diller_name,diller_man,pay_way,diller_adress, data) +dct[lang_][7][1:].upper() + '\n\n' + q + '\n\nИтого:  {} {}'.format(d,
                                                                                                                  dct[
                                                                                                                      lang_][
                                                                                                                      20])
        context.bot.send_message(chat_id=-750027091, text=check)
        context.bot.send_message(chat_id=user_id, text=dct[lang_][32], reply_markup=ReplyKeyboardMarkup([back_bu], resize_keyboard=True))
        cur.execute(stagee.format('{}', user_id).format(6))
        connect.commit()
        cur.execute("""
           DELETE  FROM korzina WHERE TG_ID = '{}'
           """.format(user_id))
        connect.commit()

    if message == dct[lang_][18]:
            cur.execute("""
               DELETE  FROM korzina WHERE TG_ID = '{}'
               """.format(user_id))
            connect.commit()
            back = [KeyboardButton(text=dct[lang_][16])]
            context.bot.send_message(chat_id=user_id, text=dct[lang_][11],
                                     reply_markup=ReplyKeyboardMarkup([back], resize_keyboard=True))


#     KKOOOORRRRRZZZZIIINNNNAAAA TUGADII
    ddd = []
    for e in tgcheck:
        e = e[0]
        ddd.append(e)

    if user_id not in ddd:
        _but = [KeyboardButton(text=dct[lang_][33])]
        context.bot.send_message(text=dct[lang_][33], chat_id=user_id,
                                 reply_markup=ReplyKeyboardRemove([_but], resize_keyboard=True,
                                                                  one_time_keyboard=True))
    ddd.clear()


    if user_id in admdict and stage_ ==100 and message == maindct[lang_][4] or user_id in admdict and stage_ ==102 and message == maindct[lang_][4] :
        dd = [KeyboardButton(text='➕Добавить➕'),KeyboardButton(text='❌Удалить❌')]
        dd1 = [KeyboardButton(text='➕Добавить клиента➕'), KeyboardButton(text='❌Удалить клиента❌')]
        context.bot.send_message(chat_id=user_id, text='Админ меню', reply_markup=ReplyKeyboardMarkup([dd, dd1], resize_keyboard=True))
        cur.execute(stagee.format('{}', user_id).format(101))
        connect.commit()
    # UUUUUUUDDDDDDAAAAAAALLLLLLIIIITTTTTTT
    if user_id in admdict and stage_ ==101 and message == '❌Удалить❌'  or user_id in admdict and stage_ ==103.2 and message == '❌Удалить❌' or user_id in admdict and stage_ == 103.2 and message == '❌Удалить❌' :
        gg.clear()
        cur.execute(stagee.format('{}', user_id).format(102))
        connect.commit()
        tovar = cur.execute('''SELECT {} FROM Menyu '''.format(ll)).fetchall()
        price_m = cur.execute('''SELECT PRICE FROM Menyu''').fetchall()
        tovar_list = []
        price_list = []
        tovar_list.append(tovar)

        buttons = []
        tovar_list = tovar_list[0]

        def func_chunks_generators(lst, n):
            for i in range(0, len(lst), n):
                yield lst[i: i + n]

        tovar_list = list(func_chunks_generators(tovar_list, 2))

        for e in tovar_list:
            b = []
            for k in e:
                k = k[0]
                a = KeyboardButton(text='❌'+str(k))
                b.append(a)
            buttons.append(b)
        buttons.insert(0,[KeyboardButton(text='Админ меню')])


        context.bot.send_message(chat_id=user_id, text='Админ меню',
                                 reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))
    if user_id in admdict and stage_==102 and message[0]=='❌' and message[-1]!='❌':
        gg.clear()
        p_id = cur.execute("""SELECT PHOTO_1 FROM Menyu WHERE {} = "{}" """.format(ll, message[1:])).fetchall()
        p_id = p_id [0][0]
        import os
        if os.path.isfile('photo_base/{}.jpeg'.format(p_id)):
             os.remove('photo_base/{}.jpeg'.format(p_id))
             print("success")
        else:
             print("File doesn't exists!")
        cur.execute("""
        DELETE  FROM Menyu WHERE {} = '{}'  
        """.format(ll, message[1:]))
        connect.commit()

        tovar = cur.execute('''SELECT {} FROM Menyu '''.format(ll)).fetchall()
        price_m = cur.execute('''SELECT PRICE FROM Menyu''').fetchall()
        tovar_list = []
        price_list = []
        tovar_list.append(tovar)

        buttons = []
        tovar_list = tovar_list[0]

        def func_chunks_generators(lst, n):
            for i in range(0, len(lst), n):
                yield lst[i: i + n]

        tovar_list = list(func_chunks_generators(tovar_list, 2))

        for e in tovar_list:
            b = []
            for k in e:
                k = k[0]
                a = KeyboardButton(text='❌'+str(k))
                b.append(a)
            buttons.append(b)
        buttons.insert(0,[KeyboardButton(text='Админ меню')])
        context.bot.send_message(chat_id=user_id, text='🧹💨🗑', reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))
    if message != '❌Удалить❌➕' and   user_id in admdict and stage_ == 101 and message == '➕Добавить➕' or user_id in admdict and stage_ == 103.2 and message == '➕Добавить➕':
        cur.execute(stagee.format('{}', user_id).format(103.01))
        connect.commit()
        gg.clear()

        sss = ['w']
        context.bot.send_message(chat_id=user_id, text='1.{}\n2.{}\n3.{}\n4.{}'.format(cdct[lang_][0], cdct[lang_][1], cdct[lang_][2], cdct[lang_][3]) ,reply_markup=ReplyKeyboardRemove([sss], resize_keyboard=True))
    message = update.message.text
    if   message != '❌Удалить❌➕' and  message!='➕Добавить➕' and stage_ ==103.01 and 0<int(message)<5:
        gg.append(message)
        cur.execute(stagee.format('{}', user_id).format(103.001))
        connect.commit()
        context.bot.send_message(chat_id=user_id, text='Введите название продукта на русском:')
    message = update.message.text
    if  message != '❌Удалить❌➕' and  message!='➕Добавить➕' and stage_ ==103.001:
        cur.execute(stagee.format('{}', user_id).format(103.1))
        connect.commit()
        gg.append(message)

        context.bot.send_message(chat_id=user_id, text='''Maxsulotni nomini kiriting o'zbek tilida:''')
    message = update.message.text
    if message != '❌Удалить❌➕' and   message != '➕Добавить➕' and stage_ == 103.1 :
        gg.append(message)
        cur.execute(stagee.format('{}', user_id).format(103.2))
        connect.commit()
        context.bot.send_message(chat_id=user_id, text='Цена:')
    message = update.message.text
    if message != '❌Удалить❌➕' and  message != '➕Добавить➕' and stage_ == 103.2 :
        context.bot.send_message(chat_id=user_id, text='Отправтье фото товара с уникальным названием:')
        cur.execute(stagee.format('{}', user_id).format(103.3))
        connect.commit()
        gg.append(message)
        # h = gg
        #
        # for e in h:
        #     if e !='❌Удалить❌➕':
        #        gg.append(message)
        #        cur.execute(first_insert3.format(h[1],h[0],h[2]))
        #        connect.commit()
        #
        #        h.clear()
        #        dd = [KeyboardButton(text='➕Добавить➕'),KeyboardButton(text='❌Удалить❌')]
        #
        #        context.bot.send_message(chat_id=user_id, text='Админ меню', reply_markup=ReplyKeyboardMarkup([dd], resize_keyboard=True))

    if message == '➕Добавить клиента➕' and stage_ == 101:
        cur.execute(stagee.format('{}', user_id).format(105))
        connect.commit()
        sss = ['w']
        context.bot.send_message(chat_id=user_id, text='Введите Telegram_ID клиента:',reply_markup=ReplyKeyboardRemove([sss], resize_keyboard=True))
    if message!='➕Добавить клиента➕' and stage_ == 105:
        try:
            client_id = int(message)
            cur.execute(first_insert222.format(client_id))
            connect.commit()
            cur.execute(stagee.format('{}', user_id).format(101))
            connect.commit()
            context.bot.send_message(chat_id=user_id, text='✅Добавлено✅')
            dd = [KeyboardButton(text='➕Добавить➕'),KeyboardButton(text='❌Удалить❌')]
            dd1 = [KeyboardButton(text='➕Добавить клиента➕'), KeyboardButton(text='❌Удалить клиента❌')]
            context.bot.send_message(chat_id=user_id, text='Админ меню', reply_markup=ReplyKeyboardMarkup([dd, dd1], resize_keyboard=True))
        except Exception:
            context.bot.send_message(chat_id=user_id, text='Telegram_ID должен состоять только из цифр')
    if message == '❌Удалить клиента❌' and stage_ == 101:
        cur.execute(stagee.format('{}', user_id).format(106))
        connect.commit()
        sss = ['w']
        context.bot.send_message(chat_id=user_id, text='Введите Telegram_ID клиента, которого вы  хотите удалить:',reply_markup=ReplyKeyboardRemove([sss], resize_keyboard=True))
    if message != '❌Удалить клиента❌' and stage_ == 106:
        tg = cur.execute(get__id.format(message)).fetchall()
        try:
            tg = tg[0][0]
        except Exception:
            pass
        try:
            message =int(message)
        except Exception:
            context.bot.send_message(chat_id=user_id,
                                     text='ОШИБКА\nПользователя с таким Telegram_ID не существует в базе данных')
        if message == int(tg):
            try:
                client_id = int(message)
                cur.execute("""DELETE FROM Users_list WHERE TG_ID = "{}" """.format(client_id))
                connect.commit()
                cur.execute(stagee.format('{}', user_id).format(101))
                connect.commit()
                context.bot.send_message(chat_id=user_id, text='✅УДАЛЕНО✅')
                dd = [KeyboardButton(text='➕Добавить➕'), KeyboardButton(text='❌Удалить❌')]
                dd1 = [KeyboardButton(text='➕Добавить клиента➕'), KeyboardButton(text='❌Удалить клиента❌')]
                context.bot.send_message(chat_id=user_id, text='Админ меню',
                                         reply_markup=ReplyKeyboardMarkup([dd, dd1], resize_keyboard=True))
            except Exception:
                context.bot.send_message(chat_id=user_id, text='ОШИБКА\nПользователя с таким Telegram_ID не существует в базе данных')
        else:
            context.bot.send_message(chat_id=user_id,
                                     text='ОШИБКА\nПользователя с таким Telegram_ID не существует в базе данных')

def adm(update,context):
    user_id = update.message.chat_id
    connect = sqlite3.connect('b_users.sqlite')
    cur = connect.cursor()
    stage_ = cur.execute(stage.format(user_id)).fetchall()

    p_name = cur.execute("""SELECT PHOTO_1 FROM Menyu""").fetchall()
    try:
       stage_ = stage_[0][0]
       p_name = p_name[0]
    except Exception:
        pass

    for e in admdict:
     if user_id == e:
        text = update.message.caption

        if text == None:
            pass
        elif user_id in admdict and text not in p_name and stage_ == 103.3:
            photo_id = update.message.photo[-1].file_id
            file = context.bot.getFile(photo_id)
            file.download('photo_base/{}.jpeg'.format(text))

            gg.append(text)
            hh = gg
            cur.execute(first_insert3.format(hh[2], hh[1], hh[0], hh[4], hh[3]))
            connect.commit()
            hh.clear()
            cur.execute(stagee.format('{}', user_id).format(101))
            connect.commit()
            context.bot.send_message(chat_id=user_id, text='✅Добавлено✅')
            dd = [KeyboardButton(text='➕Добавить➕'),KeyboardButton(text='❌Удалить❌')]
            dd1 = [KeyboardButton(text='➕Добавить клиента➕'), KeyboardButton(text='❌Удалить клиента❌')]
            context.bot.send_message(chat_id=user_id, text='Админ меню', reply_markup=ReplyKeyboardMarkup([dd, dd1], resize_keyboard=True))
        elif user_id in admdict and text  in p_name and stage_ == 103.3:
            context.bot.send_message(chat_id=user_id, text='Фото с таким названием уже существует, отправтье фото с другим названием:')
        else:
            pass


        # elif text!= 'menu':
        #     try:
        #         photo_id = update.message.photo[-1].file_id
        #         file = context.bot.getFile(photo_id)
        #         file.download('Picture.jpeg')
        #         connect = sqlite3.connect('b_users.sqlite')
        #         cur = connect.cursor()
        #         id = cur.execute('''
        #         SELECT TG_ID
        #         FROM Users
        #         WHERE TG_ID !=0
        #         ''').fetchall()
        #         for e in id:
        #               e = e[0]
        #               context.bot.send_photo(photo= open('Picture.jpeg','rb'), chat_id=e, caption=text)
        #               sleep(1.5)
        #     except Exception:
        #             continue

def ru(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('b_users.sqlite')
    cur = connect.cursor()
    lang_choose = cur.execute(lang.format('{}', user_id).format(1)).fetchall()
    connect.commit()
    cur.execute(stagee.format('{}', user_id).format(2))
    connect.commit()
    k_but = [KeyboardButton(text='далее>>>')]
    context.bot.send_message(text='нажмите на кнопку далее...' , chat_id=user_id,  reply_markup=ReplyKeyboardMarkup([k_but], resize_keyboard=True, one_time_keyboard=True))
    cur.execute(''' UPDATE Users SET Lang_sql = '{}' WHERE TG_ID = '{}' '''.format('TOVAR_RU', user_id))
    connect.commit()
def uz(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('b_users.sqlite')
    cur = connect.cursor()
    cur.execute(lang.format('{}', user_id).format(2))
    connect.commit()
    cur.execute(stagee.format('{}', user_id).format(2))
    connect.commit()
    k_but = [KeyboardButton(text='davom etish>>>')]
    context.bot.send_message(chat_id=user_id, text='davom etamish tugmasini bosing...',  reply_markup= ReplyKeyboardMarkup([k_but], resize_keyboard=True, one_time_keyboard=True))
    cur.execute(''' UPDATE Users SET Lang_sql = '{}' WHERE TG_ID = '{}' '''.format('TOVAR_UZ', user_id))
    connect.commit()
def ru_change(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('b_users.sqlite')
    cur = connect.cursor()
    lang_choose = cur.execute(lang.format('{}', user_id).format(1)).fetchall()
    connect.commit()
    cur.execute(stagee.format('{}', user_id).format(5))
    connect.commit()
    k2_but = [KeyboardButton(text='🏠Главное меню')]
    context.bot.send_message(chat_id=user_id, text='🏠Нажмите на кнопку Главное меню...',
                             reply_markup=ReplyKeyboardMarkup([k2_but], resize_keyboard=True))
    cur.execute(''' UPDATE Users SET Lang_sql = '{}' WHERE TG_ID = '{}' '''.format('TOVAR_RU', user_id))
    connect.commit()
def uz_change(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('b_users.sqlite')
    cur = connect.cursor()
    cur.execute(lang.format('{}', user_id).format(2))
    connect.commit()
    cur.execute(stagee.format('{}', user_id).format(5))
    connect.commit()
    k1_but = [KeyboardButton(text='🏠Asosiy menyu')]
    context.bot.send_message(chat_id=user_id, text='🏠Asosiy menyu tugmasini bosing...',  reply_markup= ReplyKeyboardMarkup([k1_but], resize_keyboard=True))
    cur.execute(''' UPDATE Users SET Lang_sql = '{}' WHERE TG_ID = '{}' '''.format('TOVAR_UZ', user_id))
    connect.commit()
def get_contac(update, context):
    user_id = update.message.chat_id
    num = update.message.contact.phone_number
    num = str(num)
    conn = sqlite3.connect('b_users.sqlite')
    cur = conn.cursor()
    cur.execute(update_phone_num.format(num, user_id))
    conn.commit()
    cur.execute(stagee.format('{}', user_id).format(6))
    conn.commit()


    lang_ = cur.execute(lang_select.format(user_id)).fetchall()
    conn.commit()

    lang_ = lang_[0][0]

    main_button = [KeyboardButton(text=maindct[lang_][0]),
                   KeyboardButton(text=maindct[lang_][1])]
    main_button1 = [KeyboardButton(text=maindct[lang_][2])]

    context.bot.send_message(chat_id=user_id, text=dct[lang_][16]+':',
                             reply_markup=ReplyKeyboardMarkup([main_button,
                                                               main_button1], resize_keyboard=True))
