# Arquivo: installer/powershell/compilar_cliente.ps1
# Compila o executável do cliente e cria o instalador.

Set-Location -Path "$PSScriptRoot/../../"

pyinstaller ./installer/pyinstaller/email_sender.spec
iscc.exe ./installer/inno_setup/email_sender.iss

Write-Host "Instalador do Enviador de Email criado!"