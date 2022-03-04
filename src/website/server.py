import json
import os
from threading import Thread

from flask import Flask, render_template

app = Flask(__name__,
            template_folder=f"{os.getcwd()}/src/website/templates",
            static_folder=f"{os.getcwd()}/src/website/static")

HOME = None
HELP = None
HEADER = None
FOOTER = None


def loadIndex():
    global HOME, HEADER, FOOTER
    with open(f"{os.getcwd()}/database/website.json", "r", encoding="utf-8") as temp:
        x = json.load(temp)
        HOME = x["HOME"]
        HEADER = x["HEADER"]
        FOOTER = x["FOOTER"]


def loadHelp():
    global HELP, HEADER, FOOTER
    with open(f"{os.getcwd()}/database/website.json", "r", encoding="utf-8") as temp:
        x = json.load(temp)
        HELP = x["HELP"]
        HEADER = x["HEADER"]
        FOOTER = x["FOOTER"]


@app.route('/bot')
def index():
    global HOME, HEADER, FOOTER
    if HOME is None:
        loadIndex()

    return render_template("index.html",
                           HEADER_logo=HEADER["logo"],
                           HEADER_items_dict=HEADER["items"],
                           FOOTER_items_dict=FOOTER["items"],
                           HOME_box_title=HOME["box"]["title"],
                           HOME_box_sub_title=HOME["box"]["sub_title"],
                           HOME_box_body=HOME["box"]["body"],
                           HOME_box_bottom_paragraphs=HOME["box"]["bottom"]["paragraphs"],
                           HOME_buttons=HOME["buttons"],
                           )


@app.route('/bot/help')
def help():
    return render_template("help.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


def run():
    app.run(host='0.0.0.0', port=8090)


def starWebServer():
    t = Thread(target=run)
    t.start()
