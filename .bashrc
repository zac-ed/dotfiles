##########
# bashrc #
##########


	### set env var for using compiled ###
	###  rust apps and  rust binaries  ###
export PATH="$HOME/.cargo/bin:$PATH"

	### Path for qtile binary: ###
export PATH="/home/zaced/.local/lib/python3.11/site-packages/qtile/bin:$PATH"

export PATH="/home/zaced/.local/bin:$PATH"


	### Draws a cute fetch on ###
	###     terminal open     ###
macchina

	### Starship prompt ###
eval "$(starship init bash)"


	### Sets env var for qt5ct ### 
	###    to work properly    ###
export QT_QPA_PLATFORMTHEME=qt5ct

export NVIM_CONFIG=~/.config/nvim

	### For rofi to not weep! ###
export LC_MESSAGES=en_GB.UTF-8
export LC_ALL=en_GB.UTF-8

	### Finds my aliases ###
source ~/.bash_aliases


[ -f ~/.fzf.bash ] && source ~/.fzf.bash
