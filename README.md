# Py Cryptography CLI App

Encrypt & decrypt string using cryptography.io

CLI app included in distribution folder (dist/py-cryptography-cli.exe)

## Setup for Local Development

1. Creating a virtual environment
```
py -m venv venv
```
2. Activate the environment
```
.\venv\Scripts\activate
```
3. Install all of the packages using requirements.txt
```
pip install -r requirements.txt
```
4. Run cli application 
```
py py-cryptography-cli.py -h
```
5. Build cli output (more refer to : https://pyinstaller.org/en/stable/usage.html)
```
pyinstaller py-cryptography-cli.spec
```
6. Export a list of all installed packages (Optional)
```
pip freeze > requirements.txt
```
7. Leaving the environment
```
deactivate
```
