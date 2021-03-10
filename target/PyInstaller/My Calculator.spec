# -*- mode: python -*-

block_cipher = None


a = Analysis(['C:\\Users\\Manoj\\Documents\\GitHub\\PythonCalc\\src\\main\\python\\main.py'],
             pathex=['C:\\Users\\Manoj\\Documents\\GitHub\\PythonCalc\\target\\PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['c:\\users\\manoj\\miniconda3\\envs\\py36\\lib\\site-packages\\fbs\\freeze\\hooks'],
             runtime_hooks=['C:\\Users\\Manoj\\Documents\\GitHub\\PythonCalc\\target\\PyInstaller\\fbs_pyinstaller_hook.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='My Calculator',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=False , icon='C:\\Users\\Manoj\\Documents\\GitHub\\PythonCalc\\src\\main\\icons\\Icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='My Calculator')
