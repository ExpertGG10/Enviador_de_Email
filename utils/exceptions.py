"""
Exceções customizadas para o sistema de email.
"""


class EmailServiceError(Exception):
    """Exceção base para erros do serviço de email."""
    pass


class EmailValidationError(EmailServiceError):
    """Exceção para erros de validação de email."""
    pass


class EmailSendError(EmailServiceError):
    """Exceção para erros de envio de email."""
    pass


class FileProcessingError(EmailServiceError):
    """Exceção para erros de processamento de arquivo."""
    pass

class RateLimitExceeded(EmailServiceError):
    """Exceção para indicar que o limite de taxa de envio de emails foi excedido."""
    pass

class DailyLimitExceeded(EmailServiceError):
    """Exceção para indicar que o limite de envios diário foi atingido"""