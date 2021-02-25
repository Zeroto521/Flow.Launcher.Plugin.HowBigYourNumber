# -*- coding: utf-8 -*-

import os
from copy import deepcopy
from typing import List

from flowlauncher import FlowLauncher, FlowLauncherAPI
from pyperclip import copy as copy2clipboard

from plugin.extensions import _l
from plugin.settings import SIGNS, UNITS, dotenv_path
from plugin.templates import *


class Main(FlowLauncher):
    messages_queue = []

    def query(self, param: str) -> List[dict]:
        if param:
            q = param.strip().split(".")[0]

            if len(str(q)) > len(UNITS):
                self.sendActionMess(
                    _l("WARNING: No Unit"),
                    _l("Please open the config file path and edit it."),
                    "openFolder",
                    [dotenv_path]
                )
                return self.messages_queue

            if q.isdigit() or (q[0] in SIGNS and q[1:].isdigit()):
                number_width = len(str(abs(int(q))))
                base, index = f"{q:.{number_width-1}e}".split('e')
                number_with_unit = f"{base} {UNITS[int(index)]}"

                self.sendActionMess(
                    number_with_unit,
                    _l("Click & Copy to Clipboard"),
                    "copy2clipboard",
                    [number_with_unit]
                )
            else:
                self.sendNormalMess(
                    _l("WARNING: What you input is not Numeric."),
                    _l("Please check the inputting.")
                )
        else:  # homepage, welcome words and introduction
            self.sendNormalMess(
                _l("How Big Your Number"),
                _l("Give a unit to the number.")
            )

        return self.messages_queue

    def sendNormalMess(self, title: str, subtitle: str):
        message = deepcopy(RESULT_TEMPLATE)
        message["Title"] = title
        message["SubTitle"] = subtitle

        self.messages_queue.append(message)

    def sendActionMess(self, title: str, subtitle: str, method: str, value: list):
        # information
        message = deepcopy(RESULT_TEMPLATE)
        message["Title"] = title
        message["SubTitle"] = subtitle

        # action
        action = deepcopy(ACTION_TEMPLATE)
        action["JsonRPCAction"]["method"] = method
        action["JsonRPCAction"]["parameters"] = value
        message.update(action)

        self.messages_queue.append(message)

    def copy2clipboard(self, value: str):
        copy2clipboard(value)

    def openFolder(self, path: str):
        os.startfile(path)
        FlowLauncherAPI.change_query(path)
