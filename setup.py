import os

os.system("git clone https://github.com/xiph/rnnoise.git")
os.chdir("rnnoise")
os.system("./autogen.sh")
os.system("./configure")
os.system("make")
os.chdir("..")
print("You can now run rnnoise.py using this format: python rnnoise.py input.wav")
