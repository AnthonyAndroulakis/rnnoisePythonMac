# rnnoisePythonMac
python wrapper for rnnoise (just automates some of the pre and post processing)

# Requirements
- WAVE files (these will be the input files, ideal sampling rate = 48000; output files will also be in WAVE format)
- Mac OS
- ffmpeg
- sox
- python

# Setup
1. on a Mac OS, make sure you have ffmpeg, sox, and python
2. `git clone https://github.com/AnthonyAndroulakis/rnnoisePythonMac.git`
3. `cd rnnoisePythonMac`
4. `git clone https://github.com/xiph/rnnoise.git`
5. `cd rnnoise`
6. `./autogen.sh`
7. `./configure`
8. `make`
9. `cd ../`

# Run it (after Setup steps)
`python rnnoise.py input.wav` #output will be in ./rnnoiseoutput folder, with the same name as the input file
