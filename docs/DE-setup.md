# DE setup

Using GNOME on EndeavourOS

## Packages

### System

- gnome-firmware
- gnome-shell-extension-appindicator
  - libappindicator
  - libappindicator-gtk2
- gnome-shell-extension-arc-menu
- gnome-shell-extension-astra-monitor
  - amdgpu_top
- gnome-shell-extension-dash-to-panel
- gnome-shell-extension-gtk4-desktop-icons-ng
- htop
- libva-utils
- openrgb
  - i2c-tools
- vdpauinfo
- vulkan-tools

Remove:

- uxterm
- xterm

### Core

Install:

- android-tools
- decibels
- discord
- easyeffects
  - carla
  - calf
  - lsp-plugins-lv2
  - zam-plugins-lv2
  - mda.lv2
- element-desktop
- feishin
- qsynth
  - fluidsynth
  - soundfont-fluid
- gnome-connections
- gnome-remote-desktop
- google-chrome
- jdk-openjdk
- meld
- python-pipx
- spotify
  - spotify-adblock
- telegram-desktop
- visual-studio-code-bin

### $\LaTeX$

- biber
- pandoc
- texlive
- texlive-lang

### Development

Install:

- android-studio
- android-studio-for-platform
- ccache
- fastlane
- ghidra
- gitkraken
- intellij-idea-ultimate-edition
- libc++
- lineageos-devel
- python-poetry
- python-virtualenv
- ruby-bundler
- rustrover
  - rustrover-jre
- webstorm
  - webstorm-jre

### Intel

- intel-media-driver
- libvdpau-va-gl (+ `VDPAU_DRIVER=va_gl` in `/etc/environment`)
- vulkan-intel

### NVIDIA

Install:

- nvidia
- nvidia-utils
- nvidia-settings
- libva-nvidia-driver

### CLEVO NP50DB

- clevo-drivers-dkms-git
- tuxedo-control-center-bin

## Configuration

### GNOME Settings

- Disable active angle
- Set number of workspaces to 1

### GNOME extensions

- appindicator-support (system)
- arcmenu (system)
- dash-to-panel (system)
- freon (system)
- gtk4-desktop-icons-ng (system)

### GNOME tweaks

- Fonts > Monospace Text > Cascadia Mono Regular 10
- Mouse & Touchpad > Enable "Paste on middle click"
- Windows > Titlebar buttons > Maximize and minimize
- Set "Qogir-dark" as cursor theme
- Set "ZorinBlue-Dark" as icons and older applications theme

### Dash to Panel

- Disable "Display panels on all monitors"
- Hide "Show applications button"
- Move "Date and time" to the most right, after "Show desktop button"
- Style > App icon margin > 0
- Style > App icon padding > 8
- Style > Enable "Override panel theme background opacity"
- Style > Enable "Dynamic background opacity"

### Nautilus

- Order folders first
- Enable "Create shortcut" and "Permanently delete" actions on right click menu

### GNOME Terminal

- Set theme variant to "Light"

### Dash icons

- Google Chrome
- Files
- Terminal
- Telegram
- Discord
- Element
- Spotify
- GitKraken
- Visual Studio Code
- Android Studio
- Android Studio for Platform

### desktop-icons

- Set icons size to "Small"

### GNOME text editor

- Indentation characters: Spaces
- Tabulation spaces: 4
- Indentation spaces: 4
- Disable "Restore session"
