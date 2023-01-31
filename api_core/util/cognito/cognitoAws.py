import boto3
from dotenv import load_dotenv
from api_core.util.configManager import ConfigManager
from allure import step


class AwsCognito:

    @step("Get cognito token")
    def getAwsToken(self):
        load_dotenv()

        client = boto3.client('cognito-idp', region_name=ConfigManager.getConfig('COGNITOMANGAADMIN', 'REGION'))
        response = client.initiate_auth(
            ClientId=ConfigManager.getConfig('COGNITOMANGAADMIN', 'CLIENTID'),
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME': ConfigManager.getConfig('COGNITOMANGAADMIN', 'USERNAME'),
                'PASSWORD': ConfigManager.getConfig('COGNITOMANGAADMIN', 'PASSWORD')
            },
            ClientMetadata={
                "ipAddress": "188.26.14.36",
                "country": "",
                "blackbox": ""
            }
        )
        # we might use this for something
        token = response['AuthenticationResult']['AccessToken']
        refresh_token = response['AuthenticationResult']['RefreshToken']

        return refresh_token
