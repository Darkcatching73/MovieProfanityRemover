HDMI Closed Captioning Filter for Raspberry Pi
This program is designed to take an HDMI input and extract the closed captioning (CC) track from the internet. It then searches through the CC track for swear words, and if any are found, it censors them and overlays the CC on the video with the audio muted.

Prerequisites
Before running the program, make sure the following dependencies are installed on your Raspberry Pi:

OpenCV
pytesseract
webvtt
requests
md5
You can install these dependencies by running the following commands:

bash
Copy code
sudo apt-get install python3-opencv
sudo apt-get install tesseract-ocr
pip3 install webvtt-py
pip3 install requests
pip3 install md5
Installation
To install the program, follow these steps:

Clone this repository onto your Raspberry Pi:
bash
Copy code
git clone https://github.com/Darkcatching73/hdmi-cc-filter.git
Navigate to the hdmi-cc-filter directory:
bash
Copy code
cd hdmi-cc-filter
Run the installer script to check for and install the required dependencies:
bash
Copy code
bash install.sh
Run the program:
bash
Copy code
python3 cc_filter.py
Usage
When you run the program, it will prompt you to connect an HDMI input. Once the input is detected, the program will automatically extract the CC track from the internet, search for swear words, censor them, overlay the CC on the video, and mute the audio if any swear words are found.

Limitations
The program currently only supports English closed captioning.
The program relies on accurate closed captioning data being available online, which may not always be the case.
The program may not accurately detect all instances of swear words in the CC track.
Contributing
If you find a bug or have a feature request, please open an issue on this repository. Pull requests are also welcome.

License
This program is licensed under the MIT License. See the LICENSE file for more information.
