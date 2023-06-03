# self_regex
This is web application with the ability to find matches in the text using regular expressions and replace these matches with text entered by the user.

[Design document](https://docs.google.com/document/d/16xMbB5Meyy-Vw155BB6pldhB_q_qHyHOx2ztTmDxJ6c/edit#heading=h.qokw92wctjes)

How to run?
## 1. Install required languages:
You should have installed Python and NodeJS on your machine.
[NodeJS here](https://nodejs.org/en/download) and [Python here](https://www.python.org/downloads/)
## 2. Clone this repository:
```bash
git clone https://github.com/olehmartynenko/self_regex.git
```
## 3. Run server:
```bash
cd backend
```
On Unix systems:
```bash
python3 -m venv venv
pip install flask
pip install flask_cors
python3 server.py
```
On Windows
```shell
python -m venv venv
pip install flask
pip install flask_cors
python server.py
```
## 4. Run a frontend:
```bash
cd frontend
npm i
npm start
```
And then type in your browser "localhost:3000"

## 5. App ready to use!
