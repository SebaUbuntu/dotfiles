# DE setup

Using GNOME on EndeavourOS

## Packages

Install:

- pamac
- google-chrome
- spotify
  - spotify-adblock
- discord
- telegram-desktop
- visual-studio-code-bin
- android-studio
- android-studio-for-platform
- element-desktop
- gitkraken
- lineageos-devel
- gnome-firmware
- gnome-terminal
- gnome-shell-extension-arc-menu
- gnome-shell-extension-appindicator
  - libappindicator
  - libappindicator-gtk2
- gnome-shell-extension-dash-to-panel
- gnome-shell-extension-gtk4-desktop-icons-ng
- gnome-shell-extension-freon
- meld
- openrgb
  - i2c-tools
- android-tools
- gnome-remote-desktop
- htop
- python-pipx
- python-virtualenv
- python-poetry
- easyeffects
  - carla
  - calf
  - lsp-plugins-lv2
  - zam-plugins-lv2
  - mda.lv2
- wireguard-tools
- gnome-connections
- jdk-openjdk
- libc++
- ccache
- feishin-bin
- ghidra
  - ghidra-desktop
- libva-utils
- vdpauinfo
- vulkan-tools
- decibels
- fluidsynth
- qsynth
- soundfont-fluid
- ruby-bundler
- fastlane

Remove:

- xterm
- uxterm
- gnome-console
- gnome-text-editor

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

## pamac

- Enable AUR in settings
- Enable "Remove unnecessary dependencies"

## GNOME Settings

- Disable active angle
- Set number of workspaces to 1

## GNOME extensions

- appindicator-support (system)
- arcmenu (system)
- dash-to-panel (system)
- freon (system)
- gtk4-desktop-icons-ng (system)

## GNOME tweaks

- Fonts > Monospace Text > Cascadia Mono Regular 10
- Windows > Titlebar buttons > Maximize and minimize
- Set "Qogir-dark" as cursor theme
- Set "ZorinBlue-Dark" as icons and older applications theme

## Dash to Panel

- Disable "Display panels on all monitors"
- Hide "Show applications button"
- Move "Date and time" to the most right, after "Show desktop button"
- Style > App icon margin > 0
- Style > App icon padding > 8
- Style > Enable "Override panel theme background opacity"
- Style > Enable "Dynamic background opacity"

## Nautilus

- Order folders first
- Enable "Create shortcut" and "Permanently delete" actions on right click menu

## GNOME Terminal

- Set theme variant to "Light"

## Dash icons

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

## desktop-icons

- Set icons size to "Small"
