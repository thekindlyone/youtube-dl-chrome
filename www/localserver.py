from flask import Flask, request
import subprocess
from savedialog import Selector
import os

app = Flask(__name__)

@app.route('/download' , methods=['POST'])
def start_download():
    url=request.form['url']
    dload(url)
    return 'success'

@app.route('/')
def hello():
    return 'Local server ON'

def dload(url):
    sel=Selector()
    directory=sel.get_save_dir()
    sel.kill()
    if directory:
        os.chdir(directory)
    subprocess.Popen(['gnome-terminal', '-x', 'youtube-dl',url])

if __name__ == '__main__':
    app.run(debug=True)


