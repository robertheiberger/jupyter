import boto3
from botocore.utils import InstanceMetadataFetcher
from botocore.credentials import InstanceMetadataProvider
provider = InstanceMetadataProvider(iam_role_fetcher=InstanceMetadataFetcher(timeout=1000, num_attempts=2))
creds = provider.load()

session = boto3.Session(
    aws_access_key_id=creds.access_key,
    aws_secret_access_key=creds.secret_key,
    aws_session_token=creds.token
)

s3 = session.client('s3')
s3.list_buckets()
