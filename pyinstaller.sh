#!/usr/bin/env bash

pyinstaller -D -F -n fotosort -w -i camera.ico fotosort.py settings.py my_gui/main_window.py my_gui/dialog_settings.py my_gui/dialog_about.py