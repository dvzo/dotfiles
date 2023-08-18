#!/usr/bin/bash

echo "updating update script..."
cp ~/.update-dotfiles.sh ~/src/dotfiles/

echo "updating dotfiles..."

# copy i3 files to git repo "dotfiles"
# temporarily moving from i3 to hyprland
# cp -r ~/.config/i3/ ~/src/dotfiles/

# copy hyprland files to git repo "dotfiles"
cp -r ~/.config/hypr/ ~/src/dotfiles/

echo "finished updating scripts and files!"
