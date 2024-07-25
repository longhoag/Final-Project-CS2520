# Speech <--> Text Converter

In order to run the code on your machine, you would need to set up the environement and install necessary libraries

## Set up the environement
> [!NOTE]  
> Depend on your ```python``` and ```pip``` version that you would need to use ```python3``` or ```python```, ```pip3``` or ```pip``` as the command
>
> 


### Create and activate a virtual environment to avoid any conflicting packages or configurations
```python
python3 -m venv myenv
source myenv/bin/activate
```


### Install the required libraries for the program 
```python
pip3 install SpeechRecognition   #needed to recognize speech
pip3 install gtts pyttsx3        #needed for the voice after converting to speech
pip3 install pyaudio             #needed to handle cross-platform audio input/output
pip3 install playsound           #needed for audio playback
pip3 install setuptools
```

### Running the script 

```python
python3 main.py
```


## Output Demo
