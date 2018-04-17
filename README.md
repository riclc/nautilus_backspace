*Nautilus Backspace*
-----------------------
Brings back the Backspace shortcut to Nautilus

### Installing Prerequisites
To work properly, you will need to have the following packages:

```
gi
python2-gobject
```

## Installation
-----------------------
1) Install [Nautilus Python](https://wiki.gnome.org/Projects/NautilusPython)
```
* Debian-based distributions)
apt-get install python-nautilus python2-gobject (Debian-based distributions)

* Fedora
sudo dnf search nautilus-python python2-gobject ()
pip install gi
```
 
2) Download `Backspace-Back.py` and put it here: `.local/share/nautilus-python/extensions/`
```
(you might have to create this directory first)
mkdir -p .local/share/nautilus-python/extentions
```

3) Restart Nautilus
```
nautilus -q
```
