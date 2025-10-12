"""
Configurações do aplicativo Email Sender.
"""

# Configurações SMTP
SMTP_CONFIG = {
    'gmail': {
        'server': 'smtp.gmail.com',
        'port': 465,
        'use_ssl': True
    },
    'outlook': {
        'server': 'smtp-mail.outlook.com',
        'port': 587,
        'use_ssl': False,
        'use_tls': True
    }
}

# Configurações da aplicação
APP_CONFIG = {
    'name': 'Email Sender',
    'version': '1.0',
    'organization': 'Rio Software',
    'window_title': 'Email Sender - Rio Software'
}

# Configurações de arquivo
FILE_CONFIG = {
    'supported_extensions': ['.xlsx', '.xls', '.csv'],
    'max_file_size_mb': 50,
    'encoding': 'utf-8'
}

# Configurações de email
EMAIL_CONFIG = {
    'max_recipients': 1000,
    'max_subject_length': 200,
    'max_body_length': 10000,
    'retry_attempts': 3,
    'retry_delay_seconds': 5
}

# Configurações de interface
UI_CONFIG = {
    'progress_dialog_timeout': 30000,  # 30 segundos
    'status_message_duration': 3000,   # 3 segundos
    'email_preview_limit': 5
}
