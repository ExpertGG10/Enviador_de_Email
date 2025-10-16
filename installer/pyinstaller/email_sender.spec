# -*- mode: python ; coding: utf-8 -*-

import sys
import os

# Garantir que o root do projeto esteja no sys.path quando o spec for executado
# Calcular o diretório raiz do repositório de forma robusta.
# Em alguns contextos (ex: importlib.exec_module) __file__ pode não existir,
# então tentamos usar sys.argv[0] como fallback, e por fim o diretório atual.
try:
    caller_path = os.path.abspath(__file__)
except NameError:
    # __file__ não definido - usar argv[0] ou cwd
    if len(sys.argv) > 0 and sys.argv[0]:
        caller_path = os.path.abspath(sys.argv[0])
    else:
        caller_path = os.path.abspath(os.getcwd())

repo_root = os.path.abspath(os.path.join(os.path.dirname(caller_path), '..', '..'))
if repo_root not in sys.path:
    sys.path.insert(0, repo_root)

from installer.pyinstaller.build_scripts.build_email_sender import createEmailSenderApp


a, pyz, exe = createEmailSenderApp(
    name='enviador_de_email',
    script='main.py',
    uac_admin=True
)