# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['pasted_Version2.py'],
    pathex=[],
    binaries=[],
    datas=[('arial.ttf', '.'), ('logo_khalij.png', '.'), ('logo_main.png', '.'), ('logo_misr_kwt.png', '.'), ('sig1.png', '.'), ('sig2.png', '.'), ('sig1_ai.png', '.'), ('sig1_gulfhome.png', '.'), ('sig1_harmonykids.png', '.'), ('sig1_khalij.png', '.'), ('sig1_misrkwt.png', '.'), ('sig1_realestate.png', '.'), ('موظفي_الخليج.csv', '.'), ('موظفي_المصرية_الكويتية.csv', '.'), ('موظفي_الذكاء.csv', '.'), ('موظفي_جلف_العقارية.csv', '.'), ('موظفي_جلفهوم.csv', '.'), ('موظفي_هارمونيكيدز.csv', '.'), ('قاعدة_بيانات_العقود.csv', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='pasted_Version2',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
