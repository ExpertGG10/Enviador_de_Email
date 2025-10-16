#define Versao "1.0.0"

[Setup]
AppName={#NomeApp}
AppPublisher={#NomePublisher}
AppVersion={#Versao}
DefaultDirName={pf}\{#NomePublisher} {#NomeApp}
DefaultGroupName={#NomeApp}
UninstallDisplayIcon={app}\{#NomeExe}.exe
OutputDir=..\..\releases\v{#Versao}
OutputBaseFilename=Instalador_{#NomeInstalador}_v{#Versao}
Compression=lzma
SolidCompression=yes

[Languages]
Name: "portuguesebr"; MessagesFile: "compiler:Languages\BrazilianPortuguese.isl"

[Files]
Source: "..\..\dist\{#NomeExe}.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\static\images\icon.ico"; DestDir: "{app}"

[Tasks]
Name: "desktopicon"; Description: "Criar ícone na área de trabalho"; Flags: unchecked

[Icons]
Name: "{group}\{#NomeApp}"; Filename: "{app}\{#NomeExe}.exe"; IconFilename: "{app}\icon.ico"
Name: "{userdesktop}\{#NomeApp}"; Filename: "{app}\{#NomeExe}.exe"; IconFilename: "{app}\icon.ico"; Tasks: desktopicon
