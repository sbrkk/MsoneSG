class script(object):
    START_TXT = """<b>๐ง๐พ๐ {},  ๐จ ๐บ๐ ๐  ๐ฅ๐๐๐๐พ๐ ๐ก๐๐ ๐ฌ๐บ๐ฝ๐พ ๐ฅ๐๐ ๐ณ๐พ๐บ๐ ๐ฌ๐๐๐๐พ ๐ฌ๐๐๐๐พ๐ .</b></b>
"""
    HELP_TXT = """สแดส {}
สแดสแด ษชs แดส สแดสแด แดแดแดแดแดษดแดs."""
    ABOUT_TXT = """โ ๐ฌ๐ ๐ญ๐บ๐e : ๐.๐๐ฐ๐ฐ๐ฅ๐ฎ๐ข๐ฏ
โ ๐ข๐๐พ๐บ๐๐๐ : <a href='https://t.me/aboutme_DK'>Dแด ๐ฎ๐ณ</a>
โ ๐ซ๐บ๐๐๐๐บ๐๐พ : ๐ฏ๐๐๐๐๐ ๐ฅ 
โ ๐ซ๐๐ป๐๐บ๐๐ : ๐ฏ๐๐๐๐๐๐บ๐ ๐บ๐๐๐๐ผ๐๐ ๐ข.๐ฃ๐ฉ.๐ฃ 
โ ๐ฒ๐พ๐๐๐พ๐ : Contabo
โ ๐ฃ๐บ๐๐บ๐ป๐บ๐๐พ : <a href='https://www.mongodb.com'>๐ฌ๐๐๐๐๐ฃ๐ก ๐ฅ๐๐พ๐พ ๐ณ๐๐พ๐</a>
โ ๐ก๐๐๐๐ฝ ๐ฒ๐๐บ๐๐๐ : ๐ต9.8 [BeTa]"""
    SOURCE_TXT = """<b>NOTE:</b>

- เดเดชเตเดชเต เดเดฟเดเตเดเตเด เดจเตเดเตเดเดฟ เดเดฐเตเดจเตเดจเต .

<b>DEVS:</b>
- <a href=https://t.me/AboutMe_DK>dk [OFFLINE]</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and ๐๐ผ๐๐๐ธ will respond whenever a keyword is found the message

<b>NOTE:</b>
1. ๐๐ผ๐๐๐ธ should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
โข /filter - <code>add a filter in chat</code>
โข /filters - <code>list all the filters of a chat</code>
โข /del - <code>delete a specific filter in chat</code>
โข /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- ๐๐ผ๐๐๐ธ Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. ๐๐ผ๐๐๐ธ supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/dk_botx)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
โข /connect  - <code>connect a particular chat to your PM</code>
โข /disconnect  - <code>disconnect from a chat</code>
โข /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of ๐๐ผ๐๐๐ธ

<b>Commands and Usage:</b>
โข /id - <code>get id of a specified user.</code>
โข /info  - <code>get information about a user.</code>
โข /imdb  - <code>get the film information from IMDb source.</code>
โข /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
โข /logs - <code>to get the rescent errors</code>
โข /stats - <code>to get status of files in db.</code>
โข /delete - <code>to delete a specific file from db.</code>
โข /users - <code>to get list of my users and ids.</code>
โข /chats - <code>to get list of the my chats and ids </code>
โข /leave  - <code>to leave from a chat.</code>
โข /disable  -  <code>do disable a chat.</code>
โข /ban  - <code>to ban a user.</code>
โข /unban  - <code>to unban a user.</code>
โข /channel - <code>to get list of total connected channels</code>
โข /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """โ าษชสแดs sแดแด แดแด: <code>{}</code>
โ แดsแดสs: <code>{}</code>
โ ษขสแดแดแดs: <code>{}</code>
โ แดแดแดแดแดษชแดแด: <code>{}</code> ๐ผ๐๐ฑ"""
 
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}

๐ซ๐๐ ๐ป๐ #๐ฐ๐๐ฒ๐ฉ๐ค๐ฌ๐ฌ๐ก๐ช๐๐ซ
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}

๐ซ๐๐ ๐ป๐ - #AbOutMe_DK
"""
