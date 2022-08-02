import boto3
from aws import AWSCredentials
import os
from uuid import uuid4
from typing import Any, Dict

from custom_types import AWSUploadMetadata


class AWSClient:
    def __init__(self, credentials: AWSCredentials) -> None:
        """
        Initializes the AWSClient with AWS Credentials.

        :param credentials: AWS Credentials type
        """
        self.session = boto3.client(
            credentials.service,
            aws_access_key_id=credentials.access_key,
            aws_secret_access_key=credentials.access_secret,
            region_name=credentials.region,
        )

    def upload_file(
        self, bucket_name: str, file: bytes, metadata: AWSUploadMetadata
    ) -> Dict[str, Any]:
        """
        Upload File API is used to upload any file to the specified s3 bucket and the provided credentials

        :param bucket_name: Name of the S3 Bucket where file to be stored
        :param file: File in bytes
        :param metadata: File Upload metadata such as Content Type, Content Length and File Name
        """
        name, extension = os.path.splitext(metadata.file_name)
        key = f"{name}_{str(uuid4())}{extension}"
        print(f"saving with key: {key} ")
        put_object_response = self.session.put_object(
            Key=key,
            Bucket=bucket_name,
            Body=file,
            Metadata={
                "Content-Type": metadata.content_type,
                "Content-Length": str(metadata.content_length),
            },
        )
        return put_object_response
