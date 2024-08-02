# Video Editing Application README

## Overview

This Python script provides a graphical user interface (GUI) for basic video editing tasks using the `moviepy` library. The GUI is built with `tkinter` and allows users to perform various operations on video clips, including mixing, mirroring, resizing, adjusting speed, changing color effects, trimming, and adding audio. The final edited video is saved as "Final splash.mp4" by default.

## Requirements

To run this script, you'll need to have the following Python libraries installed:

- `tkinter` (comes pre-installed with Python)
- `moviepy` (for video editing)

You can install `moviepy` using pip:

```bash
pip install moviepy
```

## How to Use

1. **Prepare Your Files**: Place your video files (`song2.mp4`, `song3.mp4`, `song4.mp4`) and an audio file (`audio.mp3`) in the same directory as the script.

2. **Run the Script**: Execute the script using Python. This will open a GUI window.

3. **Perform Operations**:
   - **Mix**: Concatenates the three video clips (`song2.mp4`, `song3.mp4`, `song4.mp4`) into a single video.
   - **Mirror**: Applies a horizontal mirror effect to the first video clip (`song2.mp4`).
   - **Resize**: Resizes the first video clip based on a user-provided scale factor.
   - **Speed**: Adjusts the speed of the first video clip based on a user-provided speed factor.
   - **Color**: Modifies the color of the first video clip by adjusting its darkness level.
   - **Trim**: Cuts out a section from the first video clip based on user-provided start and end times.
   - **Audio**: Adds an audio track (`audio.mp3`) to the first video clip.

## Code Details

Here's a brief overview of the script:

- **Variables**:
  - `clip1`, `clip2`, `clip3`: Instances of `VideoFileClip` for different video files.
  
- **Functions**:
  - `mix()`: Concatenates `clip1`, `clip2`, and `clip3` and saves the result.
  - `mirror()`: Applies a horizontal mirror effect to `clip1` and saves the result.
  - `resize()`: Resizes `clip1` according to user input and saves the result.
  - `effects_speed()`: Adjusts the playback speed of `clip1` according to user input and saves the result.
  - `effects_colour()`: Changes the color of `clip1` based on user input and saves the result.
  - `trim()`: Trims `clip1` between user-defined start and end times and saves the result.
  - `audio_file()`: Adds an audio track to `clip1` and saves the result.

- **GUI**:
  - Built using `tkinter`, the interface has buttons for each function. When a button is clicked, the corresponding function is executed.

## Known Issues

- Ensure that all required files (`song2.mp4`, `song3.mp4`, `song4.mp4`, and `audio.mp3`) are present in the same directory as the script.
- The GUI does not handle exceptions, so make sure to enter valid inputs when prompted.

## Future Improvements

- Add error handling for file operations and user inputs.
- Implement functionality to select files through the GUI.
- Provide options to customize output file names and formats.

