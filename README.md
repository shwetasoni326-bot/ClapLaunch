ClapLaunch

An automated, background audio-detection tool built with Python that listens for double-clap patterns to instantly launch applications on Windows.

Overview
ClapLaunch runs silently in the background, continuously processing microphone input. Upon detecting a double clap within a defined threshold, it automatically triggers predefined tasks or applications (such as launching YouTube or running system scripts).

Key Features
- Real-time Audio Processing: Uses PyAudio and NumPy to analyze ambient volume peaks.
- Double-Clap Logic: Built-in thresholding to prevent false positives from single loud noises.
- Automation Ready: Integrates seamlessly with Windows Task Scheduler via batch scripts (run_clap.bat) to launch on startup.
- Lightweight: Minimal CPU/RAM footprint during background monitoring.

Tech Stack
- Language: Python 3.x
- Libraries: pyaudio, numpy, os, time
- OS: Windows (Task Scheduler, Batch Processing)

Getting Started

1. Prerequisites
Ensure Python 3.x is installed on your system. Install required dependencies:
pip install -r requirements.txt

2. Execution
To run the detection script directly:
python main.py

3. Windows Startup Automation
To make ClapLaunch run automatically when Windows starts:
1. Open Windows Task Scheduler.
2. Create a new Task pointing to run_clap.bat.
3. Set the trigger to "At log on" or "At startup".
4. Set the "Start in" directory to your project folder path.

License
This project is open-source and available under the MIT License.
