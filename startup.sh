#!/bin/bash
cd /home/sktang/project/serverAlert/
gunicorn3 --workers=1 app:app -b 0.0.0.0:7998 --daemon --reload
cd /home/sktang/project/lnbAlert/
gunicorn3 --workers=1 app:app -b 0.0.0.0:7997 --daemon --reload
