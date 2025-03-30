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

https://kinobase.org/serial/221750-kak-izbezhat-nakazaniya-za-ubiystvo
https://kinobase.org/serial/228745-novichok
https://kinobase.org/serial/16938-vo-vse-tyazhkie
https://kinobase.org/serial/50284-sherlok
https://kinobase.org/serial/222988-sotnya
https://kinobase.org/serial/225133-milliardy
https://kinobase.org/serial/228064-horoshiy-doktor
""",
        reply_markup=kb.undo_keyboard
    )


@app.on_message(filters.command("webruss") | filters.regex('Сайты🪆'))
async def start_command(client: Client, message: Message):
    await message.reply(
        """
https://kinobase.org/serial/207319-kuhnya
https://kinobase.org/serial/226260-otel-eleon
https://kinobase.org/serial/230166-grand
https://kinobase.org/serial/44047-interny
https://kinobase.org/serial/220931-mazhor
https://kinobase.org/serial/230987-zvonite-dikaprio
https://kinobase.org/serial/225846-metod
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
https://kinobase.org/film/229958-holop
https://kinobase.org/film/215644-led
https://kinobase.org/film/221067-prityazhenie
https://kinobase.org/film/225150-dvizhenie-vverh
https://kinobase.org/film/232456-batya
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

https://kinobase.org/film/232833-dostat-nozhi
https://kinobase.org/film/102188-druzya-oushena
https://kinobase.org/film/195496-podrugi-oushena
https://kinobase.org/film/44764-nachalo
https://kinobase.org/film/361-boytsovskiy-klub
https://kinobase.org/film/84024-marsianin
https://kinobase.org/film/168-poymay-menya-esli-smozhesh
""",
        reply_markup=kb.undo_keyboard
    )


app.run()