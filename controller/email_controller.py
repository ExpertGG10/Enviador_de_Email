import os
import smtplib
import mimetypes
import logging

from models.email_model import EmailModel
from models.sender_model import SenderModel

logger = logging.getLogger(__name__)

class EmailController:
    """
    Controller that handles email sending.

    Args:
        app_password: application-specific password for SMTP auth
        sender_address: sender email address
    """
    def __init__(self, sender: SenderModel):
        logger.info(f"[INIT] Initializing EmailController for: {sender.address}")

        self.sender = sender
        
        logger.debug("[SMTP] Connecting to SMTP server...")
        self.smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        logger.debug("[OK] SMTP connection established")

        logger.debug("[AUTH] Logging in to SMTP server...")
        self.smtp_server.login(self.sender.address, self.sender.app_password)
        logger.info("[OK] SMTP login successful")

    def send_mass_emails(self, recipient_list: list[str], subject: str, body: str, attachments: list | None = None, progress = None) -> dict:
        """
        Send emails in bulk to a list of recipients.
        
        Args:
            recipient_list: List of recipient email addresses
            subject: Subject of the email
            body: Body content of the email (HTML format)
            attachments: List of file paths to attach to the email
            progress: Optional callable to report progress (current, total)

        Returns:
            A dictionary with counts of total, successful, and failed emails.
        """
        logger.info(f"[EMAIL] Starting bulk send to {len(recipient_list)} recipients")
        logger.debug(f"[EMAIL] Subject: {subject}")
        if attachments:
            logger.info(f"[ATTACHMENT] {len(attachments)} attachment(s) will be sent with each email")

        success_count = 0
        failed_count = 0

        try:
            for i, recipient in enumerate(recipient_list, 1):
                logger.debug(f"[EMAIL] Sending email {i}/{len(recipient_list)} to: {recipient}")
                try:
                    email = EmailModel(self.sender.address, recipient, subject, body, attachments)
                    result = self.send_email(email)
                    if result:
                        logger.debug(f"[OK] Email {i} sent successfully")
                        success_count += 1
                except Exception as e:
                    failed_count += 1
                    logger.error(f"[ERROR] Error sending email to {recipient}: {e}")

                if progress:
                    progress.emit(i)

            logger.info("[OK] All emails were sent successfully")
            logger.debug(f"[EMAIL] Bulk send results: {success_count} succeeded, {failed_count} failed")
            
            return {
                'total': len(recipient_list),
                'success': success_count,
                'failed': failed_count
            }
        except smtplib.SMTPAuthenticationError:
            logger.error("[ERROR] SMTP authentication error")
            
            raise ValueError("Authentication error! Check the email and app password.")
        except Exception as e:
            logger.error(f"[ERROR] Bulk send error: {e}")
            raise Exception(f"An error occurred: {e}")

    def send_email(self, email: EmailModel) -> bool:
        """
        Send a single email to a recipient.

        Args:
            email: EmailModel instance containing email details

        Returns:
            True if the email was sent successfully, False otherwise.
        """
        
        if email.attachments:
            logger.debug(f"[ATTACHMENT] {len(email.attachments)} attachment(s) will be sent")

        try:
            msg = email.create_message()

            try:
                existing_attachments = []
                if msg.is_multipart():
                    for part in msg.iter_attachments():
                        existing_attachments.append(part)

                msg.clear_content()
                msg.set_content(email.body, subtype="html", charset="utf-8")

                for part in existing_attachments:
                    data = part.get_payload(decode=True)
                    ctype = part.get_content_type()
                    maintype, subtype = ctype.split("/", 1)
                    filename = part.get_filename()
                    msg.add_attachment(data, maintype=maintype, subtype=subtype, filename=filename)

                if not existing_attachments and email.attachments:
                    for path in email.attachments:
                        if not path:
                            continue
                        ctype, encoding = mimetypes.guess_type(path)
                        if ctype is None or encoding is not None:
                            ctype = "application/octet-stream"
                        maintype, subtype = ctype.split("/", 1)
                        with open(path, "rb") as f:
                            data = f.read()
                        msg.add_attachment(
                            data,
                            maintype=maintype,
                            subtype=subtype,
                            filename=os.path.basename(path),
                        )

                logger.debug("[EMAIL] Body forced to HTML and attachments consolidated")
            except Exception as adjust_err:
                logger.warning(f"[WARN] Could not adjust body to HTML: {adjust_err}. Sending as created by model.")

            logger.debug(f"[EMAIL] Sending message to: {email.recipient_address}")
            self.smtp_server.send_message(msg)
            logger.debug(f"[OK] Email sent successfully to: {email.recipient_address}")

            return True
        except smtplib.SMTPAuthenticationError:
            logger.error(f"[ERROR] Authentication error when sending to: {email.recipient_address}")
            raise ValueError("Authentication error! Check the email and app password.")
        except Exception as e:
            logger.error(f"[ERROR] Error sending email to {email.recipient_address}: {e}")
            raise Exception(f"An error occurred: {e}")

    def __del__(self):
        logger.debug("[SMTP] Closing SMTP connection...")
        try:
            self.smtp_server.quit()
        except Exception:
            pass
        logger.debug("[OK] SMTP connection closed")