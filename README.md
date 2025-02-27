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
pip3 install SpeechRecognition   
pip3 install gtts pyttsx3        
pip3 install pyaudio             
pip3 install playsound          
pip3 install setuptools
```


_SpeechRecognition: needed to recognize speech_

_gtts pyttsx3: needed for the voice after converting to speech_

_pyaudio: needed to handle cross-platform audio input/output_

_playsound: needed for audio playback_




### Running the script 

```python
python3 main.py
```


## Output Demo
![Screenshot 2024-07-26 at 7 25 19 PM](https://github.com/user-attachments/assets/96e5e788-197d-4dad-8aa8-e16488135fa6)
