if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Tony-Stark2021/MH-BOT.git /MH-BOT
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /MH-BOT
fi
cd /MH-BOT
pip3 install -U -r requirements.txt
echo "sᴛᴀʀᴛɪɴɢ 𝗗𝗞 𝗕𝗢𝗧𝘅........"
python3 bot.py
