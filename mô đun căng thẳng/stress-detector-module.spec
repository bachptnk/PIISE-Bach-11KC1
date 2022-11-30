# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['stress-detector-module.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
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
    name='stress-detector-module',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
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
    name='stress-detector-module',
)
