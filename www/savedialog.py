import platform
Windows=False
if platform.system()=="Windows":
    Windows=True
if not Windows:
    import pygtk, gtk
else:
    try:
        import Tkinter as tk 
        from tkFileDialog import askdirectory
        python=2
    except ImportError:
        from tkinter.filedialog import askdirectory
        import tkinter as tk
        python=3

class LinuxSelector:
    def __init__(self):
        self.dialog=gtk.FileChooserDialog('Download to..',
                                            None,
                                            gtk.FILE_CHOOSER_ACTION_SELECT_FOLDER,
                                            (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                              gtk.STOCK_OPEN, gtk.RESPONSE_OK))

        self.dialog.set_default_response(gtk.RESPONSE_OK)

    def get_save_dir(self):
        response=self.dialog.run()
        if response == gtk.RESPONSE_OK:
            return self.dialog.get_filename()
        elif response == gtk.RESPONSE_CANCEL:
            return None

    def kill(self):
        self.dialog.destroy()

class WindowsSelector:
    def __init__(self):
        self.window=tk.Tk()

        self.window.withdraw()
        self.window.lift()
    def get_save_dir(self):
        self.folder=askdirectory()
        return self.folder

if __name__ == '__main__':
    if Windows:

        sel=WindowsSelector()
        print (sel.get_save_dir())
        
       
    else:
        sel=Selector()
        print (sel.get_save_dir())
        sel.kill()
