from apps.first_menu.models import SubMenu


def fill_default_menu():
    main_menu = SubMenu.objects.bulk_create([
        SubMenu(name='Грызуны', url='Грызуны'),
        SubMenu(name='Приматы', url='Приматы'),
        SubMenu(name='Хищные', url='Хищные'),
        SubMenu(name='Хоботные', url='Хоботные'),
    ])
    sub_menu1 = SubMenu.objects.bulk_create([
        SubMenu(name='Свинковые', url='Грызуны/Свинковые', parent=SubMenu.objects.get(name='Грызуны')),
        SubMenu(name='Дикобразы', url='Грызуны/Дикобразы', parent=SubMenu.objects.get(name='Грызуны')),
        SubMenu(name='Мышиные', url='Грызуны/Мышиные', parent=SubMenu.objects.get(name='Грызуны')),
        SubMenu(name='Тушканчики', url='Грызуны/Тушканчики', parent=SubMenu.objects.get(name='Грызуны')),
        SubMenu(name='Беличьи', url='Грызуны/Беличьи', parent=SubMenu.objects.get(name='Грызуны')),
        SubMenu(name='Лемурообразные', url='Приматы/Лемурообразные', parent=SubMenu.objects.get(name='Приматы')),
        SubMenu(name='Лориобразные', url='Приматы/Лориобразные', parent=SubMenu.objects.get(name='Приматы')),
        SubMenu(name='Обезьянообразные', url='Приматы/Обезьянообразные', parent=SubMenu.objects.get(name='Приматы')),
        SubMenu(name='Псовые', url='Хищные/Псовые', parent=SubMenu.objects.get(name='Хищные')),
        SubMenu(name='Кошачьи', url='Хищные/Кошачьи', parent=SubMenu.objects.get(name='Хищные')),
        SubMenu(
            name='Африканский слон',
            url='Хоботные/Африканский_слон',
            parent=SubMenu.objects.get(name='Хоботные'),
            about='На слонов могут стаями нападать сухопутные пиявки.'
        ),
        SubMenu(
            name='Азиатский слон',
            url='Хоботные/Азиатский_слон',
            parent=SubMenu.objects.get(name='Хоботные'),
            about='Слоны летом поднимаются в Гималаи, встречаясь у границы вечных снегов, на высоте до 3600 м.'
        ),
    ])

    sub_menu2 = SubMenu.objects.bulk_create([
        SubMenu(name='Свинки', url='Грызуны/Свинковые/Свинки', parent=SubMenu.objects.get(name='Свинковые')),
        SubMenu(name='Водосвинки', url='Грызуны/Свинковые/Водосвинки', parent=SubMenu.objects.get(name='Свинковые')),
        SubMenu(
            name='Кистехвостые дикобразы',
            url='Грызуны/Дикобразы/Кистехвостые_дикобразы',
            parent=SubMenu.objects.get(name='Дикобразы')
        ),
        SubMenu(
            name='Длиннохвостый дикобраз',
            parent=SubMenu.objects.get(name='Дикобразы'),
            about='Длиннохвостый дикобраз не может ощетиниваться и трещать своими иглами.'
        ),
        SubMenu(name='Песчанковые', url='Грызуны/Мышиные/Песчанковые', parent=SubMenu.objects.get(name='Мышиные')),
        SubMenu(
            name='Большой тушканчик',
            url='Грызуны/Тушканчики/Большой_тушканчик',
            parent=SubMenu.objects.get(name='Тушканчики'),
            about='Большой тушканчик — самый крупный среди тушканчиков.'
        ),
        SubMenu(
            name='Тарбаганчик',
            url='Грызуны/Тушканчики/Тарбаганчик',
            parent=SubMenu.objects.get(name='Тушканчики'),
            about='Тарбаганчик считается сельскохозяйственным вредителем.'
        ),
        SubMenu(name='Летяги', url='Грызуны/Беличьи/Летяги', parent=SubMenu.objects.get(name='Беличьи')),
        SubMenu(name='Суслики', url='Грызуны/Беличьи/Суслики', parent=SubMenu.objects.get(name='Беличьи')),
        SubMenu(
            name='Карликовый мышиный лемур',
            url='Приматы/Лемурообразные/Карликовый_мышиный_лемур',
            parent=SubMenu.objects.get(name='Лемурообразные'),
            about='Один из самых маленьких приматов (вес 50 граммов, длина 20 см).'
        ),
        SubMenu(
            name='Лемуровые',
            url='Приматы/Лемурообразные/Лемуровые',
            parent=SubMenu.objects.get(name='Лемурообразные')
        ),
        SubMenu(
            name='Галаго Аллена',
            url='Приматы/Лориобразные/Галаго_Аллена',
            parent=SubMenu.objects.get(name='Лориобразные'),
            about='Название вида дано в честь английского контр-адмирала Уильяма Аллена.'
        ),
        SubMenu(
            name='Широконосые обезьяны',
            url='Приматы/Обезьянообразные/Широконосые_обезьяны',
            parent=SubMenu.objects.get(name='Обезьянообразные')
        ),
        SubMenu(
            name='Узконосые обезьяны',
            url='Приматы/Обезьянообразные/Узконосые_обезьяны',
            parent=SubMenu.objects.get(name='Обезьянообразные')
        ),
        SubMenu(
            name='Померанский_шпиц',
            url='Хищные/Псовые/Померанский_шпиц',
            parent=SubMenu.objects.get(name='Псовые'),
            about='Шпиц любит движение, прогулку и игру.'
        ),
        SubMenu(
            name='Британская короткошерстная кошка',
            url='Хищные/Кошачьи/Британская_короткошерстная_кошка',
            parent=SubMenu.objects.get(name='Кошачьи'),
            about='Шерсть у британской кошки очень пушистая и мягкая, но довольно короткая.'
        ),
    ])

    sub_menu3 = SubMenu.objects.bulk_create([
        SubMenu(
            name='Бразильская свинка',
            url='Грызуны/Свинковые/Свинки/Бразильская_свинка',
            parent=SubMenu.objects.get(name='Свинки'),
            about='Бразильские свинки распространены почти по всей Южной Америке.'
        ),
        SubMenu(
            name='Морская свинка',
            url='Грызуны/Свинковые/Свинки/Морская_свинка',
            parent=SubMenu.objects.get(name='Свинки'),
            about='Могут чирикать от 2 до 15 минут, обычно в тёмное время суток.'
        ),
        SubMenu(
            name='Капибара',
            url='Грызуны/Свинковые/Водосвинки/Капибара',
            parent=SubMenu.objects.get(name='Водосвинки'),
            about='Капибара — самый крупный среди современных грызунов.'
        ),
        SubMenu(
            name='Африканский дикобраз',
            url='Грызуны/Дикобразы/Кистехвостые_дикобразы/Африканский_дикобраз',
            parent=SubMenu.objects.get(name='Кистехвостые дикобразы'),
            about='Иглы легче и короче чем у большинства других видов.'
        ),
        SubMenu(
            name='Большехвостый дикобраз',
            url='Грызуны/Дикобразы/Кистехвостые_дикобразы/Большехвостый_дикобраз',
            parent=SubMenu.objects.get(name='Кистехвостые дикобразы'),
            about='Ночной вид, иногда живущий группами.'
        ),
        SubMenu(
            name='Песчанка Чизмана',
            url='Грызуны/Мышиные/Песчанковые/Песчанка_Чизмана',
            parent=SubMenu.objects.get(name='Песчанковые'),
            about='Она притаскивает в нору сочные растения, тем самым повышая уровень влажности внутри.'
        ),
        SubMenu(
            name='Южная летяга',
            url='Грызуны/Беличьи/Летяги/Южная_летяга',
            parent=SubMenu.objects.get(name='Летяги'),
            about='Этот вид очень общительный, особенно в зимнее время, когда образуются коммунальные гнёзда.'
        ),
        SubMenu(
            name='Сложнозубая летяга',
            url='Грызуны/Беличьи/Летяги/Сложнозубая_летяга',
            parent=SubMenu.objects.get(name='Летяги'),
            about='Названа из-за своих зубов, которые отличаются от зубов других видов белок-летяг.'
        ),
        SubMenu(
            name='Реликтовый суслик',
            url='Грызуны/Беличьи/Суслики/Реликтовый_суслик',
            parent=SubMenu.objects.get(name='Суслики'),
            about='Распространение ограничено разобщёнными участками на горных склонах Тянь-Шаня и Памира.'
        ),
        SubMenu(
            name='Кошачий лемур',
            url='Приматы/Лемурообразные/Лемуровые/Кошачий_лемур',
            parent=SubMenu.objects.get(name='Лемуровые'),
            about='На хвосте 13 чёрных и белых полос.'
        ),
        SubMenu(
            name='Карликовая игрунка',
            url='Приматы/Обезьянообразные/Широконосые_обезьяны/Карликовая_игрунка',
            parent=SubMenu.objects.get(name='Широконосые обезьяны'),
            about='Является одним из самых маленьких приматов.'
        ),
        SubMenu(
            name='Человек разумный',
            url='Приматы/Обезьянообразные/Узконосые_обезьяны/Человек_разумный',
            parent=SubMenu.objects.get(name='Узконосые обезьяны'),
            about='Люди — крайне социальные животные.'
        ),
    ])
