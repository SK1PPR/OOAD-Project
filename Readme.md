# MediaWave

## About

MediaWave is a multi-purpose and easy-to-use media player that presents a user-friendly GUI, allowing users to access multiple features without spoiling their viewing experience.
The features include:

- **Playlists:** Users can create, import and edit playlists, allowing them to play any playlist with a single click.
- **GUI:** A highly intuitive and user-friendly GUI designed to make your experience as seamless and enjoyable as possible. Whether you're a novice or an experienced user, our GUI is engineered to be accessible, reducing the learning curve and ensuring efficient navigation.​
- **Editing:** Users can seamlessly trim files while playing, also allowing them to concatenate any number of such clips with a single click. ​
- **Drive Integration:** Users can automatically import media folders from the drive as a playlist, making it easy to share and receive media.​
- **File Support:** The player shows versatility, supporting various formats, from mp3, mp4, avk to mov and flv.​
- **Watch Party:** The player allows multiple users to watch video streams together as well chat with each other over a secure unified ingress platform called ngrok.

## Requirements

**Note: You can skip the first requirement if you do not wish to use the watch party features**

- **Requirement 1: Setting up ngrok** Before running the application you need to create a [ngrok](https://ngrok.com) and download the ngrok [executable](https://ngrok.com/download) for your system. After doing the steps above add your ngrok authtoken in line 2 of config.json and ngrok executable path to line 3 of config.json

- **Requirement 2: Installing the vlc media player** You need to install the [vlc](https://www.videolan.org/vlc/) media player (**64 bit version**).
If already installed you can skip this step.

- **Requirement 3: Installing codec (Skip this step if you are on a linux based operating system)** The download link for the codec is [here](https://files3.codecguide.com/K-Lite_Codec_Pack_1790_Basic.exe).

## Installation

Simply run the `setup.sh` script and after it is done you can run the following command to start the application: `python main.py`

## Maintainers

- Swapnil Garg - 22115150, swapnil_g@cs.iitr.ac.in  
- Anup Savaliya - 22114088, savaliya_ad@cs.iitr.ac.in
- Khushal Agarwal - 22114047, khushal_a@cs.iitr.ac.in
- Rushit Pancholi - 22114081, rushit_pp@cs.iitr.ac.in
- Vraj Tamakuwala - 22114098, tamakuwala_vs@cs.iitr.ac.in