cd /home/sktang/project/serverAlert/
gunicorn3 --workers=1 app:app -b 0.0.0.0:7998 --daemon --reload