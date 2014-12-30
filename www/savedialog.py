import pygtk
import gtk

class Selector:
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



if __name__ == '__main__':
    sel=Selector()
    print sel.get_save_dir()
    sel.kill()