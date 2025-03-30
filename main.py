import operator
from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery
import config as cfg
import keyboards as kb  # предполагаем, что вы создадите кнопки в файле buttons.py


app = Client(
    "gs_super_bot",
    api_id=cfg.API_ID,
    api_hash=cfg.API_HASH,
    bot_token=cfg.BOT_TOKEN
)

@app.on_message(filters.command("start") | filters.regex('Назад🔙'))
async def start_command(client: Client, message: Message):
    await message.reply(
        "Здравствуй, я бот который поможет тебе выбрать какой-то фильм или сериал для просмотра. Просто выбери что ты хочешь посмотреть, и выбери какой-то фильм из списка))\n",
        reply_markup=kb.main_keyboard
    )

@app.on_message(filters.command("films") | filters.regex('Фильмы✨'))
async def start_command(client: Client, message: Message):
    await message.reply(
        "Ты выбрал фильмы, круто!! Теперь выбери какие ты будешь смотреть фильмы, иностранные или русские, удачи при выборе:)\n",
        reply_markup=kb.chooseuridklol_keyboard
    )

@app.on_message(filters.command("seriall") | filters.regex('Сериалы📺'))
async def start_command(client: Client, message: Message):
    await message.reply(
        "Ты выбрал поссмотреть сериалы, теперь тебе надо выбрать какой будешь смотреть, удачи при выборе:)\n",
        reply_markup=kb.trumpkamalabillieszakendrick_keyboard
    )

@app.on_message(filters.command("russeriall") | filters.regex('Русские сериалы🪆'))
async def start_command(client: Client, message: Message):
    await message.reply( """
Русские сериалы:

1. Кухня (2012-2016)
Шеф-повар с адским характером, бармен-бабник, наивный поварёнок – и всё это в ресторане. Офигенный юмор и персонажи.

2. Отель Элеон (2016-2017)
Спин-офф «Кухни», но уже с акцентом на отельный бизнес. Персонажи всё такие же яркие, юмор отличный.

3. Гранд (2018-2020)
Ещё один сериал во вселенной «Кухни» и «Отеля Элеон». Героиня пытается пробиться в управлении отелем.

4. Интерны (2010-2016)
Комедия про медиков: циничный врач Быков и стажёры, которые постоянно попадают в идиотские ситуации.

5. Мажор (2014-2018)
Мажора из богатой семьи засылают работать в полицию. Вначале он тупо развлекается, но потом начинает реально расследовать дела.

6. Звоните ДиКаприо! (2018)
Актёр, ведущий разгульную жизнь, узнаёт, что болен ВИЧ. Глубокий, но очень годный сериал.

7. Метод (2015-2020)
Мрачный детектив про маньяков и следователя с нестандартными методами.
""",
reply_markup=kb.websiterusserial_keyboard
            )

@app.on_message(filters.command("ammmseriall") | filters.regex('Иностранные сериалы✨'))
async def start_command(client: Client, message: Message):
    await message.reply(
        """
Лучшие зарубежные сериалы:

1. Как избежать наказания за убийство (How to Get Away with Murder, 2014–2020)
Сюжет крутится вокруг крутейшего адвоката и её студентов, которые случайно впутываются в убийство. Загадки, интриги, расследования.

2. Новичок (The Rookie, 2018–)
Джон Нолан – самый старый новичок в полиции Лос-Анджелеса. Экшен, юмор, интересные преступления – очень бодро.

3. Во все тяжкие (Breaking Bad, 2008–2013)
Школьный учитель химии превращается в наркобарона. Гениальный сюжет, куча напряжённых моментов.

4. Шерлок (Sherlock, 2010–2017)
Современный Шерлок Холмс в Лондоне. Бенедикт Камбербэтч на высоте, мозг закипает от его дедукции.

5. Сотня (The 100, 2014–2020)
После ядерной войны люди живут в космосе, но отправляют 100 подростков проверить, можно ли вернуться на Землю. Жёсткое выживание и куча заговоров.

6. Миллиарды (Billions, 2016–)
Про мир больших денег, грязных игр, юристов и крутых бизнесменов. Интеллектуальная война миллиардера и прокурора.

7. Хороший доктор (The Good Doctor, 2017–)
Про молодого врача с аутизмом, который пытается доказать, что он гений хирургии. Трогательная, но крутая история.
""",
        reply_markup=kb.websiteammserial_keyboard
    )

@app.on_message(filters.command("amserweb") | filters.regex('Сайты🌸'))
async def start_command(client: Client, message: Message):
    await message.reply(
        """
🎬 <b>Лучшие зарубежные сериалы</b> 🎬

1. <b>Как избежать наказания за убийство</b> (How to Get Away with Murder, 2014–2020)
Сюжет крутится вокруг крутейшего адвоката и её студентов.
🔹 <a href="https://www.netflix.com/title/80024057">Netflix</a> | <a href="https://www.kinopoisk.ru/series/1048334/">Кинопоиск</a>

2. <b>Новичок</b> (The Rookie, 2018–)
Джон Нолан – самый старый новичок в полиции Лос-Анджелеса.
🔹 <a href="https://www.kinopoisk.ru/series/1048334/">Кинопоиск</a> | <a href="https://www.hulu.com/series/the-rookie">Hulu</a>

3. <b>Во все тяжкие</b> (Breaking Bad, 2008–2013)
Школьный учитель химии превращается в наркобарона.
🔹 <a href="https://www.netflix.com/title/70143836">Netflix</a> | <a href="https://www.kinopoisk.ru/series/404900/">Кинопоиск</a>

4. <b>Шерлок</b> (Sherlock, 2010–2017)
Современный Шерлок Холмс в Лондоне.
🔹 <a href="https://www.bbc.co.uk/programmes/b018ttws">BBC</a> | <a href="https://www.kinopoisk.ru/series/404900/">Кинопоиск</a>

5. <b>Сотня</b> (The 100, 2014–2020)
100 подростков проверяют, можно ли вернуться на Землю после ядерной войны.
🔹 <a href="https://www.netflix.com/title/70283264">Netflix</a> | <a href="https://www.kinopoisk.ru/series/775276/">Кинопоиск</a>

6. <b>Миллиарды</b> (Billions, 2016–)
Интеллектуальная война миллиардера и прокурора.
🔹 <a href="https://www.showtime.com/billions">Showtime</a> | <a href="https://www.kinopoisk.ru/series/1048334/">Кинопоиск</a>

7. <b>Хороший доктор</b> (The Good Doctor, 2017–)
Врач с аутизмом доказывает, что он гений хирургии.
🔹 <a href="https://www.hulu.com/series/the-good-doctor">Hulu</a> | <a href="https://www.kinopoisk.ru/series/1048334/">Кинопоиск</a>
""",
        reply_markup=kb.undo_keyboard
    )


@app.on_message(filters.command("webruss") | filters.regex('Сайты🪆'))
async def start_command(client: Client, message: Message):
    await message.reply(
        """
📺 Популярные русские сериалы с ссылками:

1. <b>Кухня</b> (2012-2016)
Ресторанная комедия
Смотреть: [START](https://start.ru/watch/kuhnya) | [Кинопоиск](https://www.kinopoisk.ru/series/716587/)

2. <b>Отель Элеон</b> (2016-2017)
Спин-офф "Кухни"
Смотреть: [START](https://start.ru/watch/oteleljon) | [IVI](https://www.ivi.ru/watch/217766)

3. <b>Гранд</b> (2018-2020)
Отельный бизнес
Смотреть: [START](https://start.ru/watch/grand) | [Кинопоиск](https://www.kinopoisk.ru/series/1044036/)

4. <b>Интерны</b> (2010-2016)
Медицинская комедия
Смотреть: [START](https://start.ru/watch/interny) | [IVI](https://www.ivi.ru/watch/internyi)

5. <b>Мажор</b> (2014-2018)
Полицейская драма
Смотреть: [Кинопоиск](https://www.kinopoisk.ru/series/77044/) | [START](https://start.ru/watch/major)

6. <b>Звоните ДиКаприо!</b> (2018)
Драма
Смотреть: [Кинопоиск](https://www.kinopoisk.ru/series/1048334/) | [IVI](https://www.ivi.ru/watch/146003)

7. <b>Метод</b> (2015-2020)
Детектив
Смотреть: [Кинопоиск](https://www.kinopoisk.ru/series/963623/) | [START](https://start.ru/watch/metod)
""",
        reply_markup=kb.undo_keyboard
    )



@app.on_message(filters.command("rusfilm") | filters.regex('Русские фильмы📺'))
async def start_command(client: Client, message: Message):
    await message.reply(
        """
🎬 Русские фильмы 🎬

1. <b>Холоп</b> (2019)
Мажора отправляют в "прошлое", где он должен стать обычным крестьянином. Куча ржачных моментов, но при этом глубокий смысл.

2. <b>Лёд</b> (2018)
История фигуристки, которая после травмы пытается вернуться к мечте. Драма, романтика, но без розовых соплей.

3. <b>Притяжение</b> (2017)
Инопланетяне падают на Москву. Наши военные, учёные и простые люди решают, что с ними делать.

4. <b>Движение вверх</b> (2017)
Фильм про легендарную победу советских баскетболистов над США в 1972 году. Очень мощно снято.

5. <b>Батя</b> (2021)
Комедия-драма про отца, который воспитывал сына жёсткими методами. Очень жизненно.
""",
        reply_markup=kb.webrusfilm_keyboard
    )

@app.on_message(filters.command("webrusfilm") | filters.regex('Сайты🎆'))
async def start_command(client: Client, message: Message):
    await message.reply(
        """
🎬 <b>Лучшие русские фильмы</b> 🎬

1. <b>Холоп</b> (2019)
Мажора отправляют в "прошлое", где он должен стать обычным крестьянином.
🔹 <a href="https://www.kinopoisk.ru/film/1143242/">Кинопоиск</a> | <a href="https://start.ru/watch/holop">START</a> | <a href="https://www.ivi.ru/watch/146018">IVI</a>

2. <b>Лёд</b> (2018)
История фигуристки, которая после травмы пытается вернуться к мечте.
🔹 <a href="https://www.kinopoisk.ru/film/1045585/">Кинопоиск</a> | <a href="https://start.ru/watch/lyod">START</a> | <a href="https://www.ivi.ru/watch/led">IVI</a>

3. <b>Притяжение</b> (2017)
Инопланетяне падают на Москву. Наши военные и учёные решают, что с ними делать.
🔹 <a href="https://www.kinopoisk.ru/film/1008448/">Кинопоиск</a> | <a href="https://start.ru/watch/prityazhenie">START</a>

4. <b>Движение вверх</b> (2017)
Легендарная победа советских баскетболистов над США в 1972 году.
🔹 <a href="https://www.kinopoisk.ru/film/1008448/">Кинопоиск</a> | <a href="https://start.ru/watch/dvizhenie-vverh">START</a>

5. <b>Батя</b> (2021)
Комедия-драма про отца, который воспитывал сына жёсткими методами.
🔹 <a href="https://www.kinopoisk.ru/film/1280498/">Кинопоиск</a> | <a href="https://start.ru/watch/batya">START</a>
""",
        reply_markup=kb.undo_keyboard
    )

@app.on_message(filters.command("amfilm") | filters.regex('Иностранные фильмы🎱'))
async def start_command(client: Client, message: Message):
    await message.reply(
        """
🎬 <b>Лучшие зарубежные фильмы</b> 🎬

1. <b>Достать ножи</b> (Knives Out, 2019)
<i>Остросюжетный детектив про гениального сыщика, который расследует загадочную смерть известного писателя. Семья подозреваемых — сплошное сборище отбитых.</i>

2. <b>Друзья Оушена</b> (Ocean's Eleven, 2001)
<i>Криминальная комедия о крутых аферистах, которые хотят провернуть мегаграбёж казино в Лас-Вегасе. Джордж Клуни, Брэд Питт, Мэтт Дэймон – просто топовый состав.</i>

3. <b>Подруги Оушена</b> (Ocean's 8, 2018)
<i>Женская версия классики: восемь дам с характером планируют дерзкое ограбление на элитном светском мероприятии.</i>

4. <b>Начало</b> (Inception, 2010)
<i>Кристофер Нолан, Ди Каприо, сны внутри снов, гениальная идея и взрывы мозга. Обязательно к просмотру.</i>

5. <b>Бойцовский клуб</b> (Fight Club, 1999)
<i>Фильм про офисного планктона, который находит смысл жизни в драках и анархии. Философия, психология, жёсткий твист в конце.</i>

6. <b>Марсианин</b> (The Martian, 2015)
<i>Мэтт Дэймон выживает в одиночку на Марсе, наука рулит, юмор присутствует, экшен тоже есть.</i>

7. <b>Поймай меня, если сможешь</b> (Catch Me If You Can, 2002)
<i>История про реального афериста, который в 16 лет начал обманывать банки и выдавать себя за пилота, врача, юриста. Том Хэнкс против Леонардо Ди Каприо – шикарное кино.</i>
""",
        reply_markup=kb.websiteamfilm_keyboard
    )

@app.on_message(filters.command("webamfilm") | filters.regex('Сайты🍡'))
async def start_command(client: Client, message: Message):
    await message.reply(
        """
🎬 <b>Лучшие зарубежные фильмы (с ссылками)</b> 🎬

1. <b>Достать ножи</b> (2019)
<a href="https://www.kinopoisk.ru/film/1047883/">Кинопоиск</a> | <a href="https://www.netflix.com/title/81067445">Netflix</a>

2. <b>Друзья Оушена</b> (2001)
<a href="https://www.kinopoisk.ru/film/402/">Кинопоиск</a> | <a href="https://www.hbomax.com/feature/urn:hbo:feature:GXdu2JAQC6YpDwgEAAAAM">HBO Max</a>

3. <b>Подруги Оушена</b> (2018)
<a href="https://www.kinopoisk.ru/film/1045585/">Кинопоиск</a> | <a href="https://www.hbomax.com/feature/urn:hbo:feature:GXkRjxwjQ7_JuwwEAAAHs">HBO Max</a>

4. <b>Начало</b> (2010)
<a href="https://www.kinopoisk.ru/film/447301/">Кинопоиск</a> | <a href="https://www.netflix.com/title/70131314">Netflix</a>

5. <b>Бойцовский клуб</b> (1999)
<a href="https://www.kinopoisk.ru/film/361/">Кинопоиск</a> | <a href="https://www.hulu.com/movie/fight-club-9b5e5d6e-9b1a-4b3d-9b7a-9b1a4b3d9b7a">Hulu</a>

6. <b>Марсианин</b> (2015)
<a href="https://www.kinopoisk.ru/film/258687/">Кинопоиск</a> | <a href="https://www.disneyplus.com/movies/the-martian/4K6YbnvWBZ6w">Disney+</a>

7. <b>Поймай меня, если сможешь</b> (2002)
<a href="https://www.kinopoisk.ru/film/328/">Кинопоиск</a> | <a href="https://www.netflix.com/title/60024916">Netflix</a>
""",
        reply_markup=kb.undo_keyboard
    )


app.run()