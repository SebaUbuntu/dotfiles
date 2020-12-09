#!/bin/bash
#
# Copyright (C) 2020 The Android Open Source Project
#
# SPDX-License-Identifier: Apache-2.0
#
# SebaUbuntu's dotfiles setup script
# Setup all my stuff (scripts, configs, etc.)
#

GIT_USER_NAME="Sebastiano Barezzi"
GIT_USER_EMAIL="barezzisebastiano@gmail.com"
AOSP_MAIN_DIR="/mnt/Android"

packageinstall() {
	echo "Installing package(s): $1"
	if [ "$(command -v apt)" != "" ]; then
		sudo apt install -y $1
	elif [ "$(command -v pacman)" != "" ]; then
		sudo pacman -S --noconfirm $1
	else
		echo "No compatible package manager found, exiting"
		exit
	fi
}

# Copy every file from the repo to the current home folder
cp -R * ~/

# Add ~/bin to PATH, so scripts inside it can be executed
echo 'export PATH="~/bin:$PATH"' >> ~/.bashrc

# Enable ccache on AOSP building
echo "export USE_CCACHE=1
export CCACHE_EXEC=/usr/bin/ccache
export CCACHE_DIR=${AOSP_MAIN_DIR}/ccache" >> ~/.bashrc

# Source build/envsetup.sh if found
echo '
if [ -f "build/envsetup.sh" ]; then
	echo "AOSP build/envsetup.sh found, sourcing..."
	source build/envsetup.sh
	echo "Done"
fi' >> ~/.bashrc

# Install git
packageinstall git

# Set git infos
git config --global user.name "Sebastiano Barezzi"
git config --global user.email "barezzisebastiano@gmail.com"

# Add the Gerrit Change-id hook
mkdir -p ~/.git/hooks
git config --global core.hooksPath ~/.git/hooks
curl -Lo ~/.git/hooks/commit-msg https://review.lineageos.org/tools/hooks/commit-msg
chmod u+x ~/.git/hooks/commit-msg
