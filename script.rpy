# Вы можете расположить сценарий своей игры в этом файле.

#
# Определение персонажей игры.
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy - "eileen happy.webp", и тогда они появятся в игре.

init python:

    def piece_dragged(drags, drop):

        if not drop:
            return

        p_x = drags[0].drag_name[0]
        p_y = drags[0].drag_name[1]
        t_x = drop.drag_name[0]
        t_y = drop.drag_name[1]

        a = []
        a.append(drop.drag_joined)
        a.append((drags[0], 3, 3))
        drop.drag_joined(a)

        if p_x == t_x and p_y == t_y:
            my_x = int(int(p_x)*active_area_size*x_scale_index)-int(grip_size*x_scale_index)+puzzle_field_offset
            my_y = int(int(p_y)*active_area_size*y_scale_index)-int(grip_size*y_scale_index)+puzzle_field_offset
            drags[0].snap(my_x,my_y, delay=0.1)
            drags[0].draggable = False
            placedlist[int(p_x),int(p_y)] = True

            for i in range(0, grid_width):
                for j in range(0, grid_height):
                    if placedlist[i,j] == False:
                        return
            return True
        return


screen jigsaw:


    add im.Scale("_puzzle_field.png", img_width, img_height) pos(puzzle_field_offset, puzzle_field_offset)

    draggroup:

        for i in range(0, grid_width):
            for j in range(0, grid_height):
                $ name = "%s%s"%(i,j)
                $ my_x = i*int(active_area_size*x_scale_index)+puzzle_field_offset
                $ my_y = j*int(active_area_size*y_scale_index)+puzzle_field_offset
                drag:
                    drag_name name
                    child im.Scale("_blank_space.png", int(active_area_size*x_scale_index), int(active_area_size*y_scale_index) )
                    draggable False
                    xpos my_x ypos my_y


        for i in range(0, grid_width):
            for j in range(0, grid_height):
                $ name = "%s%s piece"%(i,j)
                drag:
                    drag_name name
                    child imagelist[i,j]
                    #droppable False
                    dragged piece_dragged
                    xpos piecelist[i,j][0] ypos piecelist[i,j][1]





label puzzle:
    call screen jigsaw
    jump win


init:
    $ hero = Character ("[povname]", color= "#c8ffc8")
    $ barman = Character ("Бармен")
    $ gadalka = Character ("Гадалка")
    $ gender = "maleHero"
    $ friend = Character ("Незнакомец")
    $ mifana = Character ("Мифана")
    $ orakul = Character ("Оракул")
    $ dip_god = Character ("Бог Димпломатии")
    $ liar_god = Character ("Бог Лжи")
    $ truth_god = Character ("Бог Правды")
    $ jildar = Character ("Жальдар")
    $ mage = Character ("Мальширус")
    image realhero = "images/[gender].png"
# Игра начинается здесь:
label start:

scene square:
    zoom 0.35
show malehero at right:
    zoom 0.2
show femalehero at left:
    zoom 0.2

python:
    povname = renpy.input("Как тебя зовут?")
    povname = povname.strip()

    if not povname:
         povname = "Джo Доу"

hero "Меня зовут [povname]!"

menu:
    "За кого вы хотите играть?"
    "Парень":
        pass
    "Девушка":
        $ gender = "femaleHero"

image realhero = "images/[gender].png"

if gender == "femaleHero":
    hide malehero with dissolve
else:
    hide femalehero with dissolve

hero "Что это за место? Почему я не могу выйти из этого городка?"
hero "Думаю стоит обратиться за помощью."

"Вы заходите в ближайшее заведение. Им оказывается бар."

scene taverna with fade:
    zoom 0.35
show barman at left:
    zoom 0.25
show realhero at right:
    zoom 0.2
barman "Приветствую тебя, путник! Давно же я не видел здесь новых лиц, какими ветрами тебя занесло сюда?"
hero "Да вот случайно. Как ни стараюсь, не могу вспомнить этот город."
barman "Говоришь, не знаешь о городе, да? Что же, раньше я бы сказал, что это невозможно, но сейчас..."
hero "А почему невозможно?"
hide realhero with moveinright
show barman at center with moveinleft
barman "Видишь ли, так было не всегда. Наш город не такой уж и большой, и тут все друг друга знают. Так было и до этого проклятья, которым нас наградил здешний волшебник."
hero "Неужели вы ему сильно чем-то насолили?"
barman "Да не сказал бы. Конечно, тут есть и наша вина, но далеко не вся. Дело вот было в чём: этот волшебник жил в высокой башне, по сравнению с другими постройками, ну в очень высокой."
barman "В гости, насколько я слышал, к нему приходили нечасто. Даже случайно проходившие мимо путники, ищущие кров, не рисковали подниматься."
hero "И почему же? Неужели из-за большого количества ступенек?"
barman "Это, конечно, играло немаленькую роль, но основная причина была другой."
barman "В то время он начал вести себя как-то иначе: всё реже спускался со своей башни, меньше общался со своими друзьями, его жилище начинало преображаться в нечто недоброе."
barman "Прошел месяц, другой, и его друзья хотели уже его проведать, но поднялся сильный ветер, над шпилем его башни стали собираться дождевые тучи, всё загромыхало."
barman "В конце концов башня обрушилась и появился магический барьер, сквозь который нам не удалось выбраться, а люди снаружи будто нас не видели и проходили мимо."
show realhero at right with moveinright:
    zoom 0.2
show barman at left with moveinright
hero "А вы пробовали поговорить с волшебником?"
barman "Попробовали бы, но никто после того дня его не видел."
hero "Получается, я теперь не смогу вернуться домой?"
if gender == "maleHero":
    barman "Я бы согласился, если бы не тот факт, что ты как-то смог попасть внутрь. Может, именно ты сможешь разрушить этот барьер. Происходило ли что-то необычное, когда ты попал в город?"
else:
    barman "Я бы согласился, если бы не тот факт, что ты как-то смогла попасть внутрь. Может, именно ты сможешь разрушить этот барьер. Происходило ли что-то необычное, когда ты попала в город?"
hero "Не припомню чего-нибудь такого."
barman "Хмм... А знаешь тебе, наверно, стоило бы заглянуть к местной гадалке, может расскажет чего-нибудь, чего я не знаю, он в магии побольше меня знает."
hero "А почему вы к нему не обращались до меня, быть может всё уже смогли бы разрешить?"
barman "Да он никому не говорил ничего, кроме {i}«Время ещё не пришло...».{/i} Может, теперь пришло время, когда кто-то смог пройти сквозь защиту."
hero "Тогда я прямо сейчас и пойду к нему. Стоп, а где он живёт, не подскажешь?"
barman "Он необычный житель городка, и бывает много где, но в основном его встречают либо в парке, либо возле книжного магазина, тут рядом."
hero "Ясно, спасибо за ценную информацию, мне надо скорее идти!"
barman "Пожалуйста, и удачи, она тебе пригодится!"
scene park with fade:
    zoom 0.35
show realhero at left with moveinleft:
    zoom 0.2
show gadalka at right with moveinright:
    zoom 0.25
hero "Простите, а вы случаем не гадалка, больно на него похожи?"
gadalka "Да, это я. Думаю, тебя интересует, как разрушить барьер и выбраться из этого городка."
hero "Прямо в точку."
if gender == "maleHero":
    gadalka "Ну тогда слушай, я хочу убедиться, что ты сможешь справиться со всеми препятствиями, поэтому будь добр, сходи в один клуб, что находится недалеко отсюда, и передай это письмо одному моему знакомому."
else:
    gadalka "Ну тогда слушай, я хочу убедиться, что ты сможешь справиться со всеми препятствиями, поэтому будь добра, сходи в один клуб, что находится недалеко отсюда, и передай это письмо одному моему знакомому."
"{i}Гадалка отдаёт вам конверт.{/i}"
gadalka "Ты его сразу узнаешь, поверь мне. Ох, и ещё, чуть не забыл, клуб закрытый, нужен пароль."
gadalka "Я сам там не был, но кое-что про пароль знаю. {color=#44944A}{i}«На окне, на полке, что-то растёт с иголками, да с цветами атласными, яркими и красными».{/i}{/color} Забавно, а теперь иди."

scene fasad taverna with fade:
    zoom 0.6
menu:
    "Постучать":
        pass
"{i}Вы постучали. Послышался шум возле двери.{/i}"
"Незнакомец" "Пароль?"
python:
    password = renpy.input("")
    password = password.strip().lower().replace(" ", "")
    while password != "кактус":
        password = renpy.input("{b}{color=#f00}Это неверный пароль.{/color}{/b}{vspace=15}")
        password = password.strip().lower().replace(" ", "")

"{i}Дверь приоткрылась. Наружу вышел искусно одетый молодой парень с синими волосами.{/i}"
show friend at center with dissolve:
    zoom 0.25
hero "Здравствуйте, вам письмо от гадалки."
friend "Хм... Нашли меня значит. Молодец, держи, это тебе понадобится."
"{i}Незнакомец отдает вам браслет.{/i}"
hide friend with dissolve
show realhero at left with dissolve:
    zoom 0.2
hero "Так, стоит вернуться к гадалке."

scene library with fade:
    zoom 0.35
show gadalka at right with dissolve:
    zoom 0.25
show realhero at center with moveinleft:
    zoom 0.2
gadalka "Уже? Ты быстро!"
hero "Он получил письмо, как ты и просил, взамен он мне дал этот браслет, он твой?"
menu:
    "Отдать браслет гадалке":
        pass
gadalka "Да, когда-то мне его подарил местный волшебник, сказал, что он очень важен, как и два других, которые он отдал своим друзьям, просил сохранить до нужного случая, и вот, получается тот самый случай и настал."
gadalka "Теперь тебе нужно найти двух других знакомых чародея и собрать все три браслета вместе, думаю, что тогда что-то должно проясниться."
hero "Ладно, но как мне найти двух других друзей?"
gadalka "Тебе наверняка уже встретился кое-кто, кто знает каждого жителя."
hero "Не понима... А, Бармен, точно, спасибо тебе за всё, до встречи!"

scene taverna with fade:
    zoom 0.35
show barman at left with dissolve:
    zoom 0.25
show realhero at right with dissolve:
    zoom 0.2
barman "И снова здравствуй! По делу или просто нужен отдых?"
hero "Совмещу приятное с полезным. Сделай, пожалуйста, виноградный сок."
barman "Ну, как успехи?"
if gender == "maleHero":
    hero "Они определённо есть, я получил один из 3 браслетов, непонятно правда, как они мне помогут, но я уверен, что ты сможешь помочь с кое-чем?"
else:
    hero "Они определённо есть, я получила один из 3 браслетов, непонятно правда, как они мне помогут, но я уверена, что ты сможешь помочь с кое-чем?"
barman "Да, и с чем же?"
hero "Помнишь, ты мне рассказывал, что у волшебника были друзья?"
barman "Было дело."
hero "Так вот, не знаешь ли ты случаем, где они могут жить?"
barman "Хм... Ах да, скорее всего это Мифана и Жальдар."
barman "Первая на вид хоть и опрятная девушка, но вот любит ходить по пещерам, вход в которые находится в парке."
barman "Второй же, я бы сказал противоположность: взъерошенные волосы, носит одну и ту же одежду что дома, что на разного рода собраниях. И всё это при том, что он богат и мог бы себе позволить хоть каждый день менять одёжку."
barman "Единственное, на что он потратился, так это на дом и лабиринт из живой изгороди, который надо преодолеть, прежде чем попасть к нему в гости."
hero "М-да уж, странные у него друзья."

scene park with fade:
    zoom 0.35
show realhero at center with dissolve:
    zoom 0.2
hero "{i}«Где-то тут будет вход в пещеры»{/i}"
scene cave with fade:
    zoom 0.6
show realhero at left with dissolve:
    zoom 0.2
hero "{i}«Ух, а тут темно, надо быть осторожней»{/i}"
show mifana at right with moveinright:
    zoom 0.2
mifana "Не думала, что однажды тут кого-нибудь встречу."
hero "Ты же Мифана, верно?"
mifana "Да, так ко мне все и обращаются. Хочешь со мной тут погулять?"
hero "Боюсь, у меня нет на это времени, так что не судьба. Я здесь в поисках браслета, который вручил тебе волшебник."
mifana "О, вон оно как, и с чего бы это мне тебе его отдавать?"
hero "Ну у меня уже есть один браслет. Мне его отдал знакомый гадалки."
mifana "А, так тебе отдал его сам Липосий. Должно быть, у него были на то причины. Погоди-ка… Не ты ли тот самый путник, который оказался в нашем городке несмотря на проклятие?"
hero "Точно! Но откуда ты обо мне узнала?"
mifana "От Липосия слышала, он в последнее время предрекал нам явление незнакомца, что разрушит проклятье. Так вот, я отдам тебе браслет, но при одном условии."
hero "И при каком же?"
mifana "Браслет лежит в этой пещере, только его будет не так просто взять."
hero "Почему?"
mifana "Я решила его спрятать и разработала неплохую систему защиты. Пошли, покажу."
scene torches with fade:
    zoom 0.6
show realhero at left with dissolve:
    zoom 0.2
show mifana at right with dissolve:
    zoom 0.2
mifana "Мы пришли, всё, что нужно сделать, так это зажечь факелы в нужном порядке. Только я плохо запоминаю различные комбинации, так что записала их на этом листочке."
hero "Ну так прочитай, освежи память и зажги факела в нужном порядке."
mifana "Есть одно но, мне несколько сотен лет, и решать свои собственные загадки скучно, так что давай это сделаешь ты. О, и ещё обрати внимание на руны, которые появятся над факелами после разгадки."
hero "{i}«Попробую некоторые варианты»{/i}"
hide realhero with dissolve
hide mifana with dissolve
label riddle:
    show riddle at center with fade:
        zoom 0.15
    hero "{i}«И в каком же порядке их зажечь?»{/i}"
    hide riddle
    menu:
        "Зажечь верхний, правый, нижний, левый":
            jump badriddle
        "Зажечь левый, правый, верхний, нижний":
            jump badriddle
        "Зажечь нижний, верхний, левый, правый":
            jump goodriddle
        "Зажечь правый, верхний, левый, нижний":
            jump badriddle
label badriddle:
    scene torchesbad with fade:
        zoom 0.26
    "Ничего не произошло. Нужно затушить факелы и попробовать заново."
    jump riddle
label goodriddle:
    scene torchesgood with fade:
        zoom 0.6
    show realhero at left with dissolve:
        zoom 0.2
    show mifana at right with dissolve:
        zoom 0.2
    hero "Ура! Получилось!"
    mifana "Теперь ко второй загадке."
scene alchemy with fade:
    zoom 0.6
show realhero at left with dissolve:
    zoom 0.2
show mifana at right with dissolve:
    zoom 0.2
mifana "Посмотри, там должен быть листочек с подсказкой."
hero "Вижу."
hide realhero with dissolve
hide mifana with dissolve
centered "{i}«Недавно увлекался алхимией, и нашёл способ превращения кирпича в железо, для этого кирпич сначала надо нагреть. Теперь понадобится зелье {color=#44944A}жёлтого{/color} цвета, такого оттенка, какой можно увидеть на радуге. Получится оно таким, когда в воду положить кусочек особого кристалла, который имеет {color=#44944A}начальную{/color} фазу обращения в лунный камень, а {color=#44944A}второй{/color} и последний ингредиент - смола дуба»{/i}"
show realhero at left with dissolve:
    zoom 0.2
show mifana at right with dissolve:
    zoom 0.2
hero "{i}«Кажется, нужна комбинация цифр»{/i}"
python:
    code = renpy.input("")
    code = code.strip().replace(" ", "")
    while code != '312':
        code = renpy.input("{b}{color=#f00}Это неверный код.{/color}{/b}{vspace=15}")
        code = code.strip().replace(" ", "")
mifana "Верно. Можно вернуться обратно."
scene chest with fade:
    zoom 0.6
show realhero at left with dissolve:
    zoom 0.2
show mifana at right with dissolve:
    zoom 0.2
hero "Опять нужен код? И какой же?"
mifana "А я, кажется, говорила про руны."
python:
    code = renpy.input("")
    code = code.strip().replace(" ", "")
    while code != '2487':
        code = renpy.input("{b}{color=#f00}Это неверный код.{/color}{/b}{vspace=15}")
        code = code.strip().replace(" ", "")
mifana "Что же, теперь это твоё."
menu:
    "Забрать браслет":
        pass
mifana "Ну, теперь, я думаю, смысла нам торчать тут больше нет, пошли, я нас выведу."
hero "Веди."
scene park with fade:
    zoom 0.35
show realhero at left with dissolve:
    zoom 0.2
show mifana at right with dissolve:
    zoom 0.2
mifana "О, кстати, мы вышли недалеко от дома Жальдара, я так понимаю, ты к нему сейчас направишься."
hero "Да, а не подскажешь, как быстрее к нему пройти?"
mifana "Без проблем, иди по той дорожке, потом на втором повороте направо, после налево, прямо пока не упрёшься в табличку, где уже будет сказано, как к нему пройти."
hero "Слушай, а ты не могла бы меня проводить, мало ли сверну не туда."
if gender == "maleHero":
    mifana "Ну уж нет, ты справишься с этим сам, удачи в приключениях."
else:
    mifana "Ну уж нет, ты справишься с этим сама, удачи в приключениях."
hero "И на этом спасибо, Мифана."
mifana "Всегда пожалуйста!"
scene maze with fade:
    zoom 0.6
hero "{i}«Так, это место подходит под описание Бармена, ни ворот, ни охраны, только один лабиринт».{/i}"
"На входе стоит стол, на котором лежат кусочки пазла, и рядом находится записка..."
"«Я хочу, чтобы один из ключей к этим воротам был выделяющимся, с моим любимым существом - Минотавром»."
hero "{i}«Похоже, чтобы достать ключ, мне нужно разгадать пазл».{/i}"



scene expression "_20130709_192009.jpg" #Менять фон для пазла
$ grid_width = 4    # Это и ниже меняет сложность => увеличевает количество пазла, но повышает время ожидания
$ grid_height = 4
$ puzzle_field_size = 900
$ puzzle_field_offset = 30
$ puzzle_piece_size = 450
$ grip_size = 75
$ active_area_size = puzzle_piece_size - (grip_size * 2)
$ chosen_img = "puzzle.jpg "#Здесь менять картинку для пазла




    #####################################################################################################
    #
python:

    img_width, img_height = renpy.image_size(chosen_img)


        # scales down an image to fit the puzzle_field_size
    if img_width >= img_height and img_width > puzzle_field_size:
        img_scale_down_index = round( (1.00 * puzzle_field_size / img_width), 6)
        img_to_play = im.FactorScale(chosen_img, img_scale_down_index)
        img_width = int(img_width * img_scale_down_index)
        img_height = int(img_height * img_scale_down_index)

    elif img_height >= img_width and img_height > puzzle_field_size:
        img_scale_down_index = round( (1.00 * puzzle_field_size / img_height), 6)
        img_to_play = im.FactorScale(chosen_img, img_scale_down_index)
        img_width = int(img_width * img_scale_down_index)
        img_height = int(img_height * img_scale_down_index)

    else:
        img_to_play = chosen_img

    x_scale_index = round( (1.00 * (img_width/grid_width)/active_area_size), 6)
    y_scale_index = round( (1.00 * (img_height/grid_height)/active_area_size), 6)


    mainimage = im.Composite((int(img_width+(grip_size*2)*x_scale_index), int(img_height+(grip_size*2)*y_scale_index)),(int(grip_size*x_scale_index), int(grip_size*y_scale_index)), img_to_play)


    top_row = []
    for i in range (0, grid_width):
        top_row.append(i)

    bottom_row = []
    for i in range (0, grid_width):
        bottom_row.append(grid_width*(grid_height-1)+i)

    left_column = []
    for i in range (0, grid_height):
        left_column.append(grid_width*i)

    right_column = []
    for i in range (0, grid_height):
        right_column.append(grid_width*i + (grid_width-1) )


    jigsaw_grid = []
    for i in range(0,grid_height):
        for j in range (0,grid_width):
            jigsaw_grid.append([9,9,9,9])

    for i in range(0,grid_height):
        for j in range (0,grid_width):
            if grid_width*i+j not in top_row:
                if jigsaw_grid[grid_width*(i-1)+j][2] == 1:
                    jigsaw_grid[grid_width*i+j][0] = 2
                else:
                    jigsaw_grid[grid_width*i+j][0] = 1
            else:
                jigsaw_grid[grid_width*i+j][0] = 0
            if grid_width*i+j not in right_column:
                jigsaw_grid[grid_width*i+j][1] = renpy.random.randint(1,2)
            else:
                jigsaw_grid[grid_width*i+j][1] = 0
            if grid_width*i+j not in bottom_row:
                jigsaw_grid[grid_width*i+j][2] = renpy.random.randint(1,2)
            else:
                jigsaw_grid[grid_width*i+j][2] = 0
            if grid_width*i+j not in left_column:
                if jigsaw_grid[grid_width*i+j-1][1] == 1:
                    jigsaw_grid[grid_width*i+j][3] = 2
                else:
                    jigsaw_grid[grid_width*i+j][3] = 1
            else:
                jigsaw_grid[grid_width*i+j][3] = 0


        piecelist = dict()
        imagelist = dict()
        placedlist = dict()
        testlist = dict()

        for i in range(0,grid_width):
            for j in range (0,grid_height):
                piecelist[i,j] = [int(renpy.random.randint(0, (config.screen_width * 0.9 - puzzle_field_size))+puzzle_field_size), int(renpy.random.randint(0, (config.screen_height * 0.8)))]

                temp_img = im.Crop(mainimage, int(i*active_area_size*x_scale_index), int(j*active_area_size*y_scale_index), int(puzzle_piece_size*x_scale_index), int(puzzle_piece_size*y_scale_index))

        # makes puzzle piece image using its shape description and tile pieces
        # (will rotate them to form top, right, bottom and left sides of puzzle piece)
                imagelist[i,j] = im.Composite(
        (int(puzzle_piece_size*x_scale_index), int(puzzle_piece_size*y_scale_index)),
        (0,0), im.AlphaMask(temp_img, im.Scale(im.Rotozoom("_00%s.png"%(jigsaw_grid[grid_width*j+i][0]), 0, 1.0), int(puzzle_piece_size*x_scale_index), int(puzzle_piece_size*y_scale_index))),
        (0,0), im.AlphaMask(temp_img, im.Scale(im.Rotozoom("_00%s.png"%(jigsaw_grid[grid_width*j+i][1]), 270, 1.0), int(puzzle_piece_size*x_scale_index), int(puzzle_piece_size*y_scale_index))),
        (0,0), im.AlphaMask(temp_img, im.Scale(im.Rotozoom("_00%s.png"%(jigsaw_grid[grid_width*j+i][2]), 180, 1.0), int(puzzle_piece_size*x_scale_index), int(puzzle_piece_size*y_scale_index))),
        (0,0), im.AlphaMask(temp_img, im.Scale(im.Rotozoom("_00%s.png"%(jigsaw_grid[grid_width*j+i][3]), 90, 1.0), int(puzzle_piece_size*x_scale_index), int(puzzle_piece_size*y_scale_index)))
        )
                placedlist[i,j] = False

    #
    #####################################################################################################


jump puzzle

label win:
    scene black
    show expression img_to_play at Position(xalign=0.5,yalign=0.5) with dissolve

hero "Ура, теперь у меня есть ключ!"

scene maze2 with fade:
    zoom 0.6
show realhero at left with dissolve:
    zoom 0.2
show orakul at right with dissolve:
    zoom 0.47
orakul "Как же давно последний раз я тут видел кого-то, кроме птиц. Здравствуй!"
hero "Приветствую, ты тоже собираешься к Жальдару наведаться?"
orakul "Не совсем, я просто люблю здесь находиться, такая обстановка на свежем воздухе мне по душе. А ты, я смотрю, по делу к нему, за браслетом небось?"
hero "Да, а ты об этом откуда знаешь?"
orakul "Я знаю куда больше, чем нужно, и знаю, что будет тебя ждать после этой встречи, но прежде всего тебе нужно отворить эти ворота, а для этого нужно открыть вот этот сундучок."
orakul "И обрати внимание, что здесь могут быть вещи, которые помогут тебе в дальнейшем."
menu:
    "Открыть сундук":
        pass
scene chest_trial with fade:
    zoom 0.6
orakul "О, а я всё думал, где же она."
hero "Это твоя книга?"
orakul "Частично. Я лишь дополняю записи моих предшественников, дать почитать не могу, она не закончена. Однако теперь у тебя есть ключ, и ты можешь наконец встретиться с Жальдаром. Хочешь ли напоследок от меня загадку?"
hero "Почему бы и нет, давай."
label gods:
    scene trial2 with fade:
        zoom 0.6
    show dip_god at left:
        zoom 0.2
    show liar_god at center:
        zoom 0.2
    show truth_god at right:
        zoom 0.2
    orakul "Загадка об одном моём знаком оракуле. В отличие от остальных оракулов его устами вещало не одно божество, а целых три: бог Правды, бог Лжи и бог Дипломатии."
    orakul "Они изображались совершенно одинаковыми фигурами, расположенными за алтарем, перед которым люди, ищущие совета, преклоняли колени."
    orakul "Боги всегда охотно отвечали на вопросы. Но, так как они были похожи друг на друга, никто не мог определить, кто же из них отвечает."
    orakul "То ли бог Правды, которому надо верить, то ли бог Лжи, который всегда говорит неправду, то ли бог Дипломатии, который мог либо солгать, либо сказать правду."
    orakul "Это было на руку жрецам и способствовало славе оракула: боги всегда оказывались правы."
    orakul "Но однажды нашелся человек, казавшийся простаком, который задумал совершить то, что не удавалось сделать самым большим мудрецам. Он решил опознать каждого из богов."
    orakul "Человек вошел в храм и спросил бога, стоявшего слева:"
    orakul  "- Кто стоит рядом с тобой?"
    orakul "- Бог Правды, - был ответ."
    orakul "Тогда он спросил бога, стоявшего в центре:"
    orakul "- Кто ты?"
    orakul "- Бог Дипломатии, - был ответ."
    orakul "Последний вопрос он задал богу, стоящему справа:"
    orakul "- Кто стоит рядом с тобой?"
    orakul "- Бог Лжи, - был ответ."
    orakul "После этих вопросов человек узнал, где какой бог стоит. А сможешь ли ты мне сказать, какой бог стоит слева?"
hide dip_god
hide liar_god
hide truth_god
show realhero at left with dissolve:
    zoom 0.2
show orakul at right with dissolve:
    zoom 0.47
menu:
    "бог Правды":
        orakul "Неверно. Послушай ещё раз, а потом попробуй."
        jump gods
    "бог Лжи":
        orakul "Неверно. Послушай ещё раз, а потом попробуй."
        jump gods
    "бог Дипломатии":
        pass
if gender == "maleHero":
    orakul "Хм...И вправду, ты и с этим справился, ты действительно годишься для своей цели."
else:
    orakul "Хм...И вправду, ты и с этим справилась, ты действительно годишься для своей цели."
hero "Спасибо, но мне уже пора идти дальше, до встречи!"
orakul "Если она всё же случится, прощай..."

scene near_house with fade:
    zoom 0.6
show realhero at left with dissolve:
    zoom 0.2
"К часам прикреплена записка..."
"«Часы сломаны, какой-то хулиган выставил на них неправильное время»."
"«Я не собираюсь принимать гостей в запутанное для них время, поэтому прошу сверить время и исправить ошибку на часах»."
scene clock_start with fade:
    zoom 0.6
hero "{i}«Так, ну если судить по тем наручным часам, что я нашёл, то сейчас ровно...»{/i}"
$ clock = False
python:
    code = renpy.input("")
    code = code.strip().replace(" ", "").replace(".", ":")
    if code == '14:20' or code == '1420' or code == '2:20' or code == '220':
        clock = True
    else:
        pass
if clock:
    jump clockgood
hero "{i}«Стрелка часов вернулась на место. Видимо, это было неверное время».{/i}"
hero "{i}«Попробую ещё раз».{/i}"
python:
    code = renpy.input("")
    code = code.strip().replace(" ", "").replace(".", ":")
    if code == '14:20' or code == '1420' or code == '2:20' or code == '220':
        clock = True
if clock == False:
    jump clockbad
label clockgood:
    scene clock_win with fade:
        zoom 0.6
    "В часах показался ключ. Но в доме уже открылась дверь, и кто-то идет к часам."
    scene near_house with fade:
        zoom 0.6
    show realhero at left with dissolve:
        zoom 0.2
    show jildar at right with dissolve:
        zoom 0.2
    jildar "Приветсвую тебя, о твоём приходе я уже наслышан. Значит, тебе нужен последний браслет, что вручил мне Мальширус?"
    hero "Да, я пришёл именно за этим, волшебника звали Мальширус? Мне до тебя никто об этом не говорил."
    jildar "Ну, эта информация мало бы тебе помогла, да и после произошедшего у многих отпало желание называть его по имени."
    hero "А почему ты продолжаешь его так называть?"
    jildar "Потому что знаю, что он не хотел ничего плохого этому городку, он лишь хотел защитить его."
    hero "От кого?"
    jildar "От тёмного мага, чьи желания могли привести к гибели этого городка."
    jildar "Гроза в тот роковой день была лишь остатком от того, что направил на этот городок тёмный маг, этот защитный барьер смог защитить от более ужасного катаклизма."
    jildar "После этого Мальширус решил остановить этого мага, и утащить его в другое измерение, но тот оказывал серьёзное сопротивление, и в итоге они сейчас оба неизвестно где."
    jildar "Но одно мне известно точно, эти браслеты смогут открыть портал Мальширусу в его старой башне, что на болоте, и вызволить его."
    hero "Так почему бы тебе с гадалкой и Мифаной самим раньше этого не сделать? Почему эта честь выпала именно мне?"
    jildar "Дело всё в том, что процесс открытия требует магической силы, которой у нас нет, а вот в тебе, в избраннике пророчества, в твоей крови есть источник возобновляемой маны."
    hero "{b}ТЫ ХОЧЕШЬ СКАЗАТЬ, ЧТО Я МАГ?!{/b}"
    jildar "Тише, успокойся, ты ещё слишком неопытен для мага, но при помощи этих браслетов, думаю, ты сможешь открыть портал и освободить Мальшируса, а уж он точно всем нам поможет."
    hero "Вау, мне даже не верится, что это всё взаправду..."
    jildar "Думаю, для тебя это был очень тяжёлый день, ты можешь отдохнуть у меня в гостях, только не долго, надо нам до сумерек попасть на болото."
    jildar "А пока вот держи браслет и карту, что поможет миновать слишком опасные участки на болоте."
    menu:
        "Забрать браслет и карту":
            jump swamp
label clockbad:
    "В доме открылась дверь. Кто-то идет к часам."
    scene near_house with fade:
        zoom 0.6
    show realhero at left with dissolve:
        zoom 0.2
    show jildar at right with dissolve:
        zoom 0.2
    jildar "{b}КАК ТЫ CМОГ ПРОЙТИ ПРЕДЫДУЩИЕ ИСПЫТАНИЯ, ДОБРАТЬСЯ ДО МОЕГО ДОМА, НО ПРОСТО НЕ СМОГ ПОСТАВИТЬ НУЖНОЕ ВРЕМЯ?{/b}"
    hero "И что я теперь не смогу попасть домой?"
    jildar "Конечно, сможешь. Но теперь я буду называть тебя ослом."
    $ hero = Character ("Осёл", color= "#c8ffc8")
    jildar "Думаю, тебе нужен последний браслет, что вручил мне Мальширус?"
    hero "Да, я пришёл именно за этим, волшебника звали Мальширус? Мне до тебя никто об этом не говорил."
    jildar "Ну, эта информация мало бы тебе помогла, да и после произошедшего у многих отпало желание называть его по имени."
    hero "А почему ты продолжаешь его так называть?"
    jildar "Потому что знаю, что он не хотел ничего плохого этому городку, он лишь хотел защитить его."
    hero "От кого?"
    jildar "От тёмного мага, чьи желания могли привести к гибели этого городка."
    jildar "Гроза в тот роковой день была лишь остатком от того, что направил на этот городок тёмный маг, этот защитный барьер смог защитить от более ужасного катаклизма."
    jildar "После этого Мальширус решил остановить этого мага, и утащить его в другое измерение, но тот оказывал серьёзное сопротивление, и в итоге они сейчас оба неизвестно где."
    jildar "Но одно мне известно точно, эти браслеты смогут открыть портал Мальширусу в его старой башне, что на болоте, и вызволить его."
    hero "Так почему бы тебе с гадалкой и Мифаной самим раньше этого не сделать? Почему эта честь выпала именно мне?"
    jildar "Дело всё в том, что процесс открытия требует магической силы, которой у нас нет, а вот в тебе, в избраннике пророчества, в твоей крови есть источник возобновляемой маны."
    hero "{b}ТЫ ХОЧЕШЬ СКАЗАТЬ, ЧТО Я МАГ?!{/b}"
    jildar "Тише, успокойся, ты ещё слишком неопытен для мага, но при помощи этих браслетов, думаю, ты сможешь открыть портал и освободить Мальшируса, а уж он точно всем нам поможет."
    hero "Вау, мне даже не верится, что это всё взаправду..."
    jildar "Думаю, для тебя это был очень тяжёлый день, ты можешь отдохнуть у меня в гостях, только не долго, надо нам до сумерек попасть на болото."
    jildar "А пока вот держи браслет и карту, что поможет миновать слишком опасные участки на болоте."
    menu:
        "Забрать браслет и карту":
            jump swamp
label swamp:
    scene swamp_filler with fade:
        zoom 0.6
    show realhero at left with dissolve:
        zoom 0.2
    show jildar at right with dissolve:
        zoom 0.2
    jildar "Так, тут я вынужден тебя оставить, не потому что я так хочу, а потому что я совсем терпеть не могу камыши и болота."
    jildar "Всё, что тебе нужно - добраться вон до той башни, что посередине болота."
    jildar "Карта у тебя для этого есть, все браслеты при тебе. Мне остаётся пожелать тебе удачи и смиренно ждать твоего возвращения. Только это, обязательно вернись, возможно, ты последний шанс этого города."
    hero "Сделаю всё, что будет в моих силах, до скорой, надеюсь, встречи!"
    hide jildar with dissolve
    hero "{i}«Если я буду четко действовать указаниям на листке, всё должно получиться».{/i}"
jump swamp1
label swamp1dead:
    scene swamp_dead with fade:
        zoom 0.6
    show realhero at left with dissolve:
        zoom 0.2
    show help_list at right with dissolve:
        zoom 0.35
    menu:
        "Пойти налево":
            scene black with fade
            centered  "{color=#f00}Вы забрели туда, откуда нет выхода. Придётся оказаться в самом начале.{/color}"
            jump swamp1
        "Пойти направо":
            scene black with fade
            centered  "{color=#f00}Вы забрели туда, откуда нет выхода. Придётся оказаться в самом начале.{/color}"
            jump swamp1
        "Пойти прямо":
            scene black with fade
            centered  "{color=#f00}Вы забрели туда, откуда нет выхода. Придётся оказаться в самом начале.{/color}"
            jump swamp1
        "Вернуться назад":
            pass
label swamp1:
    scene swamp2 with fade:
        zoom 0.6
    show realhero at left with dissolve:
        zoom 0.2
    show help_list at center with dissolve:
        zoom 0.35
    menu:
        "Пойти налево":
            jump swamp1dead
        "Пойти направо":
            jump swamp1dead
        "Пойти прямо":
            jump swamp2
label swamp2dead:
    scene swamp_dead with fade:
        zoom 0.6
    show realhero at left with dissolve:
        zoom 0.2
    show help_list at right with dissolve:
        zoom 0.35
    menu:
        "Пойти налево":
            scene black with fade
            centered  "{color=#f00}Вы забрели туда, откуда нет выхода. Придётся оказаться в самом начале.{/color}"
            jump swamp1
        "Пойти направо":
            scene black with fade
            centered  "{color=#f00}Вы забрели туда, откуда нет выхода. Придётся оказаться в самом начале.{/color}"
            jump swamp1
        "Пойти прямо":
            scene black with fade
            centered  "{color=#f00}Вы забрели туда, откуда нет выхода. Придётся оказаться в самом начале.{/color}"
            jump swamp1
        "Вернуться назад":
            pass
label swamp2:
    scene swamp4 with fade:
        zoom 0.6
    show realhero at left with dissolve:
        zoom 0.2
    show help_list at center with dissolve:
        zoom 0.35
    menu:
        "Пойти налево":
            jump swamp2dead
        "Пойти направо":
            jump swamp2dead
        "Пойти прямо":
            jump swamp3
        "Вернуться назад":
            jump swamp1
label swamp3dead:
    scene swamp_dead with fade:
        zoom 0.6
    show realhero at left with dissolve:
        zoom 0.2
    show help_list at right with dissolve:
        zoom 0.35
    menu:
        "Пойти налево":
            scene black with fade
            centered  "{color=#f00}Вы забрели туда, откуда нет выхода. Придётся оказаться в самом начале.{/color}"
            jump swamp1
        "Пойти направо":
            scene black with fade
            centered  "{color=#f00}Вы забрели туда, откуда нет выхода. Придётся оказаться в самом начале.{/color}"
            jump swamp1
        "Пойти прямо":
            scene black with fade
            centered  "{color=#f00}Вы забрели туда, откуда нет выхода. Придётся оказаться в самом начале.{/color}"
            jump swamp1
        "Вернуться назад":
            pass
label swamp3:
    scene swamp1 with fade:
        zoom 0.6
    show realhero at left with dissolve:
        zoom 0.2
    show help_list at center with dissolve:
        zoom 0.35
    menu:
        "Пойти налево":
            jump swamp4
        "Пойти направо":
            jump swamp3dead
        "Пойти прямо":
            jump swamp3dead
        "Вернуться назад":
            jump swamp2
label swamp4dead:
    scene swamp_dead with fade:
        zoom 0.6
    show realhero at left with dissolve:
        zoom 0.2
    show help_list at right with dissolve:
        zoom 0.35
    menu:
        "Пойти налево":
            scene black with fade
            centered  "{color=#f00}Вы забрели туда, откуда нет выхода. Придётся оказаться в самом начале.{/color}"
            jump swamp1
        "Пойти направо":
            scene black with fade
            centered  "{color=#f00}Вы забрели туда, откуда нет выхода. Придётся оказаться в самом начале.{/color}"
            jump swamp1
        "Пойти прямо":
            scene black with fade
            centered  "{color=#f00}Вы забрели туда, откуда нет выхода. Придётся оказаться в самом начале.{/color}"
            jump swamp1
        "Вернуться назад":
            pass
label swamp4:
    scene swamp_filler with fade:
        zoom 0.6
    show realhero at left with dissolve:
        zoom 0.2
    show help_list at center with dissolve:
        zoom 0.35
    menu:
        "Пойти налево":
            jump swamp5
        "Пойти направо":
            jump swamp4dead
        "Пойти прямо":
            jump swamp4dead
        "Вернуться назад":
            jump swamp3
label swamp5dead:
    scene swamp_dead with fade:
        zoom 0.6
    show realhero at left with dissolve:
        zoom 0.2
    show help_list at right with dissolve:
        zoom 0.35
    menu:
        "Пойти налево":
            scene black with fade
            centered  "{color=#f00}Вы забрели туда, откуда нет выхода. Придётся оказаться в самом начале.{/color}"
            jump swamp1
        "Пойти направо":
            scene black with fade
            centered  "{color=#f00}Вы забрели туда, откуда нет выхода. Придётся оказаться в самом начале.{/color}"
            jump swamp1
        "Пойти прямо":
            scene black with fade
            centered  "{color=#f00}Вы забрели туда, откуда нет выхода. Придётся оказаться в самом начале.{/color}"
            jump swamp1
        "Вернуться назад":
            pass
label swamp5:
    scene swamp5 with fade:
        zoom 0.6
    show realhero at left with dissolve:
        zoom 0.2
    show help_list at center with dissolve:
        zoom 0.35
    menu:
        "Пойти налево":
            jump swamp6
        "Пойти направо":
            jump swamp5dead
        "Пойти прямо":
            jump swamp5dead
        "Вернуться назад":
            jump swamp4
label swamp6dead:
    scene swamp_dead with fade:
        zoom 0.6
    show realhero at left with dissolve:
        zoom 0.2
    show help_list at right with dissolve:
        zoom 0.35
    menu:
        "Пойти налево":
            scene black with fade
            centered  "{color=#f00}Вы забрели туда, откуда нет выхода. Придётся оказаться в самом начале.{/color}"
            jump swamp1
        "Пойти направо":
            scene black with fade
            centered  "{color=#f00}Вы забрели туда, откуда нет выхода. Придётся оказаться в самом начале.{/color}"
            jump swamp1
        "Пойти прямо":
            scene black with fade
            centered  "{color=#f00}Вы забрели туда, откуда нет выхода. Придётся оказаться в самом начале.{/color}"
            jump swamp1
        "Вернуться назад":
            pass
label swamp6:
    scene swamp5 with fade:
        zoom 0.6
    show realhero at left with dissolve:
        zoom 0.2
    show help_list at center with dissolve:
        zoom 0.35
    menu:
        "Пойти налево":
            jump swamp6dead
        "Пойти направо":
            jump swamp6dead
        "Пойти прямо":
            jump swamp7
        "Вернуться назад":
            jump swamp5
label swamp7dead:
    scene swamp_dead with fade:
        zoom 0.6
    show realhero at left with dissolve:
        zoom 0.2
    show help_list at right with dissolve:
        zoom 0.35
    menu:
        "Пойти налево":
            scene black with fade
            centered  "{color=#f00}Вы забрели туда, откуда нет выхода. Придётся оказаться в самом начале.{/color}"
            jump swamp1
        "Пойти направо":
            scene black with fade
            centered  "{color=#f00}Вы забрели туда, откуда нет выхода. Придётся оказаться в самом начале.{/color}"
            jump swamp1
        "Пойти прямо":
            scene black with fade
            centered  "{color=#f00}Вы забрели туда, откуда нет выхода. Придётся оказаться в самом начале.{/color}"
            jump swamp1
        "Вернуться назад":
            pass
label swamp7:
    scene swamp4 with fade:
        zoom 0.6
    show realhero at left with dissolve:
        zoom 0.2
    show help_list at center with dissolve:
        zoom 0.35
    menu:
        "Пойти налево":
            jump swamp7dead
        "Пойти направо":
            jump swamp7dead
        "Пойти прямо":
            jump swamp8
        "Вернуться назад":
            jump swamp6
label swamp8dead:
    scene swamp_dead with fade:
        zoom 0.6
    show realhero at left with dissolve:
        zoom 0.2
    show help_list at right with dissolve:
        zoom 0.35
    menu:
        "Пойти налево":
            scene black with fade
            centered  "{color=#f00}Вы забрели туда, откуда нет выхода. Придётся оказаться в самом начале.{/color}"
            jump swamp1
        "Пойти направо":
            scene black with fade
            centered  "{color=#f00}Вы забрели туда, откуда нет выхода. Придётся оказаться в самом начале.{/color}"
            jump swamp1
        "Пойти прямо":
            scene black with fade
            centered  "{color=#f00}Вы забрели туда, откуда нет выхода. Придётся оказаться в самом начале.{/color}"
            jump swamp1
        "Вернуться назад":
            pass
label swamp8:
    scene swamp3 with fade:
        zoom 0.6
    show realhero at left with dissolve:
        zoom 0.2
    show help_list at center with dissolve:
        zoom 0.35
    menu:
        "Пойти налево":
            jump swamp8dead
        "Пойти направо":
            jump swamp9
        "Пойти прямо":
            jump swamp8dead
        "Вернуться назад":
            jump swamp7
label swamp9dead:
    scene swamp_dead with fade:
        zoom 0.6
    show realhero at left with dissolve:
        zoom 0.2
    show help_list at right with dissolve:
        zoom 0.35
    menu:
        "Пойти налево":
            scene black with fade
            centered  "{color=#f00}Вы забрели туда, откуда нет выхода. Придётся оказаться в самом начале.{/color}"
            jump swamp1
        "Пойти направо":
            scene black with fade
            centered  "{color=#f00}Вы забрели туда, откуда нет выхода. Придётся оказаться в самом начале.{/color}"
            jump swamp1
        "Пойти прямо":
            scene black with fade
            centered  "{color=#f00}Вы забрели туда, откуда нет выхода. Придётся оказаться в самом начале.{/color}"
            jump swamp1
        "Вернуться назад":
            pass
label swamp9:
    scene swamp2 with fade:
        zoom 0.6
    show realhero at left with dissolve:
        zoom 0.2
    show help_list at center with dissolve:
        zoom 0.35
    menu:
        "Пойти налево":
            jump swamp9dead
        "Пойти направо":
            jump swamp10
        "Пойти прямо":
            jump swamp9dead
        "Вернуться назад":
            jump swamp8
label swamp10dead:
    scene swamp_dead with fade:
        zoom 0.6
    show realhero at left with dissolve:
        zoom 0.2
    show help_list at right with dissolve:
        zoom 0.35
    menu:
        "Пойти налево":
            scene black with fade
            centered  "{color=#f00}Вы забрели туда, откуда нет выхода. Придётся оказаться в самом начале.{/color}"
            jump swamp1
        "Пойти направо":
            scene black with fade
            centered  "{color=#f00}Вы забрели туда, откуда нет выхода. Придётся оказаться в самом начале.{/color}"
            jump swamp1
        "Пойти прямо":
            scene black with fade
            centered  "{color=#f00}Вы забрели туда, откуда нет выхода. Придётся оказаться в самом начале.{/color}"
            jump swamp1
        "Вернуться назад":
            pass
label swamp10:
    scene swamp4 with fade:
        zoom 0.6
    show realhero at left with dissolve:
        zoom 0.2
    show help_list at center with dissolve:
        zoom 0.35
    menu:
        "Пойти налево":
            jump swamp11
        "Пойти направо":
            jump swamp10dead
        "Пойти прямо":
            jump swamp10dead
        "Вернуться назад":
            jump swamp9
label swamp11dead:
    scene swamp_dead with fade:
        zoom 0.6
    show realhero at left with dissolve:
        zoom 0.2
    show help_list at right with dissolve:
        zoom 0.35
    menu:
        "Пойти налево":
            scene black with fade
            centered  "{color=#f00}Вы забрели туда, откуда нет выхода. Придётся оказаться в самом начале.{/color}"
            jump swamp1
        "Пойти направо":
            scene black with fade
            centered  "{color=#f00}Вы забрели туда, откуда нет выхода. Придётся оказаться в самом начале.{/color}"
            jump swamp1
        "Пойти прямо":
            scene black with fade
            centered  "{color=#f00}Вы забрели туда, откуда нет выхода. Придётся оказаться в самом начале.{/color}"
            jump swamp1
        "Вернуться назад":
            pass
label swamp11:
    scene swamp1 with fade:
        zoom 0.6
    show realhero at left with dissolve:
        zoom 0.2
    show help_list at center with dissolve:
        zoom 0.35
    menu:
        "Пойти налево":
            pass
        "Пойти направо":
            jump swamp10dead
        "Пойти прямо":
            jump swamp10dead
        "Вернуться назад":
            jump swamp9
scene magic_tower with fade:
    zoom 0.6
show realhero at left with dissolve:
    zoom 0.2
"Вы открываете старую тяжелую скрипучую дверь. Наверх ведёт винтовая лестница."
scene without_mage with fade:
    zoom 0.6
show realhero at left with dissolve:
    zoom 0.2
"Впереди находится очень странное зеркало."
scene with_mage with fade:
    zoom 0.6
show realhero at left with dissolve:
    zoom 0.2
mage "Я уже и не надеялся, что кто-то придёт. Смотрю тебе удалось собрать почти все нужные браслеты. Что же, сейчас я добавлю одну небольшую деталь, и можем начинать."
"Из зеркала вылетел ещё один браслет. Когда же они собрались вместе, то улетели в зеркало."
mage "Теперь мне понадобится твоя помощь, я буду отсюда устанавливать связь с браслетами, отчего они должны начать сверкать."
mage "Всё, что тебе нужно - это устанавливать с ними связь в том же порядке, что и я. Тогда я смогу использовать их силу и перейти через портал. Ты как, готов?"
hero "Что, подожди... А как мне установить с ними связь, докоснуться или что?"
mage "Нет, тут ты должен задействовать своё сознание, ты должен почувствовать, что браслеты это не безделушки, а что-то, что поддаётся воздействию или само воздействует."
mage "Для первого раза попробуй сосредоточиться, глядя на него, а я начинаю."
# Саймон говорит
label badsimon:
    mage "Нет, нет, нет, связь с браслетами слишком нестабильна, я не могу отсюда их контролировать..."
    scene bad_end_1 with Fade(2, 0.0, 4):
        zoom 0.6
    scene bad_end_2 with vpunch:
        zoom 0.6
    scene black with Fade(4, 0.0, 2)
    centered "{color=#f00}Произошёл невиданной силы взрыв, который смёл всё живое, что находилось под магическим барьером.{/color}"
    centered "{color=#f00}Пройдёт время, магия покинет это место, заслон падёт, но только вот никто из странников никогда не узнает, почему этот город разрушился.{/color}"
    centered "{color=#f00}Никто не узнает о путнике, которому выпала честь быть избранным спасти город и который так и не смог оправдать надежд местных жителей.{/color}"
    # return
label goodsimon:
    scene without_mage with fade:
        zoom 0.6
    show realhero at left with dissolve:
        zoom 0.2
    show witcher at right with dissolve:
        zoom 0.2
    mage "Фух, наконец-то, свобода."
    hero "Это что, получается, барьер больше не окружает этот город?"
    mage "Да, его больше нет, вот и конец твоего небольшого приключения. Однако, этот конец станет новым началом другой истории."
    mage "Я хочу сказать, что могу телепортировать тебя к бару, откуда ты сможешь пойти домой. Или же я предлагаю тебе стать моим учеником."
    mage "В тебе есть магические силы, сейчас их немного, но при правильных тренировках из тебя может выйти неплохой маг. Ну, что скажешь?"
    menu:
        "Согласиться":
            hero "Знаешь, мне и вправду очень интересна магия, так что я был бы не против стать твоим учеником."
            scene magic_end_1 with Fade(2, 0.0, 2):
                zoom 0.6
            scene magic_end_2 with Fade(2, 0.0, 2):
                zoom 0.6
            "Вы стали учеником мага и принялись постигать самые потаённые глубины магии, в то время как город зажил своей прежней жизнью."
            "Он вновь стал зрим для путников, и жители наконец-то перестали ощущать себя заточёнными в этом новом и одновременно старом мире."
        "Отказаться":
            hero "Я всё же хочу обратно, домой, устал я от этого приключения."
            scene magic_end_1 with Fade(2, 0.0, 2):
                zoom 0.6
            scene ordinary_end with Fade(2, 0.0, 2):
                zoom 0.6
            "Над городом больше нет барьера."
            "В город вновь стали прибывать путники, и если они заходили в бар, то первым, что они слышали - это история, рассказывающая о приключении одного Героя, который смог снять магический барьер с города."
            "Жизнь здесь стала прежней. А вы отправляетесь домой."
return
