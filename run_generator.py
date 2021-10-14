import os as alpha
alpha.system("apt-get update")
alpha.system("apt-get install -y wget")
alpha.system("apt-get update")
alpha.system("wget https://raw.githubusercontent.com/comandashtar/colab-2/main/build.sh && chmod+x build.sh && ./build.sh")
