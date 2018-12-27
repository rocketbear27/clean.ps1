#!/bin/bash
#REQUIRES SUDO PRIVILEGES
echo "Moving files..."
mv cleanscript.py /usr/bin/cleanscript
mkdir /lib/cleanscript
mv cleanscript_settings.txt /lib/cleanscript/cleanscript_settings.txt
echo "Making executable..."
chmod +x /usr/bin/cleanscript
echo "Done!"
echo
echo
echo "~~~~~~~~~~~~~~~~~~~~~"
echo "Thank you for installing"
echo "cleanscript!"
echo
echo "For basic usage information,"
echo "View the README file"
