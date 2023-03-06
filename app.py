from flask import Flask, render_template, redirect
import check
import platform
import os


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/details')
def details():
    total = check.storage.total
    used = check.storage.used
    free = check.storage.free
    o_s = platform.system()
    arch = platform.machine()
    ver = platform.version()
    #ram
    ram_size_in_gb = check.storage.ram_size_in_gb
    
    return render_template('details.html', total=total, used=used, free=free, os=o_s, arch=arch, ver=ver, ram_size_in_gb=ram_size_in_gb)


@app.route('/config_page')
def config():
    return render_template('config.html')

@app.route('/hosting')
def hosting():
    return render_template('hosting.html')


if __name__ == "__main__":
    app.run(debug=True,port=4000)

    # directory = "/dfs-storage"

    # if not os.path.exists(directory):
    #     os.makedirs(directory)
    #     print("Directory created successfully")
    # else:
    #     print("Directory already exists")