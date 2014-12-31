import platform, os

if platform.system()=='Linux':
    DIRECTORY=os.path.expanduser('~/Videos') # Set your default download direcory variable for LINUX
else:
    DIRECTORY="H:\\Videos\\"  #Set your default download direcory variable for WINDOWS
WindowsConEmu=False #Set this to True if you want to use ConEmu in place of CMD. I will..