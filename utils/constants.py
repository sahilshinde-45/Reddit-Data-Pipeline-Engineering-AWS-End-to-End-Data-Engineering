import configparser
import os

# Load config file
parser = configparser.ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), '../config/config.conf')
parser.read(config_path)

# Use environment variables as a fallback for sensitive data
SECRET = os.getenv("REDDIT_SECRET_KEY", parser.get("api_keys", "reddit_secret_key", fallback=""))
CLIENT_ID = os.getenv("REDDIT_CLIENT_ID", parser.get("api_keys", "reddit_client_id", fallback=""))

# Database Credentials
DATABASE_HOST = parser.get("database", "database_host", fallback="localhost")
DATABASE_NAME = parser.get("database", "database_name", fallback="airflow_reddit")
DATABASE_PORT = parser.get("database", "database_port", fallback="5432")
DATABASE_USER = parser.get("database", "database_username", fallback="postgres")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", parser.get("database", "database_password", fallback="postgres"))

# AWS Credentials (fallback to environment variables)
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID", parser.get("aws", "aws_access_key_id", fallback=""))
AWS_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY", parser.get("aws", "aws_secret_access_key", fallback=""))
AWS_REGION = parser.get("aws", "aws_region", fallback="us-east-1")
AWS_BUCKET_NAME = parser.get("aws", "aws_bucket_name", fallback="")

# File Paths
INPUT_PATH = parser.get("file_paths", "input_path", fallback="/opt/airflow/data/input")
OUTPUT_PATH = parser.get("file_paths", "output_path", fallback="/opt/airflow/data/output")

# Post Fields
POST_FIELDS = (
    "id",
    "title",
    "score",
    "num_comments",
    "author",
    "created_utc",
    "url",
    "over_18",
    "edited",
    "spoiler",
    "stickied",
)

# Debugging (Optional)
print(f"Reddit Client ID: {CLIENT_ID}")
print(f"Database: {DATABASE_NAME} on {DATABASE_HOST}:{DATABASE_PORT}")
