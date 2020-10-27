## Hari Libur Indonesia Generator
This code is meant to generate Indonesian public holiday for specific year. This will output the public holiday to json format which you can parse/decode it for your apps.

---
#### Prerequisite
You have to set up API for google calendar and grant permission to your service account on google developer console. Then, download the json private key and replace the google-service-account.json in src directory. Failed to do so, may prevent the script to work properly.

#### Installation
Make sure you already installed pip and venv, then apply the following command to install the dependencies

To create virtual env and activate it, appy the following command on your project directory:

```
python3 -m venv env &&
source env/bin/activate
```
```
pip install -r requirements.txt
```
After the installation completed, run the main.py script on src directory with

    main.py <full digit year>
    e.g: main.py 2020

A json formatted file will be produced in dist folder.