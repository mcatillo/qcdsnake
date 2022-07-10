#! ./
echo ""
echo "[EN] Preparing for the installation method 2"
echo "[IT] Installazione metodo 2 in preparazione"
echo ""

game_position=~/.local/share/qcdsnake
src=src

mkdir $game_position &&
cp -r resources $game_position &&
cp -r database $game_position &&
mkdir $game_position/$src &&

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

echo "$desktopapp" | tee QCD-Snake.desktop &&
cp QCD-Snake $game_position/$src/ &&
cp QCD-Snake.desktop ~/.local/share/applications/ &&
cp QCD-Snake.desktop ~/Desktop/ &&

echo ""
echo "[EN] QCD-Game has been installed! You can close the window"
echo "[IT] QCD-Game è stato installato! Puoi chiudere la finestra"
echo ""

./QCD-Snake
