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
echo "π²ππΊπππππ π¬ππππΎ π¬ππππΎπ π»π #ππ―π’πππ π²_ππ..."
python3 bot.py
