#!/bin/bash

yellow='\e[1;33m'
blueF='\e[1;34m'
BAR='█║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║█'


# func to show progress bar
showProgressBar ()
{
    echo
	sleep 1 & while [ "$(ps a | awk '{print $1}' | grep $!)" ] ; do for X in '-' '\' '|' '/'; do echo -en "\b$X"; sleep 0.1; done; done
    echo
	echo

    for i in {1..50}; do
        echo -ne "\r             ${BAR:0:$i}"
        sleep 0.04
    done
    echo
}

echo -e $blueF"  [*] Installing ..."
rm -f .git/hooks/commit-msg
cp -f commit-msg.py .git/hooks/commit-msg
chmod ug+x .git/hooks/
showProgressBar
echo -e $yellow"  [*] Installed successfully"