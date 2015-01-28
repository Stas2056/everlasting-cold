﻿init:
    $ sm = Character(u'Семпай', color="#920000", what_color="E2C555", drop_shadow = [ (-1, -1), (1, -1), (-1, -1), (1, -1) ], drop_shadow_color = "#000")
    $ li = Character(u'Лиза', color="#920000", what_color="E2C555", drop_shadow = [ (-1, -1), (1, -1), (-1, -1), (1, -1) ], drop_shadow_color = "#000")
    $ mods["SirVilat"] = u"Бесконечный Холод"
    
    image bg home = "mods/SirVilat/image/room_1.jpg"
   #  image ss_li = "mods/sirvilat/image/sprites/lisa.png"
 
label SirVilat:
    $ prolog_time()
    $ persistent.sprite_time = "day"
 
    # {w}text   -слово текст еапичатается не сразу  
    # {i}{/i} -курсив
 
# Дописал холод и лег спать
    play music  music_list["sunny_day"] fadein 1
    scene bg semen_room
    "Я дописал очередной черновик следующей серии Холода, который наврняка будет еще много раз переписан и в итоге от проделанной работы не останется и следа"
    "На часах светилось 6:21 утра"
    th "Наверное, пора уже и спать ложиться. К черту этот Холод, к черту Лизу эту проклятую - я все равно как был форевеалоуном, так и останусь"
    "Можно было еще пройти какой-нибдуь рут из мода для Бесконечного Лета напоследок, но и его я послал к черту"
    th "И без Лета хоть вскрывайся {i} - думал я, брякнувшись в кровать.{/i}"
    "Сон долго не шел, я ворочался с бока на бок, а мысли скакали с одного на другое, ни на чем толком не сосредотачиваясь"
    "размытые образы новых сцен Холода мутно плавали перед глазами, мелькала Лиза в разных эпизодах, обличиях"
    "Я наконец-то заснул."
    
    
# Прибытие (Сплэш монитора с фразой "прибытие"

# Очнулся в автобусе
    play music  music_list["door_to_nightmare"] fadein 1
    show unblink
    scene bg int_bus 
    with dissolve2 
    "Еще не открыв глаза я уже почуял неладное - тело затекло в сидячей позе"
    th "Ну не в новом же кресле я вчера уснул - мелькнула мысль"
    "Все быстро стало ясно, а точнее нифига не ясно - я сидел в автобусе, чей номер молниеностно всплыл в памяти. Я вроде не Семен, так какого чёрта я тут очутился?"
    sm "Ну ахереть теперь"
    "Только и сказал я."
    th "Нет, я конечно мечтал попасть на месте дауна-Семена, но как-то не особо был к этому готов. С другой стороны, это место было мне как родное и вряд ли чем-то удивит, да и бояться нечего"

# Вырубить музыку
    stop music fadeout 3
# Вышел, увидел Семена   
    scene bg ext_bus 
    with dissolve2
    "Оказавшись на свежем водухе под палящим солнцем я тут же увидел и главного героя всей истории - Семена. Он валялся на асфальте и отвратительно ревел навзрыд" 
    play ambience sfx_lena_hits_alisa 
    with vpunch
    stop ambience
    "Без лишних раздумий я смачно пнул ДЦПщника по хребту и отскочил за один из постоментов"
    scene cg d6_pioneer
    th "Эх, надо было пнуть дважды - все-равно он бы не успел заметить"

# Славя пришла    Не-настолько-треш коммит
    scene ext_camp_entrance_day 
    show sl normal casual at right
    sl "Вот так храбрец! Незнакомого человека ударить, да ещё и лежачего"
    я "А какого хрена этот паникёр тут сопли развешивает с утра пораньше? "
    sl "А если бы ты ему сломал что-то? Не подумал,а?"
    я "Ладно, всё-равно ничего страшного я не сделал.Идю сюда, жертва избиения!"
    th "Тем временем Семёшка уже тихо сбегал отсюда"
    я"Остановись, идиот!"
    "Он не послушал и бежал постоянно оглядываясь"
    "Зря.Он благополучно споткнулся о камень и влетел головой в рядом стоящее дерево"
    th "А я, как будто, ждал от этого комнтатного попаданца чего-то другого?Славя смотрела на меня с немым укором, но после феерического полёта Семёна она, скорее всего поняла, что этого бедового и трогать-то не нужно, сам себе проблемы создаст."
# Вернулись полным составом к воротам
    sl "И всё-таки я не понимаю... Ну зачем? Что он тебе такого сделал?"
    th "Вот рассказал бы я, как от его идиотизма в твоём руте у меня припекло - сразу бы поняла."
    я "А тебе не кажется странным, почему вполне взрослый парень без видимой причины ведёт себя, как дитя малое? Заговорить с ним в этот момент и так не получилось бы. 
    я "В лучшем случае - точно так же припустил бы, а то и вовсе на меня набросился. А так - вот стоит теперь спокойный"    
    th "Как-то даже не подумал, что в этот самый момент предмет нашего разговора стоял рядом, потупив взгляд."
    se "Что ты тут вообще делаешь? Как ты попал сюда?! Я весь автобус осмотрел!"
    th "Хоть я и был не совсем в своей тарелке - не каждый же день попадаешь в любимую игру! - до истерического исступления этого парня мне было далеко."
    я "На автобусе приехал, как же ещё. Или ты знаешь другой способ попасть в пионерлагерь?"
    th "Я заметил, что губы Слави тронула чуть заметная улыбка. Что же это может значить? Возможно, её повеселила странность вопросов Семёна."
    th "Или она распознала мою самоиронию, хотя, как же гротескна была эта ситуация. Она тоже обычный человек, и подобные саркастические ответы не должны её насторожить."
    sl "Хватит нести чушь! Успокойтесь."
    th "Улыбка, спустя несколько мгновений неловкого молчания, пропала бесследно.За ней оказалась любовь к дисциплине и неприятие конфликта."
    sl "И вообще, извинись!Чтоб ты там не говорил - ты без причины ударил человека, а лагерь - не место для ненужных ссор."
    я "Ну, извини."
    th "На большее просто не хватило фантазии. Надеюсь, в ознаменование перемирия нас не заставят обнятся."
    th " Семён хмыкнул и ничего не ответил."
    sl "Ну вот и хорошо, мир. А теперь давайте знакомиться!"
    th "Как же быстро для неё пропадают следы негатива. Вот минуту назад я и не подумал бы о бескровном перемирии."
    sl " Вот тебя как зовут?"
    th "Первым она обратилась к Сёме - видимо, пыталась отвлечь его внимание."
    se "Ну...Семён.."
    th "Не хотелось растягивать этот разговор, поэтому я взял инициативу в свои руки."
    я "Очень приятно, Сергей."
    th "На попытку пожать руки он отреагировал , отстранившись, но Славин настойчивый взгляд заставил его пересилить страх."
    sl "Ну вот и славно! А меня Славей зовут. Полное имя Славяна, но все зовут меня Славей,и вы тоже зовите!"
    sl "А теперь идите к Ольге Дмитриевне, да побыстрее. Вы и так здесь много времени потеряли. На площади поверните налево, там будет её домик."
    th "И не успел Семён задать какой-нибудь из своих дурацких вопросов, ка Славя скрылась за воротами. Как же она всё-таки мила! Даже к этому юродивому так хорошо относиться."
    я "Пошли!"
    th "Без этого чёткого приказа он бы стоял здесь еще несколько минут, пораженный произошедшим."
    
