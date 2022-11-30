# -*- mode: python ; coding: utf-8 -*-
import pkg_resources.extern.packaging
import pkg_resources.extern.appdirs
from PyInstaller.utils.hooks import collect_data_files
from PyInstaller.utils.hooks import copy_metadata


datas = []
datas += collect_data_files('torch')
datas += copy_metadata('torch')
datas += copy_metadata('tqdm')
datas += copy_metadata('regex')
datas += copy_metadata('requests')
datas += copy_metadata('packaging')
datas += copy_metadata('filelock')
datas += copy_metadata('regex')
datas += copy_metadata('numpy')
datas += copy_metadata('tokenizers')
datas += copy_metadata('importlib_metadata')







block_cipher = None


a = Analysis(
    ['VINA.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=['tensorflow', 'sklearn.utils._cython_blas', 'sklearn.neighbors.typedefs', 'sklearn.neighbors.quad_tree', 'sklearn.neighbors._typedefs', 'sklearn.utils._typedefs', 'sklearn.neighbors._partition_nodes', 'sklearn.tree', 'sklearn.tree._utils'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
for d in a.datas:
    if '_C.cp310-win_amd64.pyd' in d[0]:
        a.datas.remove(d)
        break
    if '_C.cp38-win_amd64.pyd' in d[0]:
        a.datas.remove(d)
        break
    if '_C.cp37-win_amd64.pyd' in d[0]:
        a.datas.remove(d)
        break
    if '_C.cp36-win_amd64.pyd' in d[0]:
        a.datas.remove(d)
        break
    if '_C.cp39-win_amd64.pyd' in d[0]:
        a.datas.remove(d)
        break
    if '_C.cp311-win_amd64.pyd' in d[0]:
        a.datas.remove(d)
        break


pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='VINA',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon='D:\\Python - Copy\\assets\\logo.ico',
    disable_windowed_traceback=True,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='VINA',
)
