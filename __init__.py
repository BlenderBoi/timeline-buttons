bl_info = {
    "name": "Timeline Buttons",
    "author": "TinkerBoi",
    "version": (1, 0, 0),
    "blender": (4, 2, 0),
    "description": "Put the buttons in timeline to other animation related editors, Affected Editors - Dopesheet Editor, Graph Editor, NLA Editor, Sequencer",
    "doc_url": "",
    "tracker_url": "https://support.tinkerboi.com",
    "category": "Animation",
}

import bpy
from . import main

modules = [main]


def register():
    for module in modules:
        module.register()


def unregister():
    for module in modules:
        module.unregister()


if __name__ == "__main__":
    register()
