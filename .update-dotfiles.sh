#!/usr/bin/bash

echo "updating update script..."
cp ~/.update-dotfiles.sh ~/src/dotfiles/

echo "updating xdg toggle portals script..."
cp ~/.toggle-xdg-portals.sh ~/src/dotfiles/

echo "updating dotfiles..."

# copy i3 files to git repo "dotfiles"
# temporarily moving from i3 to hyprland
# cp -r ~/.config/i3/ ~/src/dotfiles/

echo "copying hyprland files..."
# copy hyprland files to git repo "dotfiles"
cp -r ~/.config/hypr/ ~/src/dotfiles/

echo "copying waybar files..."
cp -r /etc/xdg/waybar ~/src/dotfiles/

echo "copying eww files..."
cp -r ~/.config/eww/ ~/src/dotfiles/

echo "copying vimrc..."
cp ~/.vimrc ~/src/dotfiles/

echo "finished updating scripts and files!"
