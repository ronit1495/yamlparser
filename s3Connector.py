from distutils.command import config
from distutils.log import error, info
import boto3,logging
from botocore.config import Config

logger=logging.getLogger() 

# Backoff reties impementation for boto3's S3 calls
config = Config(
   retries = {
    #5 attempts is 5x2=10minutes
      'max_attempts': 5,
      'mode': 'standard'
   }
)

# Use boto3 for Amazon S3 access
s3 = boto3.client("s3", config=config)

# S3 file downloader, not asked but created for future use
def s3Downloader():
    logger.info("Connecting to S3, make sure you have used aws configure to allow access to buckets.")
    try:
        s3.download_file(
            Bucket="config-uploader", 
            Key="result.json", 
            Filename="downloaded_config.json"
        )    
        logger.info("File downloaded successfully.")
    except:
        logger.error("File download failed.")

# S3 file uploader
def s3Uploader():
    logger.info("Connecting to S3, make sure you have used aws configure to allow access to buckets.")
    try:
        s3.upload_file(
            Filename="config.json",
            Bucket="config-uploader",
            Key="result.json",
        )
        logger.info("File uploaded successfully.")
    except:
        logger.error("File upload failed.")