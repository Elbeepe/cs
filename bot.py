import requests
import mysql.connector
import asyncio
from telegram import Bot, Update, InputMediaPhoto
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram.error import TelegramError

GROUP_CHAT_ID = '-1002227465176'
TOKEN = '6566767891:AAE56kR2JPccB6OL7DPEamXV74uVdFxdrto'
API_URL = 'https://cshost.com.ua/api?action=getServersStatus&serverid=34339&token=3c7f0fa6e4e16229965cf50360d97e4e'

# Initialize the bot
bot = Bot(token=TOKEN)

# Параметри підключення до бази даних
DB_HOST = "cshost.site"
DB_USER = "legofdef"
DB_PASSWORD = "Potop4ik0305"
DB_DATABASE = "legofdef"

photo_admin = ['Adminmenu.png','admint.png','adminct.png']
photo_vip = 'vip.png'
photo_logo = 'logo.jpg'

# Initialize the database connection
def get_db_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_DATABASE
    )

async def welcome_new_member(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    for member in update.chat_member.new_chat_members:
        if not member.is_bot:
            welcome_message = (
                f"◽️ Вітаємо, {member.full_name}, !\n"
                f"🥳 Дякуємо що завітав до нас.\n"
                f"🎁 За підключення ти отримуєш VIP на тиждень\n"
                f"〽️ З питаннями та пропозиціями стосовно серверу до ⬆️\n"
                f"🔱 Создатель cерверу - @potop4ik24\n"
                f"🔵 Cайт серверу : legofdef.cshost.site\n"
                f"〽️ З питаннями та пропозиціями стосовно серверу до ⬆️\n"
                f"======================================================\n"
                f"📝Також тут доступні команди.\n"
                f"      /info - Інформація про сервер\n"
                f"      /online - Переглянути онлайн\n"
                f"      /admin - Послуга [Admin]\n"
                f"      /vip - Послуга [Vip]\n"
            )
            await context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_message)


async def get_server_admin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        # Параметри для Telegram бота
        # Отримання даних з API
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        name_serv = data.get('server_name', 'Немає інформації про Сервер')
        server_admin = (
            f"🇺🇦 Cервер: {name_serv} 🇺🇦\n"
            f"🔹Послуга: Адмін🔹\n"
            f"〽️Вартість: 200грн\n"
            f"⏱Термін дії: 1️⃣ місяць\n"
            f"🧑🏻‍💻За покупкою до @potop4ik24\n"
            f"—————————————————\n"
            f"📝Можливості Адмін📝\n"
            f"1) Кікати гравців\n"
            f"2) Банити граців\n"
            f"3) Вдарити/вбити граців\n"
            f"4) Створити голосування\n"
            f"5) Змінювати карти\n"
            f"6) Змінювати команду гравця\n"
            f"7) Робити рестарт мапи\n"
            f"8) Видавати будь яку зброю\n"
            f"9) Видавати мут гравцям [amx_gagmenu]\n"
            f"9) Доступ до Віп меню зброї\n"
            f"10) Префікс [Адмін] в чаті\n"
            f"11) Імунітет від Kick/Ban/Mute\n"
            f"12) Граната для лікування\n"
            f"13) Модель гравця [Admin]\n"
            f"14) Для зручного доступу до меню пропишіть в консолі \nbind КНОПКА ultimate\n"
        )      
        # Формування повідомлення про користувачів, які онлайн більше 2
        user_messages = []
        # Перевірка наявності і відправка повідомлень
        media_group = []
        for photo_path in photo_admin:
            with open(photo_path, 'rb') as photo:
                media_group.append(InputMediaPhoto(media=photo))
        if user_messages:
            final_message = server_admin
            if media_group:
                await context.bot.send_media_group(chat_id=update.effective_chat.id, media=media_group, caption=final_message)
            else:
                await update.message.reply_text(final_message)
        else:
            if media_group:
                await context.bot.send_media_group(chat_id=update.effective_chat.id, media=media_group, caption=server_admin)
            else:
                await update.message.reply_text(server_admin)

    except requests.exceptions.RequestException as e:
        await update.message.reply_text(f'Помилка при отриманні даних: {e}')

async def get_server_vip(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        # Параметри для Telegram бота
        # Отримання даних з API
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        name_serv = data.get('server_name', 'Немає інформації про Сервер')
        icon_curl = data.get('icon', None)
        server_vip = (
            f"🇺🇦 Cервер: {name_serv} 🇺🇦\n"
            f"🔹Послуга: Vip🔹\n"
            f"〽️Вартість: 100грн\n"
            f"⏱Термін дії: 1️⃣ місяць\n"
            f"🧑🏻‍💻За покупкою до @potop4ik24\n"
            f"—————————————————\n"
            f"📝Можливості Vip📝\n"
            f"1) Доступ до Віп меню зброї\n"
            f"2) Префікс [Vip] в чаті\n"
            f"3) Граната для лікування\n"
            f"4) Позначка VIP в таблиці рахунку TAB\n"
            f"5) Модель гравця [Vip]\n"
            f"6) Для зручного доступу до меню пропишіть в консолі \nbind КНОПКА vipmenu\n"
        )
        # Формування повідомлення про користувачів, які онлайн більше 2
        user_messages = []
        # Перевірка наявності і відправка повідомлень
        if user_messages:
            final_message = server_vip
            if icon_curl:
                await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(photo_vip, 'rb'), caption=final_message)
            else:
                await update.message.reply_text(final_message)
        else:
            if icon_curl:
                await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(photo_vip, 'rb'), caption=server_vip)
            else:
                await update.message.reply_text(server_vip)

    except requests.exceptions.RequestException as e:
        await update.message.reply_text(f'Помилка при отриманні даних: {e}')


async def get_server_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        # Параметри для Telegram бота
        site_http = 'legofdef.cshost.site'
        # Отримання даних з API
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        name_serv = data.get('server_name', 'Немає інформації про Сервер')
        ip_address = data.get('server_address', 'Немає інформації про Сервер')
        server_stat = data.get('server_status', 'Немає інформації про Сервер')
        map_name = data.get('server_maps', 'Немає інформації про карту')
        online_status = data.get('server_maxonline', 'Немає інформації про онлайн')
        slots = data.get('server_maxslots', 'Немає інформації про онлайн')
        icon_curl = data.get('icon', None)
        server_messageinfo = (
            f"🇺🇦 Cервер: {name_serv} 🇺🇦\n"
            f"🌐 Сайт - {site_http}\n"
            f"📝 Правила серверу - /rules /rulesadmin /rulesbanadmin"
            f"🔹 Статус - {server_stat}\n"
            f"🎮 IP: {ip_address}\n"
            f"🗺 Карта: {map_name}\n"
            f"🧍🏻‍♂️ Гравців: {online_status} / {slots}\n"
            f"==========================\n"
            f"🔱 Создатель - @potop4ik24\n"
            f"〽️ З питаннями та пропозиціями стосовно серверу до ⬆️\n")      
        # Формування повідомлення про користувачів, які онлайн більше 2
        user_messages = []
        # Перевірка наявності і відправка повідомлень
        if user_messages:
            final_message = server_messageinfo + "\n".join(user_messages)
            if icon_curl:
                await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(photo_logo, 'rb'), caption=final_message)
            else:
                await update.message.reply_text(final_message)
        else:
            if icon_curl:
                await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(photo_logo, 'rb'), caption=server_messageinfo)
            else:
                await update.message.reply_text(server_messageinfo)

    except requests.exceptions.RequestException as e:
        await update.message.reply_text(f'Помилка при отриманні даних: {e}')

async def get_server_rules(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        # Параметри для Telegram бота
        site_http = 'legofdef.cshost.site'
        # Отримання даних з API
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        name_serv = data.get('server_name', 'Немає інформації про Сервер')
        icon_curl = data.get('icon', None)
        server_messageinfo = (
            f"🇺🇦 Правила серверу: {name_serv} 🇺🇦\n"
            f"🌐 Сайт - {site_http}\n"
            f"🔱 Создатель - @potop4ik24\n"
            f"〽️ З питаннями та пропозиціями стосовно серверу до ⬆️\n"
            f"==========================\n"
            f"📝Загальний стан: Правила всім гравців сервера.📝\n"
            f"1.1. Незнання чи нерозуміння правил не звільняє від відповідальності за їх недотримання.\n"
            f"1.2. Заборонено рекламувати або надавати будь-яку інформацію про інші ігрові сервери.\n"
            f"1.3. Заборонено давати інформацію де знаходиться противник коли тебе воскрешають за таке порушення бан на 1 день!\n"
            f"1.4. Заборонено переходити в спектр та бігати під час голосування за карту за таке порушення бан на 1 день!\n"
            f"1.5. Заборонено ригати у мікрофон за таке порушення ГАГ на 1 день!\n\n"
            f"2.1. Заборонено ображати гравців, виявляти національну або расову ворожнечу, що порушують чинні норми етики та моралі. ✚ Покарання: /попередження, GAG від 30 хвилин до 24 годин/. Образа батьків GAG НАЗАВЖДИ/\n"
            f"2.2. заборонено багаторазове повторення однієї й тієї фрази (flood), моніторинг. ✚ Покарання: /попередження, GAG, BAN від 5 до 60 хвилин/.\n"
            f"2.3. заборонено вживання виразів та використання імен, спрямованих на розпалювання міжнаціональної та міжконфесійної ворожнечі. ✚ Покарання: /попередження, BAN від 60 хвилин до 24 годин/.\n"
            f"2.4. заборонено плагіатників. заборонено використовувати ніки з образливим змістом, нечитані ніки, а також заборонено використовувати клан теги.✚ Покарання: /попередження, BAN від 5 до 60 хвилин/.\n"
            f"2.5. Заборонено обговорювати дії адміну під час ігрового процесу. ✚ Покарання: /попередження, BAN від 30 до 60 хвилин/.\n"
            f"2.6. Провокація гравців спрямована на дії, що порушують правила, заборонена в будь-якій формі. ✚ Покарання: /попередження, BAN від 5 до 60 хвилин/.\n\n"
            f"3.1. заборонено використання всякого роду читів (cheats), у тому числі з метою тестування самого читання чи античитерської програми. ✚ Покарання: /BAN перманентний (НАЗАВЖДИ)/.\n"
            f"-Заборонені будь-які зміни текстур карток, у тому числі однотонні картки (які можуть надавати перевагу).\n"
            f"-Заборонено палітру кольорів 16 біт.\n\n"
            f"4.1. Заборонено злісне кемперство, ситуація, коли гравець сховався в затишному місці і чекає, поки супротивник пробіжить повз. ✚ Покарання:/попередження, стукнути/slay/кік.\n"
            f"4.2. Заборонено використання текстур, баг карт. ✚ Покарання: попередження, BAN від 5 до 30 хвилин/.\n"
            f"4.3. Заборонено закуповувати більше одного комплекту гранат і більше одного раунду, а також розкидка кількох гранат з точки респауна, покарання - бан від 5 хвилин до 6 годин\n"
            f"4.4. Заборонено брати через команду /anew - 100hp кілька разів за раунд, бан від 30 хвилин до 6 годин\n"
            f"4.5. Заборонено моніторити розташування гравців за допомогою соціальних мереж та голосових програм (Skype, TeamSpeak 3, RaidCall та ін.).\n\n"
            f"5.1. При спілкуванні з адміністрацією сервера гравець має бути ввічливий, ввічливий і терплячий. Гравець повинен коротко, виразно та без використання сленгу розповісти про свою проблему або відповісти на задані Адміном питання.\n"
            f"5.2. Гравцю забороняється висловлюватися про його професійні здібності адміна, саркастично насміхатися з нього.\n"
            f"5.3. Забороняється просити Адміна зробити щось, що не входить до його обов язків.\n"
            f"5.4. При відповідях питання Адміна забороняється приховування інформації, брехня, введення в оману.\n"
            f"5.5. Забороняється звати Адміна без причини, створювати перешкоди та відволікати Адміна від виконання обовязків.\n\n"
            f"〽️Примітка: Головний адміністратор Potop4ik (@potop4ik24) залишає за собою одноосібне право звільнити від покладених повноважень адміністратора без пояснення причин останньому, наділити виходячи з власних переконань гідного, що має досвід адміністрування людини повноваженнями адміністратора на свій розсуд.\n\n"
            f"〽️Зайшовши на сервер, ви погоджуєтесь з правилами! У разі порушення правил кошти не повертаються. Повернення коштів можливе 24 години після оплати у разі дотримання правил проекту!"
        )      
        # Перевірка наявності і відправка повідомлень
        user_messages = []
        if user_messages:
            server_messageinfo = server_messageinfo
            if icon_curl:
                await update.message.reply_text(server_messageinfo)
            else:
                await update.message.reply_text(server_messageinfo)
        await update.message.reply_text(server_messageinfo)
            

    except requests.exceptions.RequestException as e:
        await update.message.reply_text(f'Помилка при отриманні даних: {e}')

async def get_server_rulesadmin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        # Параметри для Telegram бота
        site_http = 'legofdef.cshost.site'
        # Отримання даних з API
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        name_serv = data.get('server_name', 'Немає інформації про Сервер')
        icon_curl = data.get('icon', None)
        server_messageinfo = (
            f"🇺🇦 Правила серверу: {name_serv} 🇺🇦\n"
            f"🌐 Сайт - {site_http}\n"
            f"🔱 Создатель - @potop4ik24\n"
            f"〽️ З питаннями та пропозиціями стосовно серверу до ⬆️\n"
            f"==========================\n"
            f"📝Правила Адміністрації📝.\n"
            f"6.2. У разі, якщо порушення правил адміністратором мало місце, адміна чекає на покарання. Залежно від ступеня тяжкості порушення буде винесено рішення про покарання - від попередження до позбавлення прав адміністратора та бана на сервері.\n"
            f"6.3. Якщо ж буде виявлено факт лжесвідчення і злочинний намір з метою обмовити адміна, то суворе покарання понесе людина, яка подала скаргу.\n\n"
            f"📝Адміністратор сервера зобов язаний📝 (вправі):\n"
            f"7.1. Знати та дотримуватись загальних правил серверів\n"
            f"7.2. Використовувати повноваження адміністратора виключно на користь підтримки порядку під час ігрового процесу та нормального функціонування сервера.\n"
            f"7.3. Підтримувати ігровий процес на сервері може, задовольняє більшість гравців.\n"
            f"7.4. Вживати заходів дисциплінарної дії на гравців, які перешкоджають нормальному ходу ігрового процесу.\n"
            f"7.5. Припиняти застосування гравцями ненормативної лексики з метою приниження честі та гідності інших гравців.\n"
            f"Кикати або виписувати бани просто так, до цього відноситься і ворожість до людини. Використовувати при лазні образливі та незрозумілі причини."
            f"7.6. Припиняти всі види реклами та не допускати указних дій зі свого боку.\n"
            f"7.7. Прислухатись до думки гравців.\n"
            f"7.8. Видалити з сервера гравців, що знаходяться у списку Spectators більше пяти раундів поспіль, якщо сервер повний (20/20).\n"
            f"7.9. Видаляти гравців із сервера, які порушують правила.\n"
            f"7.10. Кожен адміністратор повинен грати з увімкненим voice_enable 1, щоб стежити за порядком на сервері.\n"
            f"7.11. Кожен адміністратор розглядає свою заявку на розбан сам. Якщо заявка залишилася без розгляду 24 години, зняття прав адміністрування на 3 дні!\n"
            f"7.12. Забороняється загрожувати гравцеві баном, кіком без усіляких причин.\n"
            f"7.13. Адміністратор повинен стежити за грою гравця перед баном. Якщо адмін зайшов наприкінці карти, він має право дати бан гравцю, щоб переглянути гру на повній карті.\n"
            f"7.14. Забороняється перебувати у спектрах більше 1 години, при частих порушеннях цього правила, у адміністратора забирається імунітет від (kick, ban, slay).\n"
            f"7.15. Якщо Адмін вважає за потрібне перевірити гравця, він робить скрини має право забанити гравця, щоб той предявив - демо чи скрини.\n"
            f"7.16. При підозрі у використанні софту забороняється видавати бан менше, ніж на максимальний термін.\n\n"
            
            f"〽️Примітка: Головний адміністратор Potop4ik (@potop4ik24) залишає за собою одноосібне право звільнити від покладених повноважень адміністратора без пояснення причин останньому, наділити виходячи з власних переконань гідного, що має досвід адміністрування людини повноваженнями адміністратора на свій розсуд.\n\n"
            f"〽️Зайшовши на сервер, ви погоджуєтесь з правилами! У разі порушення правил кошти не повертаються. Повернення коштів можливе 24 години після оплати у разі дотримання правил проекту!"
        )      
        # Формування повідомлення про користувачів, які онлайн більше 2
        user_messages = []
        if user_messages:
            server_messageinfo = server_messageinfo
            if icon_curl:
                await update.message.reply_text(server_messageinfo)
            else:
                await update.message.reply_text(server_messageinfo)
        await update.message.reply_text(server_messageinfo)
            

    except requests.exceptions.RequestException as e:
        await update.message.reply_text(f'Помилка при отриманні даних: {e}')

async def get_server_rulesbanadmin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        # Параметри для Telegram бота
        site_http = 'legofdef.cshost.site'
        # Отримання даних з API
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        name_serv = data.get('server_name', 'Немає інформації про Сервер')
        icon_curl = data.get('icon', None)
        server_messageinfo = (
            f"🇺🇦 Правила серверу: {name_serv} 🇺🇦\n"
            f"🌐 Сайт - {site_http}\n"
            f"🔱 Создатель - @potop4ik24\n"
            f"〽️ З питаннями та пропозиціями стосовно серверу до ⬆️\n"
            f"==========================\n"
            f"📝Адміністратору сервера заборонено:📝\n"
            f"8.1. Порушувати правила, встановлені для серверів.\n"
            f"8.2. Кікати, вбивати, банити гравців, з особистої неприязні або без причин!\n"
            f"8.3. Ображати гравців, грубити гравцям, видавати неадекватні бани.\n"
            f"8.4. Знімати чужі бани та GAGі.\n"
            f"8.5. Використання адмінського голосування за картку та номінація 2 карт!\n"
            f"Адміністратор Не може самовільно: змінювати карту / робити дострокове голосування / або забирати вибрані вже заздалегідь карти іншими гравцями /maps .\n"
            f"Тривалість будь-якої картки має тривати до 15 раундів. Після 15 раундів старший адмін має право запустити дострокове голосування Якщо на сервері 18 і менше осіб, то картка змінюється без голосування на de_dust2, de_dust2_2х2\n"
            f"8.6. Заборонено обговорювати поведінку інших адміністраторів.\n"
            f"8.6. Адміністратор зобовязаний озвучити причину kick/slay на прохання гравця, який був кікнутий/убитий\n"
            f"8.7. Заборонено передавати іншим гравцям свою Адмінку/Vip/Меценат (зняття прав без повернення коштів)\n"
            f"8.8. ЗАБОРОНЕНО ДАВАТИ СЛОТ ГРАВЦЯМ, ЯКЩО СЕРВЕР ЗАПОВНЕНИЙ ! КІКАТИ МОЖНА ТІЛЬКИ СПЕКТОРІВ І АФК\n"
            f"8.9. Якщо VIP-гравець веде себе некоректно по відношенню до гравців сервера та адмінів (образа і т.д.), то на прохання адміна, у нього відключається послуга антибан, для застосування карних заходів.\n"
            f"8.10. Купівля будь якої зброї у 1 раунді заборонена за порушення бан на 1 день!\n"
            f"Vip-гравець та Адміністратор вправі перебуває у спектрах трохи більше 5-7 раундів.\n\n"
            f"В іншому випадку старший адміністратор має право зробити /kick\n\n"
            f"〽️Примітка: Головний адміністратор Potop4ik (@potop4ik24) залишає за собою одноосібне право звільнити від покладених повноважень адміністратора без пояснення причин останньому, наділити виходячи з власних переконань гідного, що має досвід адміністрування людини повноваженнями адміністратора на свій розсуд.\n\n"
            f"〽️Зайшовши на сервер, ви погоджуєтесь з правилами! У разі порушення правил кошти не повертаються. Повернення коштів можливе 24 години після оплати у разі дотримання правил проекту!"
        )      
        # Формування повідомлення про користувачів, які онлайн більше 2
        user_messages = []
        # Перевірка наявності і відправка повідомлень
        user_messages = []
        if user_messages:
            server_messageinfo = server_messageinfo
        if icon_curl:
            await update.message.reply_text(server_messageinfo)
        else:
            await update.message.reply_text(server_messageinfo)
            
    except requests.exceptions.RequestException as e:
        await update.message.reply_text(f'Помилка при отриманні даних: {e}')


async def get_server_online(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        API_URL = 'https://cshost.com.ua/api?action=getServersStatus&serverid=34339&token=3c7f0fa6e4e16229965cf50360d97e4e'
        site_http = 'legofdef.cshost.site'
        # Отримання даних з API
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        name_serv = data.get('server_name', 'Немає інформації про Сервер')
        ip_address = data.get('server_address', 'Немає інформації про Сервер')
        server_stat = data.get('server_status', 'Немає інформації про Сервер')
        map_name = data.get('server_maps', 'Немає інформації про карту')
        online_status = data.get('server_maxonline', 'Немає інформації про онлайн')
        slots = data.get('server_maxslots', 'Немає інформації про онлайн')
        icon_curl = data.get('icon', None)
        server_messageonline = (
            f"🇺🇦 Cервер: {name_serv} 🇺🇦\n"
            f"🌐 Сайт - {site_http}\n"
            f"🎮 IP: {ip_address}\n"
            f"🗺 Карта: {map_name}\n"  
            f"🧍🏻‍♂️ Гравців: {online_status} / {slots}\n\n")
        # Формування повідомлення про користувачів, які онлайн більше 2
        user_counter = 1
        user_messages = []
        for user in data.get('users', []):
            if int(user.get('ping', 0)) > 2:  # Якщо ping більше 2
                name = user.get('name', '')
                frag = user.get('frag', '')
                time = user.get('time', 'Невідомий')
                user_message = (
                    f"👤 {user_counter}) {name} : [{frag} | {time}]"
                )
                user_messages.append(user_message)
                user_counter += 1  # Збільшити лічильник

        # Перевірка наявності і відправка повідомлень
        if user_messages:
            final_message = server_messageonline + "\n".join(user_messages)
            if icon_curl:
                await context.bot.send_photo(chat_id=update.effective_chat.id, photo=icon_curl, caption=final_message)
            else:
                await update.message.reply_text(final_message)
        else:
            if icon_curl:
                await context.bot.send_photo(chat_id=update.effective_chat.id, photo=icon_curl, caption=server_messageonline)
            else:
                await update.message.reply_text(server_messageonline)

    except requests.exceptions.RequestException as e:
        await update.message.reply_text(f'Помилка при отриманні даних: {e}')
        

def main() -> None:
    TOKEN = '6566767891:AAE56kR2JPccB6OL7DPEamXV74uVdFxdrto'
    application = Application.builder().token(TOKEN).build()
    # Запуск періодичної перевірки бази даних
    application.add_handler(CommandHandler("info", get_server_info))
    application.add_handler(CommandHandler("online", get_server_online))
    application.add_handler(CommandHandler("admin", get_server_admin))
    application.add_handler(CommandHandler("rules", get_server_rules))
    application.add_handler(CommandHandler("rulesadmin", get_server_rulesadmin))
    application.add_handler(CommandHandler("rulesbanadmin", get_server_rulesbanadmin))
    application.add_handler(CommandHandler("vip", get_server_vip))
    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()
