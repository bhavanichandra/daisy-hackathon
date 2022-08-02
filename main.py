from aws import AWSCredentials, s3_driver

from custom_types import AWSUploadMetadata


def upload_file(
    file: bytes,
    bucket_name: str,
    access_key: str,
    access_secret: str,
    region: str,
    file_name: str,
    content_type: str,
    content_length: int,
):
    """
    Upload File API is used to upload any file to the specified s3 bucket and the provided credentials

    :param file: File in bytes
    :param bucket_name: Name of the S3 Bucket where file to be stored
    :param access_key: AWS Access Key Id
    :param access_secret: AWS Access Secret
    :param region: AWS S3 Bucket Region
    :param file_name: Name of the file
    :param content_type: Content Type of the file
    :param content_length: Size of the files

    :returns: Returns a PutObjectResponse as Dictionary
    """
    credentials = AWSCredentials(
        service="s3", access_key=access_key, access_secret=access_secret, region=region
    )
    metadata = AWSUploadMetadata(
        content_length=content_length, content_type=content_type, file_name=file_name
    )
    client = s3_driver.AWSClient(credentials)
    return client.upload_file(bucket_name, file, metadata)
