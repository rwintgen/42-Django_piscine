#!/bin/sh

LIB_DIR="local_lib"
LOG_FILE="local_lib.log"
PYTHON_PROGRAM="my_program.py"

pip install --upgrade pip >> $LOG_FILE 2>&1
echo -n "Current pip version: " 
pip --version | awk '{print $2}'

echo "Beginning installation..." > $LOG_FILE

if [ -d "$LIB_DIR" ]; then
	echo "Removing existing $LIB_DIR..." >> $LOG_FILE
	rm -rf "$LIB_DIR"
fi

echo "Fetching content from remote repository..." >> $LOG_FILE
git clone https://github.com/jaraco/path.git "$LIB_DIR" >> $LOG_FILE 2>&1

echo "Installing path module..." >> $LOG_FILE
cd "$LIB_DIR"
pip install . >> ../$LOG_FILE 2>&1
if [ $? -ne 0 ]; then
	echo "Installation failed!" >> ../$LOG_FILE
	exit 1
fi

echo "Packaging $LIB_DIR..." >> ../$LOG_FILE
touch __init__.py
cd ..

echo "Successfully installed path module!" >> $LOG_FILE

python3 $PYTHON_PROGRAM