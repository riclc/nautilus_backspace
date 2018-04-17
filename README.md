*Nautilus Backspace*
-----------------------
Brings back the Backspace shortcut to Nautilus


### Prerequisites
To work properly, you will need to have the following packages:

```
NautilusPython [Nautilus Python](https://wiki.gnome.org/Projects/NautilusPython)
gi 
python2-gobject
```

## Installation
-----------------------
### Debian-based distributions)
1) Install the requirements:
```
$ sudo apt-get install python-nautilus python2-gobject (Debian-based distributions)
$ pip install --user gi
```

2) Download `Backspace-Back.py` and put it here: `.local/share/nautilus-python/extensions/`
(you might have to create this directory first)
```
mkdir -p .local/share/nautilus-python/extentions
mv Backspace-Back.py .local/share/nautilus-python/extentions
```

### Fedora
1) Install the requirements
```
sudo dnf install nautilus-python python2-gobject
pip install --user gi
```

3) Restart Nautilus
```
nautilus -q
```
