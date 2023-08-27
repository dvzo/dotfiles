#!/usr/bin/bash
#
echo "updating dotfiles!"

echo "updating update script..."
cp ~/.update-dotfiles.sh ~/src/dotfiles/

echo "updating xdg toggle portals script..."
cp ~/.toggle-xdg-portals.sh ~/src/dotfiles/

# echo "updating i3 files..."
# moving from i3 to hyprland
# cp -r ~/.config/i3/ ~/src/dotfiles/

echo "updating hyprland files..."
# delete current and copy hyprland files to git repo "dotfiles"
cp -r ~/.config/hypr/ ~/src/dotfiles/

echo "updating waybar files..."
cp -r /etc/xdg/waybar ~/src/dotfiles/

echo "updating eww files..."
cp -r ~/.config/eww/ ~/src/dotfiles/

echo "updating vimrc..."
cp ~/.vimrc ~/src/dotfiles/

echo "finished updating scripts and files!"
