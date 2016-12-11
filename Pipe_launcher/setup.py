import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

options = {
    'build_exe': {
        'includes': 'atexit'
    }
}

executables = [
    Executable('application.py', base=base)
]

setup(name='App Launcher',
      version='0.1',
      description='Lanceur d\'application',
      options=options,
      executables=executables
      )
