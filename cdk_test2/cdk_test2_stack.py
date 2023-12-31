from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_sns as sns
)
from constructs import Construct

class CdkTest2Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        topic = sns.Topic(self, "MyTopic")
        # example resource
        # queue = sqs.Queue(
        #     self, "CdkTest2Queue",
        #     visibility_timeout=Duration.seconds(300),
        # )
