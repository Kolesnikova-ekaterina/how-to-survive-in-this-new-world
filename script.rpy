# Вы можете расположить сценарий своей игры в этом файле.

#
# Определение персонажей игры.
define hero = Character ("[povname]", color= "#c8ffc8")
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.
init:
    image malehero="images/maleHero.png"
    image femalehero = "images/femaleHero.png"

# Игра начинается здесь:
label start:

scene square:
        zoom 0.35

show malehero at right:
        zoom 0.25
show femalehero at left:
        zoom 0.25

python:
    povname = renpy.input("Как тебя зовут?")
    povname = povname.strip()

    if not povname:
         povname = "Джo Доу"

hero "Меня зовут [povname]!"
$ gender = "maleHero"
menu:
    "За кого вы хотите играть?"
    "Парень":
        pass
    "Девушка":
        $ gender = "femaleHero"
        pass
hide malehero
hide femalehero
image realhero = "images/[gender].png"
show realhero at left:
    zoom 0.25
hero "Что это за место?"
return
