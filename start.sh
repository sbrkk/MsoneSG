if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Abidpknew/filteroli.git /filteroli
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /filteroli
fi
cd /filteroli
pip3 install -U -r requirements.txt
echo "𝖲𝗍𝖺𝗋𝗍𝗂𝗇𝗀 𝖲𝗎𝗓𝗓𝗒 𝖻𝗒 #𝗔𝗯𝗢𝘂𝘁𝗠𝗲_𝗗𝗞..."
python3 bot.py
