= some games for palladiumpi with gamepad input =

pong and tetris from pygames and https://www.101computing.net/pong-tutorial-using-pygame-getting-started/ adapted
to a palladium-pi game device (Palladium TV 500 with black and white screen and Raspbian Raspbery Pi 1 with composite output)

joystick-input.py used for starting games from the menu and in-game controller
only the first gamepad is used by python inputs library (https://inputs.readthedocs.io/en/latest/user/intro.html)

select	-> ALT+F4
start	-> WIN key
A 	-> Return
B 	-> Escape
A+B	-> toggle gamepad as OS input (for using the gamepad inside games or toggling the lxdmenu)

the script is started using this joystick-input.desktop file in /etc/xdg/autostart
the Path variable is important for python scripts

"""
[Desktop Entry]
Type=Application
Name=joystick-input
Comment=Joystick input
NoDisplay=true
Exec=/home/pi/src/joystick/joystick-input.py
Path=/home/pi/src/joystick
Terminal=false
Categories=Application;
"""

add game to lxd menu, add game.desktop file in directory ~/.local/share/applications
"""
[Desktop Entry]
Type=Application
Name=Asteroids
Comment=Asteroids pygame
Icon=/usr/share/pixmaps/minecraft-pi.png
StartupNotify=true
NoDisplay=false
Exec=/home/pi/src/AsteroidsInfinity/AsteroidsInfinity.py
Path=/home/pi/src/AsteroidsInfinity
Terminal=false
Categories=Application;Game;
"""
