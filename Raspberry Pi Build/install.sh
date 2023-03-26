#!/bin/bash

# Check if OpenCV is installed, install it if it's missing
if ! dpkg -s libopencv-dev >/dev/null 2>&1; then
    echo "OpenCV is not installed. Installing OpenCV..."
    sudo apt-get update
    sudo apt-get install -y libopencv-dev
fi

# Check if pytesseract is installed, install it if it's missing
if ! dpkg -s tesseract-ocr >/dev/null 2>&1; then
    echo "pytesseract is not installed. Installing pytesseract..."
    sudo apt-get update
    sudo apt-get install -y tesseract-ocr
fi

# Check if webvtt is installed, install it if it's missing
if ! python3 -c "import webvtt" >/dev/null 2>&1; then
    echo "webvtt is not installed. Installing webvtt..."
    pip3 install webvtt-py
fi

# Check if requests is installed, install it if it's missing
if ! python3 -c "import requests" >/dev/null 2>&1; then
    echo "requests is not installed. Installing requests..."
    pip3 install requests
fi

# Check if md5 is installed, install it if it's missing
if ! python3 -c "import hashlib" >/dev/null 2>&1; then
    echo "md5 is not installed. Installing md5..."
    sudo apt-get update
    sudo apt-get install -y python3-hashlib
fi

# Clone the program repository
git clone https://github.com/example/repo.git

# Navigate to the program directory
cd repo

# Ask the user if they want to run the program
read -p "Installation complete. Would you like to run the program now? [y/n]: " choice
case "$choice" in
    y|Y )
        # Run the program
        python3 program.py
        ;;
    n|N )
        echo "Exiting program."
        ;;
    * )
        echo "Invalid choice. Exiting program."
        ;;
esac