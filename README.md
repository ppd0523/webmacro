# Web Macro
Web macro template

## Environment
* python 3.9
* selenium 4.1
* chrome 96

## Quick start
```shell
git clone ...
cd webmacro
python -m venv venv
pip install -r requirements.txt

python main.py
```

## Build Executor
This step confirmed only Windows
```shell
pip install pyinstaller
pyinstaller --onefile --noconsole main.py
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
