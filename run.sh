#!/usr/bin/env bash
set -e
source "./venv/bin/activate"
python -u pnu.pythonanywhere.py
deactivate

# nohup /home/arsalanse/pnu/run.sh > custom-output.log &
# zip -r pnu.zip pnu/ -x pnu/venv/\*
