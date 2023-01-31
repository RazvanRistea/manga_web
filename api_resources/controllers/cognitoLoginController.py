from api_core.util.configManager import ConfigManager
from api_core.microservices.restBase import ApiClient
from allure import step

adminEndpointHeaders = {
    'content-type': 'application/x-amz-json-1.1',
    'authority': str(ConfigManager.getConfig('COGNITOMANGAADMIN', 'AUTHORITY')),
    'x-amz-target': ConfigManager.getConfig('COGNITOMANGAADMIN', 'X-AMZ-TARGET'),
    'x-amz-user-agent': ConfigManager.getConfig('COGNITOMANGAADMIN', 'X-AMZ-USER-AGENT')
}


class CognitoController(ApiClient):

    @step("Get IdToken.")
    def postGetIdToken(self, payload=None):
        path = ConfigManager.getConfig('COGNITOMANGAADMIN', 'ENDPOINTTOKENID')
        response = super().post(base_address=ConfigManager.getConfig('COGNITOMANGAADMIN', 'URL'),
                                path=path, data=payload,
                                headers=adminEndpointHeaders)

        return response.json()

    @step("Get IdToken for player.")
    def postGetIdTokenPlayer(self, payload=None):
        path = ConfigManager.getConfig('COGNITOMANGAPLAYER', 'ENDPOINTTOKENID')
        response = super().post(base_address=ConfigManager.getConfig('COGNITOMANGAPLAYER', 'URL'),
                                path=path, data=payload,
                                headers=adminEndpointHeaders)

        return response.json()
