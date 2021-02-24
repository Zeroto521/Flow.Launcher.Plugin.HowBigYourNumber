# -*- coding: utf-8 -*-

import copy
import os
from typing import List

import pyperclip
from flowlauncher import FlowLauncher, FlowLauncherAPI

from plugin.extensions import _l
from plugin.settings import UNITS, dotenv_path
from plugin.templates import *


class Main(FlowLauncher):
    messages_queue = []

    def query(self, param: str) -> List[dict]:
        q = param.strip().split(".")[0]
        if q:
            if len(str(q)) > len(UNITS):
                self.sendActionMess(
                    _l("WARNING: No Unit"),
                    _l("Please open the config file path and edit it."),
                    "openFolder",
                    [dotenv_path]
                )
                return self.messages_queue

            if q.isdigit():
                res = f"{q[0]}{UNITS[len(q)-1]}"

                self.sendActionMess(
                    res,
                    _l("Click & Copy to Clipboard"),
                    "copy2clipboard",
                    [res]
                )
            else:
                self.sendNormalMess(
                    _l("WARNING: What you input is not Numeric."),
                    _l("Please check the inputting.")
                )
        else:
            self.sendNormalMess(
                _l("How Big Your Number"),
                _l("Give a unit to the number.")
            )

        return self.messages_queue

    def sendNormalMess(self, title: str, subtitle: str):
        message = copy.deepcopy(RESULT_TEMPLATE)
        message["Title"] = title
        message["SubTitle"] = subtitle

        self.messages_queue.append(message)

    def sendActionMess(self, title: str, subtitle: str, method: str, value: list):
        # information
        message = copy.deepcopy(RESULT_TEMPLATE)
        message["Title"] = title
        message["SubTitle"] = subtitle

        # action
        action = copy.deepcopy(ACTION_TEMPLATE)
        action["JsonRPCAction"]["method"] = method
        action["JsonRPCAction"]["parameters"] = value
        message.update(action)

        self.messages_queue.append(message)

    def copy2clipboard(self, value):
        pyperclip.copy(str(value).strip())

    def openFolder(self, path: str):
        os.startfile(path)
        FlowLauncherAPI.change_query(path)