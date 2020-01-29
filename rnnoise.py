#rnnoise.py, requirements: ffmpeg, sox, rnnoise, python
import os, sys

def run(filename):
    os.system("mkdir -p inputraw")
    os.system("mkdir -p outputraw")
    os.system("mkdir -p rnnoiseoutput")

    print("Pre-processing audio...") #wav to pcm raw
    os.system("ffmpeg -i "+filename+" -f s16le -ac 1 -ar 48000 ./inputraw/"+filename[:-4]+".raw") #convert to raw

    print("Applying rnnoise algorithm to audio...") #rnnoise
    os.system("./rnnoise/examples/rnnoise_demo ./inputraw/"+filename[:-4]+".raw ./outputraw/"+filename[:-4]+".raw")

    print("Post-processing audio...") #pcm raw to wav
    os.system("sox -t raw -r 48000 -b 16 -e signed-integer -c 1 outputraw/"+filename[:-4]+".raw rnnoiseoutput/"+filename)
    os.system("rm -rf inputraw")
    os.system("rm -rf outputraw")

    print("Audio-filtering completed!")

run(sys.argv[1])
