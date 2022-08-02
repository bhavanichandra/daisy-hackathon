from curses import meta
from io import TextIOWrapper
from aws import AWSCredentials, s3_driver
import os
from dotenv import load_dotenv
from uuid import uuid4

import custom_types

load_dotenv()


def upload_file(file: bytes, bucket_name: str, credentials: AWSCredentials, metadata: custom_types.AWSUploadMetadata):
    """
    Upload File API is used to upload any file to the specified s3 bucket and the provided credentials

    :param file: File in bytes
    :param bucket_name: Name of the S3 Bucket where file to be stored
    :param credentials: AWS Credentials
    :param metadata: File Upload metadata such as Content Type, Content Length and File Name

    """
    client = s3_driver.AWSClient(credentials)
    name, extension = os.path.splitext(metadata.file_name)
    key = f"{name}_{str(uuid4())}{extension}"
    print(f"saving with key: {key} ")
    put_object_response = client.session.put_object(
        Key=key,
        Bucket=bucket_name,
        Body=file,
        Metadata={
            'Content-Type': metadata.content_type,
            'Content-Length': str(metadata.content_length)
        }
    )
    return put_object_response



