# Web Macro
Web macro template

## Environment
* Python 3.9
* Selenium 4.1
* Chrome 96

## Quick start
```shell
git clone https://github.com/ppd0523/webmacro
cd webmacro
python -m venv venv
pip install -r requirements.txt

python main.py
```

## Build Executable
This step confirmed Windows(10, 11), Mac OSX(15.0)
```shell
pip install pyinstaller
pyinstaller main.py --onefile --noconsole
```

## Running with Chrome extension
Creating the `extensions/`, place the `*.crx` as shown below
```shell
webmacro
├── README.md
├── extensions
│   └── metamask_10_6_4_0.crx
├── main.py
├── requirements.txt
├── tester.ipynb
└── tk2.py
```
