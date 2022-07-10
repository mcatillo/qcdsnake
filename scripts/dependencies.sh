#! ./
echo ""
echo "[EN] Preparing for the installation (it will take a while)"
echo "[IT] Installazione in preparazione (ci vorrà qualche minuto per il completamento)"
echo ""

#   Create the location to put the Game material

game_position=~/.local/share/qcdsnake
src=src

mkdir $game_position &&
cp -r resources $game_position &&
cp -r database $game_position &&
mkdir $game_position/$src &&
alias activate=". game-env/bin/activate"

# Define the game app

desktopapp=$"#!/usr/bin/env xdg-open
[Desktop Entry]
Comment[en_US]=Pedagogical Game on QCD Phyisics
Comment[it_IT]=Gioco Pedagogico per la Fisica della QCD
Description[en_US]=Pedagogical Game on QCD Phyisics
Description[it_IT]=Gioco Pedagogico per la Fisica della QCD
Exec=$game_position/$src/QCD-Snake
Icon=$game_position/resources/logo.ico
Name[en_US]=QCD Snake
Name=QCD Snake
Path=$game_position/$src
StartupNotify=true
Terminal=false
Type=Application
Categories=Game;Application;
Version=0.0"

# Install python if not installed and install other useful tools

python3 -m venv game-env &&
source game-env/bin/activate &&
python3 -m pip install -U pygame &&
python3 -m pip install pyautogui &&
python3 -m pip install --upgrade Pillow &&
pip install pyinstaller &&
pip install screeninfo &&
pyinstaller --onefile -w --icon=./resources/logo.ico ./src/main.py --name=QCD-Snake &&
deactivate &&
mv dist/QCD-Snake .
cp QCD-Snake $game_position/$src/ &&
rm QCD-Snake.spec &&
rm -r build/ game-env/ dist/

# Define desktop application

echo "$desktopapp" | tee QCD-Snake.desktop &&
cp QCD-Snake.desktop ~/.local/share/applications/ &&
cp QCD-Snake.desktop ~/Desktop/ &&
rm QCD-Snake.desktop &&
#cp --preserve=links QCD-Snake.desktop ~/Desktop/ &&

echo ""
echo "[EN] QCD-Game has been installed! You can close the window"
echo "[IT] QCD-Game è stato installato! Puoi chiudere la finestra"
echo ""

./QCD-Snake





