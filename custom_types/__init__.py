from pydantic import BaseModel

class AWSUploadMetadata(BaseModel):
    """
    AWSUploadMetadata contains FileName, Content Type and Content Length
    """
    content_type: str
    file_name: str
    content_length: int
