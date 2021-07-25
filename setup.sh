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
for file in .bashrc-overlay .xprofile; do
	cp "${file}" ~/
done

for dir in .ssh bin; do
	cp -R "${dir}" ~/
done

# Source .bashrc additions
echo 'source ~/.bashrc-overlay' >> ~/.bashrc

# Install git
packageinstall git

# Set git infos
git config --global user.name "${GIT_USER_NAME}"
git config --global user.email "${GIT_USER_EMAIL}"

# Add the Gerrit Change-id hook
mkdir -p ~/.git/hooks
git config --global core.hooksPath ~/.git/hooks
curl -Lo ~/.git/hooks/commit-msg https://review.lineageos.org/tools/hooks/commit-msg
chmod u+x ~/.git/hooks/commit-msg
