from api_core.util.configManager import ConfigManager
from api_core.microservices.restBase import ApiClient
from allure import step

registrationHeaders = {
    'content-type': 'application/json;charset=UTF-8',
    'sitecontext': "{\"siteId\": \"3\"}"
}

getBalanceHeaders = {
    'Accept': '*/*'
}

paripalyContextHeaders = {
    'Accept': '*/*'
}


class PlayerController(ApiClient):

    @step("First step register new user.")
    def registerStepOne(self, payload=None):
        path = ConfigManager.getConfig('MANGADEV', 'REGISTRATION-API')

        response = super().post(base_address=ConfigManager.getConfig('MANGADEV', 'PLAYER-EXECUTE-URL'),
                                path=path, data=payload,
                                headers=registrationHeaders)

        return response.json()

    @step("Second step register new user.")
    def registerStepTwo(self, payload=None):
        path = ConfigManager.getConfig('MANGADEV', 'REGISTRATION-API')

        response = super().put(base_address=ConfigManager.getConfig('MANGADEV', 'PLAYER-EXECUTE-URL'),
                               path=path, data=payload,
                               headers=registrationHeaders)

        return response.json()

    @step("Get user balance")
    def getBalance(self, idToken=None):
        getBalanceHeaders['authorization'] = idToken
        path = '/'
        response = super().get(base_address=ConfigManager.getConfig('MANGADEV', 'PLAYER-EXECUTE-WALLET-URL'),
                               path=path,
                               headers=getBalanceHeaders)

        return response.json()

    @step("Request SMS")
    def requestSMS(self, payload=None):
        path = ConfigManager.getConfig('MANGADEV', 'REGISTRATION-API') + ConfigManager.getConfig('MANGADEV',
                                                                                                'SMS-REQUEST-API')

        response = super().post(base_address=ConfigManager.getConfig('MANGADEV', 'PLAYER-EXECUTE-URL'),
                                path=path, data=payload,
                                headers=registrationHeaders)

        return response

    @step("Send SMS confirmation")
    def verifySMS(self, payload=None):
        path = ConfigManager.getConfig('MANGADEV', 'REGISTRATION-API') + ConfigManager.getConfig('MANGADEV',
                                                                                                'SMS-VERIFICATION-API')

        response = super().post(base_address=ConfigManager.getConfig('MANGADEV', 'PLAYER-EXECUTE-URL'),
                                path=path, data=payload,
                                headers=registrationHeaders)

        return response

    @step("Get Pariplay Token")
    def requestPariplayToken(self, payload=None, idToken=None):
        path = ConfigManager.getConfig('MANGADEV', 'ENDPOINT-PAIRPLAY-REAL')
        paripalyContextHeaders['authorization'] = "Bearer " + idToken

        response = super().post(base_address=ConfigManager.getConfig('MANGADEV', 'PAIRPLAY-GAMES-AUTHORITY'),
                                path=path, data=payload,
                                headers=paripalyContextHeaders)

        return response

    @step("Auth Pariplay")
    def authPariplay(self, payload=None):
        path = ConfigManager.getConfig('MANGADEV', 'PAIRPLAY-ENDPOINT-AUTH')

        response = super().post(base_address=ConfigManager.getConfig('MANGADEV', 'PAIRPLAY-URL-STAGING'),
                                path=path, data=payload,
                                headers=paripalyContextHeaders)

        return response

    @step("Pariplay Credit")
    def pariplayCredit(self, payload=None):
        path = ConfigManager.getConfig('MANGADEV', 'PAIRPLAY-ENDPOINT-CREDIT')

        response = super().post(base_address=ConfigManager.getConfig('MANGADEV', 'PAIRPLAY-URL-STAGING'),
                                path=path, data=payload,
                                headers=paripalyContextHeaders)

        return response

    @step("Pariplay Debit")
    def pariplayDebit(self, payload=None):
        path = ConfigManager.getConfig('MANGADEV', 'PAIRPLAY-ENDPOINT-DEBIT')

        response = super().post(base_address=ConfigManager.getConfig('MANGADEV', 'PAIRPLAY-URL-STAGING'),
                                path=path, data=payload,
                                headers=paripalyContextHeaders)

        return response
