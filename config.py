from dotenv import load_dotenv
import os
load_dotenv()

NEWS_API_KEY=os.getenv("NEWS_API_KEY")
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = os.getenv("SMTP_PORT")
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")
EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_TO = os.getenv("EMAIL_TO")
DYNAMODB_TABLE = os.getenv("DYNAMODB_TABLE")
AWS_REGION = os.getenv("DYNAMODB_TABLE")
DEFAULT_NEWS_TOPICS = os.getenv("DEFAULT_NEWS_TOPICS")