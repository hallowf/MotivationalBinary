from cx_Freeze import setup, Executable

setup(
    name = "HexadecimalChuck",
    version = "1.0",
    options = {"build_exe": {
        'packages': ["idna", "TwitterAPI", "json", "pickle", "time", "requests", "codecs", "queue"],
        'include_files': ["api_key.json", "objs.pkl"],
    }},
    executables = [Executable("tweeterBot.py",base="Win32GUI")]
    )
