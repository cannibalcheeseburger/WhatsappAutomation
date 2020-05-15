# Whatsapp Automation

This repository was created as a learning path to understand Selenium(Python) for automation.
It contains a python script to spam your target whatsapp contact with customized message(s).

## Installation

### Packages

```
python -m pip install -r requirements.txt
```
### Webdriver

Along with python packages you will require webdrivers.
Here i am using ChromDriver 81.0.4044.138.

You can either the webdriver included in repo or download your own depending on your browser and version.

For Chrome webdrivers different than used here:
<a href = "https://chromedriver.chromium.org/downloads" target="_blank">ChromeDrivers</a>


Or

If you have chocolatey installed run this in your Terminal:

```
choco install selenium-chrome-driver --pre 
```

### To run Script

```
python Spam.py
```
