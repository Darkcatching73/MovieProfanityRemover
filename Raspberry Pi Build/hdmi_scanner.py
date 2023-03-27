import cv2
import pytesseract
import requests
from webvtt import WebVTT

# Set up Tesseract OCR engine
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# Set up OpenCV video capture
cap = cv2.VideoCapture(0)

# Set up WebVTT closed captioning parser
parser = WebVTT()

# Load swear words list from a localized CSV file hosted online
response = requests.get('https://gist.github.com/mcmaloney/1262336/raw/e726672c406c3ed3bcde4da3337cca6199dc61da/profanity.csv')
swear_words_list = response.text.split(',')

# Mute audio output
def mute_audio():
    os.system("amixer -q -D pulse sset Master 0%")

# Unmute audio output
def unmute_audio():
    os.system("amixer -q -D pulse sset Master 100%")

while True:
    # Capture frame from HDMI input
    ret, frame = cap.read()

    # Use OpenCV to detect the name of the movie or show
    movie_or_show_name = pytesseract.image_to_string(frame)

    # Search for closed captioning track online
    cc_url = f'https://example.com/{movie_or_show_name}.vtt'
    response = requests.get(cc_url)

    if response.status_code == 200:
        # Parse closed captioning track using WebVTT
        captions = parser.read(response.text)

        # Remove swear words from closed captioning track and censor them
        for caption in captions:
            caption_text = caption.text
            for swear_word in swear_words_list:
                if swear_word in caption_text:
                    caption_text = caption_text.replace(swear_word, '*' * len(swear_word))
            caption.text = caption_text

        # Create a new image with the closed caption overlay
        caption_image = frame.copy()
        caption_text = '\n'.join([caption.text for caption in captions])
        cv2.putText(caption_image, caption_text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        # Display the image with closed caption overlay
        cv2.imshow('Video with Closed Captioning', caption_image)

        # Mute audio output if swear words are present
        for caption in captions:
            caption_text = caption.text
            for swear_word in swear_words_list:
                if swear_word in caption_text:
                    mute_audio()
                    break

        # Unmute audio output if no swear words are present
        unmute_audio()

    else:
        print('Closed captioning track not found')

    # Press q to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and destroy all windows
cap.release()
cv2.destroyAllWindows()