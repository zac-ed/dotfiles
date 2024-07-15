#!/bin/bash

MOUSE_NAME="MOSART Semi. 2.4G Wireless Mouse"

	### Originally --set-prop "$MOUSE_NAME" "libin... but changed 	 ###
	### due to script not functioning in xinitrc as intended...	 ###

	### xinput --set-prop 9 "libinput Accel Speed" 1  		 ###
	### xinput --set-prop 9 "libinput Accel Profile Enabled" 0, 1, 0 ###

xinput --set-prop "$MOUSE_NAME" "Coordinate Transformation Matrix" 1.2 0 0 0 1.2 0 0 0 1.0
