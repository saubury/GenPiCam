# GenPiCam

GenPiCam - *a RaspberryPi based camera that re-imagines the world with GenAI.*

Read the [blog](https://medium.com/@simon-aubury/genpicam-generative-ai-camera-dfd8123ac6f6) for more details

## Setup virtual python environment
Create a [virtual python](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) environment to keep dependencies separate. The _venv_ module is the preferred way to create and manage virtual environments. 

 ```console
python3 -m venv env
```

Before you can start installing or using packages in your virtual environment you’ll need to activate it.

```console
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
 ```

 ## Assumptions and setup

This code is definitely a rough, work-in-progress. You'll need to tinker with things to get it to work locally. Consider this code "inspiration" and not a complete solution.

- Setup a `discord_config.py` file with with a Discord token which has enough scope to interact with messages (you can copy [discord_config_EXAMPLE.py](./discord_config_EXAMPLE.py))
- It is assumed you have a Discord channel setup, and have added a Midjourney bot (with appropriate subscription). You'll need to add your Discord bot to the same channel so the token has sufficient scope. 
- The Discord web page should be open - as GenPiCam will literally be controlling the mouse and keyboard to interact with Midjourney bot.
- The _describe_ mode requires some very ugly code to interact with the file browser icon (literally the button you press to open the file selection dialog). Depending on your screen size, you may need to adjust the location of the _browse file_ mouse pointer location in [midjourney.py](midjourney.py)



## Usage

Basic usage; run interactive commands against Discord Midjourney bot to automatically chain actions. Does not require a RaspberryPi.
```bash
python generative_camera.py --auto
```

RaspberryPi usage; will dynamically import Raspberry Pi GPIO library
```bash
export DISPLAY=:0
python generative_camera.py  --enablePi --auto
```


## Issues and work around

If you get an error import Raspberry Pi GPIO library `import RPi.GPIO` try the following package updates

```bash
sudo apt-get install python3-dev python3-rpi.gpio
pip install RPi.GPIO
```



## Code credits & references

- [Discord Bot to Download Midjourney Images Automatically by Michael King](https://medium.com/@neonforge/how-to-create-a-discord-bot-to-download-midjourney-images-automatically-python-step-by-step-guide-3e76d3282871) - provided inspiration for using Python to download images from Midjourney
- [Midjourney](https://docs.midjourney.com/docs/command-list) - Midjourney command syntax for bot channels
- [discord.py](https://discordpy.readthedocs.io/en/stable/) - Python API wrapper for Discord.