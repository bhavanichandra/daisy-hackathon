from pydantic import BaseModel


class AWSCredentials(BaseModel):
    """
    AWS Credentials class with constructor Service, Access Key, Access Secret and Region
    """
    service: str
    access_key: str
    access_secret: str
    region: str

