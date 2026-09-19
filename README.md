# CineShell

![Language](https://img.shields.io/badge/Language-Python-green?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-1.0.0-purple?style=for-the-badge)
![Time](https://img.shields.io/badge/Time-2h_13mins-blue?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-red?style=for-the-badge)

Welcome to CineShell! This repository houses a program that **plays any video in the TERMINAL**!

## Description

CineShell is a command-line based tool that allows you to play any video in greyscale in the terminal using ASCII characters. It has a responsive playback, which means it rescales the resolution of the video based on available/target resolution.

### Screenshots
<img width="2816" height="1762" alt="image" src="https://github.com/user-attachments/assets/b3f0f329-d0ef-4290-a403-354d0d1a4158" />

## Getting Started

### Dependencies
If you fork the repository rather than using a release, you require:
- Python 3.x
- The following libraries (`pip install`):
    - Numpy
    - OpenCV
 
### Installing
To fork the repository:
- Open your terminal:
    - Enter your preffered folder:
        - `cd <pathtoyourfolder>`
    - Clone the repsitory
        - `git clone https://github.com/astrokoala23/cineshell.git`
    - Open the main folder
        - `cd cineshell`
     
To use a release, go to http://github.com/astrokoala23/cineshell/releases, and download the latest release.

### Executing program
If you forked the repo:
- Open the parent folder of `main.py` in the terminal:
    - Use CineShell
        - Windows: `python main.py -fp <pathtovideo>`
        - Mac/Linux: `python3 main.py -fp <pathtovideo>`
    - Use example videos in the repo (filepaths below):
        - `assets/kingbob.mp4`
        - `assets/crabrave.mp4`
        - `assets/badapple.mp4`
        - NOTE: All videos were downloaded from Youtube

If you are using the executable:
- Open the parent folder of the executable in the terminal:
    - Provide permission to run (MacOS only):
        - `chmod +x <pathtoexecutable>` 
    - Use CineShell (MacOS currently, future version might have Linux/Windows):
        - MacOS/Linux: `./main -fp <pathtovideo>`
        - Windows: `main.exe -fp <pathtovideo>`

## License
This project is licensed under the MIT License - see the LICENSE.md file for details



