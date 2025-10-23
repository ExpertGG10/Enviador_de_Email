import sys
import os

caminhoBase = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.insert(0, caminhoBase)

from utils.files import join_paths
from PyInstaller.building.build_main import Analysis, PYZ, EXE

dadosPadrao = [
    (join_paths(caminhoBase, 'static'), 'static')
]
pathexPadrao = ['.']
iconePadrao = [join_paths(caminhoBase, 'static\\images\\icon.ico')]

def criarAplicacao(
    *,
    name: str,
    script: str,
    console: bool,
    icon=iconePadrao,
    datas=dadosPadrao,
    pathex=pathexPadrao,
    optimize: int = 0,
    workpath: str | None = None,
    distpath: str | None = None,
    debug: bool = False,
    strip: bool = False,
    upx: bool = True,
    upx_exclude: list[str] | None = None,
    hiddenimports: list[str] | None = None,
    hookspath: list[str] | None = None,
    hooksconfig: dict | None = None,
    runtime_hooks: list[str] | None = None,
    excludes: list[str] | None = None,
    noarchive: bool = False,
    bootloader_ignore_signals: bool = False,
    disable_windowed_traceback: bool = False,
    argv_emulation: bool = False,
    runtime_tmpdir=None,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    uac_admin: bool = False,
):
    """
    Cria uma aplicação empacotável usando PyInstaller.

    Args:
        name (str): O nome do executável.
        script (str): O caminho para o script de entrada.
        console (bool): Se a aplicação deve ser de console (True) ou sem console (False).
        ... (demais argumentos padrão do PyInstaller)
    """
    analysis_kwargs = dict(
        pathex=pathex,
        binaries=[],
        datas=datas,
        hiddenimports=hiddenimports or [],
        hookspath=hookspath or [],
        hooksconfig=hooksconfig or {},
        runtime_hooks=runtime_hooks or [],
        excludes=excludes or [],
        noarchive=noarchive,
        optimize=optimize,
    )
    if workpath is not None:
        analysis_kwargs["workpath"] = workpath

    a = Analysis([join_paths(caminhoBase, script)], **analysis_kwargs)
    pyz = PYZ(a.pure)

    exe_kwargs = dict(
        name=name,
        debug=debug,
        bootloader_ignore_signals=bootloader_ignore_signals,
        strip=strip,
        upx=upx,
        upx_exclude=upx_exclude or [],
        runtime_tmpdir=runtime_tmpdir,
        console=console,
        disable_windowed_traceback=disable_windowed_traceback,
        argv_emulation=argv_emulation,
        target_arch=target_arch,
        codesign_identity=codesign_identity,
        entitlements_file=entitlements_file,
        icon=icon,
        uac_admin=uac_admin,
    )
    if distpath is not None:
        exe_kwargs["distpath"] = distpath

    exe = EXE(
        pyz,
        a.scripts,
        a.binaries,
        a.datas,
        [],
        **exe_kwargs
    )

    return a, pyz, exe