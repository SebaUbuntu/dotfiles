#!/bin/bash
#
# Copyright (C) 2020 The Android Open Source Project
#
# SPDX-License-Identifier: Apache-2.0
#
# SebaUbuntu's dotfiles setup script
# Setup all my stuff (scripts, configs, etc.)
#

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &> /dev/null && pwd)"

GIT_USER_NAME="Sebastiano Barezzi"
GIT_USER_EMAIL="barezzisebastiano@gmail.com"

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
for file in $(ls -Ap "${SCRIPT_DIR}" | grep -v /); do
	cp "${SCRIPT_DIR}/${file}" ~/
done

for dir in $(ls -Ap "${SCRIPT_DIR}" | grep /); do
	cp -R "${SCRIPT_DIR}/${dir}" ~/
done

# Source .bashrc additions
BASHRC_OVERLAY_STRING='source ~/.bashrc-overlay'
if [ "$(cat ~/.bashrc | grep "${BASHRC_OVERLAY_STRING}")" = "" ]; then
	echo "${BASHRC_OVERLAY_STRING}" >> ~/.bashrc
fi

# Install git
packageinstall git

# Set git infos
git config --global user.name "${GIT_USER_NAME}"
git config --global user.email "${GIT_USER_EMAIL}"

# Add the Gerrit Change-id hook
mkdir -p ~/.git/hooks
git config --global core.hooksPath ~/.git/hooks
#curl -Lo ~/.git/hooks/commit-msg https://review.lineageos.org/tools/hooks/commit-msg
rm -f ~/.git/hooks/commit-msg
ln -s ~/.githooks/commit-msg ~/.git/hooks/commit-msg
chmod u+x ~/.git/hooks/commit-msg

# Add Nautilus "New document" templates
mkdir -p "$(xdg-user-dir TEMPLATES)"
touch "$(xdg-user-dir TEMPLATES)/Empty text file.txt"
