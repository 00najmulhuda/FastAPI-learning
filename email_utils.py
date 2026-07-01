from fastapi_mail import FastMail, MessageSchema
from email_config import conf

async def send_email(email: str):
    message = MessageSchema(
        subject = "Welcome to Lab",
        recipients = [email],
        body = """
        <h1> Welcome to Lab </h1>
        <p> Thank you for registering. </p>
        <p> We're excited to have you with us. </p>
        """,
        subtype = "html"
    )
    fm = FastMail(conf)
    await fm.send_message(message)