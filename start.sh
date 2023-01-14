if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/sbrkk/MsoneSG.git /MsoneSG
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /MsoneSG
fi
cd /MsoneSG
pip3 install -U -r requirements.txt
echo "𝖲𝗍𝖺𝗋𝗍𝗂𝗇𝗀 𝖬𝗌𝗈𝗇𝖾 𝖬𝗈𝗏𝗂𝖾𝗌 𝖻𝗒 #𝗔𝗯𝗢𝘂𝘁𝗠𝗲_𝗗𝗞..."
python3 bot.py
