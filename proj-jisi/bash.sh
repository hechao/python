#! /bin/sh
cd /root/python/proj-jisi/
python jisi.py
mail -s 'The bond info today!22' formblackt@gmail.com < log.html
