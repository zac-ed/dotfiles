#/bin/bash

	### For virtualisation, gui file explorer, appearance, ###
	###   archiving,   neovim setup,  package management   ###
sudo pacman -Syu xorg-server xorg-xinit go qtile ufw rofi alacritty base-devel thunar zip unzip lxappearance qt5ct p7zip xclip ristretto firefox virt-manager bridge-utils qemu-full libguestfs netcat ebtables libguestfs libvirt cargo flatpak nodejs npm lua

	###    Obviously    ###
git clone https://aur.archlinux.org/yay.git
cd yay && makepkg -si
cd .. && rm -rf yay

yay -S brave-bin
	
	### Starship prompt ###
curl -sS https://starship.rs/install.sh | sh

sudo cp ../rosy.rasi /usr/share/themes/rofi
cp ../rosy.rasi ~

	### Get Agave Nerd Fonts ###
url="https://github.com/ryanoasis/nerd-fonts/releases/download/v3.0.2/Agave.zip"

curl -LJO "$url"

if [ $? -eq 0 ]; then
  unzip Agave.zip
  sudo mv *tf /usr/share/fonts
else
  echo "Failed to download agave nerd font!"
fi

	### Add self to groups! ###
groups=("kvm" "qemu" "libvirt" "video" "audio" "input")

for group in "${groups[@]}"; do
    sudo usermod -a -G "$group" zaced 
done

	###  Enable virtualisation services! ###
sudo systemctl start libvirtd
sudo systemctl enable libvirtd
sudo virsh net-autostart default

	### Something I always forget to do! ###
	### 	      Firewall:        	     ###
sudo systemctl enable --now ufw
sudo ufw enable
sudo ufw start

	### Themes reminder since you can't curl this! ###
echo "visit this link: https://www.gnome-look.org/p/1310034/ for your icon pack"
echo "visit this link: https://www.gnome-look.org/p/1276216 for your GTK theme"

reboot
