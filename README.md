# CS162 Kanban Board

Link for demo: https://www.loom.com/share/f145f5b76d614f34b78d3dc962c34273

## Project Structure

`/static` css files and js.

`/static/assets` images.

`/templates` html files.

`/app.py` project initializer file.

`/tests` test files. Tests for: kanban operations (add, move, delete).


## Run Application

**macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 app.py
```

**Windows:**
```bash
python3 -m venv venv
venv\Scripts\activate.bat
pip3 install -r requirements.txt
python3 app.py
```

## Unit Tests

```bash
python3 -m unittest discover
```
