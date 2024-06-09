if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/NischayYadav615/THEMOVIEBOT.git /NEWV-BOT
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /NEWV-BOT
fi
cd /NEWV-BOT
pip3 install -U -r requirements.txt
echo "Starting NEWVBOT...."
python3 bot.py
