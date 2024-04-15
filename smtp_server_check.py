import smtplib
import ssl
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def check_smtp_credentials(smtp_server, port, username, password):
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.ehlo()
        try:
                server.login(username, password)
                logger.info("SMTP Connection Established.")
                return True
        except (smtplib.SMTPAuthenticationError, smtplib.SMTPConnectError, smtplib.SMTPResponseException, smtplib.SMTPServerDisconnected, smtplib.SMTPException) as e:
                logger.error("SMTP Connection Issue: %s", e)
                return False
        finally:
                server.quit()

if __name__ == "__main__":
        logger.info("START")
        smtp_server = 'smtp.adani.com'
        port = 25
        username = 'noreply_tmsinfo@adani.com'
        password = 'Welc0me@2024'
        logger.info("Adani SMTP Credentials")
        logger.info("SMTP Server: %s", smtp_server)
        logger.info("Port: %s", port)
        logger.info("UserName: %s", username)
        logger.info("Password: %s", password)
        check_smtp_credentials(smtp_server, port, username, password)
        logger.info("END")




ERROR:__main__:Failed to send email: __init__() got an unexpected keyword argument 'tls'
