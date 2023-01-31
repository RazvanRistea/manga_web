from api_core.util.configManager import ConfigManager
from api_core.microservices.restBase import ApiClient
from allure import step


adminEndpointHeaders = {
    'Accept': '*/*',
    'authority': ConfigManager.getConfig('MANGAADMINDEV', 'GETUSERSAUTHORITY'),
}

# limit=20&position=0&search=&type=FULL ask question why seach is empty
params = {'limit': 20, 'position': 0, 'type': 'FULL'}


class AdminController(ApiClient):

    @step("Get users.")
    def getUsers(self, params=None, idToken=None):
        path = ConfigManager.getConfig('MANGAADMINDEV', 'ENDPOINTGETUSERS')
        adminEndpointHeaders['authorization'] = idToken
        response = super().get(base_address=ConfigManager.getConfig('MANGAADMINDEV', 'URLGETUSERS'),
                               path=path, params=params,
                               headers=adminEndpointHeaders)

        return response.json()
