import boto3
from boto3.resources.base import ServiceResource
from aws import AWSCredentials


class AWSClient:

    def __init__(self, credentials: AWSCredentials) -> None:
        """
        Initializes the AWSClient with AWS Credentials.

        :param credentials: AWS Credentials type
        """
        self.session = boto3.client(credentials.service, aws_access_key_id=credentials.access_key,
                                    aws_secret_access_key=credentials.access_secret, region_name=credentials.region)

    
    
    