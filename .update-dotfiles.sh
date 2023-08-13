#!/usr/bin/bash

echo "updating update script..."
cp ~/.update-dotfiles.sh ~/src/dotfiles/


echo "updating dotfiles..."

# copy i3 files to git repo "dotfiles"
cp -r ~/.config/i3/ ~/src/dotfiles/

echo "finished updating scripts and files!"
