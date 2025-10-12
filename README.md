# Email Sender - Rio Software

Uma aplicação moderna para envio de emails em massa com interface gráfica PySide6.

## 🚀 Funcionalidades

- **Interface Gráfica Moderna**: Interface intuitiva construída com PySide6
- **Envio em Massa**: Envie emails para múltiplos destinatários simultaneamente
- **Suporte a Anexos**: Anexe arquivos de qualquer tipo aos emails
- **Importação de Destinatários**: Importe listas de emails de arquivos Excel (.xlsx, .xls) ou CSV
- **Sistema de Logs**: Logs detalhados para debug e monitoramento
- **Validação Robusta**: Validação de emails e arquivos antes do envio
- **Configuração Segura**: Uso de senhas de aplicativo para autenticação
- **Arquitetura MVC**: Código bem estruturado e organizado

## 📋 Pré-requisitos

- Python 3.8 ou superior
- Conta Gmail com verificação em duas etapas ativada

## 🛠️ Instalação

1. Clone o repositório:
```bash
git clone https://github.com/ExpertGG10/email_sender.git
cd email_sender
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 🚀 Como Usar

1. **Execute a aplicação**:
```bash
python main.py
# ou
python gui/main_window.py
```

2. **Configure o remetente**:
   - Menu "Remetente" → Definir email e senha de aplicativo
   - Para Gmail: Ative verificação em duas etapas e gere uma senha de aplicativo

3. **Importe destinatários**:
   - Menu "Destinatários" → Selecionar arquivo Excel/CSV
   - O sistema extrairá automaticamente emails válidos

4. **Adicione anexos** (opcional):
   - Clique em "Anexo" para selecionar arquivos

5. **Envie os emails**:
   - Preencha assunto e corpo do email
   - Clique em "Enviar"

## 📁 Estrutura do Projeto

```
email_sender/
├── main.py                     # Ponto de entrada principal
├── config/                     # Configurações
│   └── settings.py
├── core/                       # Lógica de negócio
│   └── email_service.py
├── gui/                        # Interface gráfica
│   ├── main_window.py
│   └── ui_mainwindow.py
├── models/                     # Modelos de dados
│   └── email_model.py
├── controller/                 # Controladores
│   └── email_controller.py
├── dao/                        # Data Access Objects
│   └── email_dao.py
├── utils/                      # Utilitários
│   ├── validators.py
│   └── exceptions.py
└── requirements.txt            # Dependências
```

## 🔧 Configuração

### Senha de Aplicativo Gmail

1. Acesse [myaccount.google.com](https://myaccount.google.com)
2. Vá em "Segurança" → "Verificação em duas etapas"
3. Ative a verificação em duas etapas
4. Vá em "Senhas de app"
5. Gere uma nova senha para "Email Sender"
6. Use esta senha na aplicação

## 📊 Logs de Debug

A aplicação gera logs detalhados em:
- Terminal: Logs em tempo real
- Arquivo: `email_sender_debug.log`

### Exemplo de Logs:
```
[EMAIL] Iniciando envio em massa para 3 destinatarios
[ANEXO] 1 anexo(s) serão enviados com cada email
[OK] Email enviado com sucesso para: usuario@exemplo.com
```

## 🎯 Funcionalidades Detalhadas

### Importação de Destinatários
- Suporte a arquivos Excel (.xlsx, .xls) e CSV
- Extração automática de emails válidos usando regex
- Validação de formato de email
- Prevenção de duplicatas

### Sistema de Anexos
- Suporte a qualquer tipo de arquivo
- Detecção automática de tipo MIME
- Codificação base64 automática
- Múltiplos anexos por email

### Validações
- Validação de formato de email
- Validação de arquivos de destinatários
- Validação de campos obrigatórios
- Tratamento de erros robusto

## 🐛 Solução de Problemas

### Erro de Autenticação
- Verifique se a verificação em duas etapas está ativada
- Use senha de aplicativo, não a senha normal
- Verifique se o email está correto

### Problemas com Anexos
- Verifique se o arquivo existe e é acessível
- Tamanho máximo recomendado: 25MB por anexo
- Alguns provedores podem bloquear certos tipos de arquivo

### Problemas de Encoding
- A aplicação usa UTF-8 por padrão
- Logs são salvos em `email_sender_debug.log`

## 📝 Dependências

- PySide6>=6.5.0
- pandas>=1.5.0
- openpyxl>=3.0.0
- xlrd>=2.0.0

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👥 Autores

- **Rio Software** - *Desenvolvimento inicial*

## 📞 Suporte

Para suporte, abra uma issue no GitHub ou entre em contato através do email: gustavo.fc.cfc@gmail.com

---

**Email Sender** - Uma solução completa para envio de emails em massa com interface moderna e recursos avançados.
