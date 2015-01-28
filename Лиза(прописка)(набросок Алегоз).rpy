init:
    $ mods["alegoztest"]=u"alegoztest"                               ## Мой файл вместо alegoztest впихиваем наше
    $ Lisa = Character(u'Лиза',color="#920000")                      ## Объявили Лизу  
    image lis = "alegoztest/sprites/li_casual.png"                   ## Объявили спрайт Лизы (папка мода лежит в папке game) Использовать только "/" если "\" = Краш
    
label alegoztest:
    scene bg int_house_of_mt_day                                     ## Сцена
    play music music_list["my_daily_life"]                           ## Музыка
    show lis ## Показываем лизу в центре  P.S. at center - центрируется(обрезаные ноги видно) без центрирования норм
 
    "Вау!!"
    Lisa "Твой мод супер"
    me "Я знаю!"
 
    
    
    return
