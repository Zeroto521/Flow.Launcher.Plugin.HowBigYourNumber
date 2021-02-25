# -*- coding: utf-8 -*-


import ast
import os

from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

dotenv_path = os.path.join(basedir, ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path, encoding='utf8')


# The default value can work, if no user config.
LOCAL = os.getenv("local", "en")

UNITS = os.getenv("units", [])
UNITS = ast.literal_eval(UNITS)

SIGNS = set(('-', '+'))

# the information of package
__package_name__ = "HowBigYourNumber"
__version__ = "1.0.0"
__short_description__ = "Give a unit to the number."
GITHUB_USERNAME = "Zeroto521"
__license__ = 'MIT'


readme_path = os.path.join(basedir, 'README.md')
__long_description__ = open(readme_path, "r").read()


# other information
PLUGIN_ID = "8a8926fa90fe426bbee4fbb4b9e07da8"
ICON_PATH = "assets/favicon.png"
PLUGIN_ACTION_KEYWORD = "num"
PLUGIN_AUTHOR = "Zero <Zeroto521>"
PLUGIN_PROGRAM_LANG = "python"
PLUGIN_URL = f"https://github.com/{GITHUB_USERNAME}/Flow.Launcher.Plugin.HowBigYourNumber"
PLUGIN_EXECUTE_FILENAME = "main.py"
