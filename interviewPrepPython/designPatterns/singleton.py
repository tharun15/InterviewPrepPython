class ApplicationState:
    instance = None

    def __init__(self):
        self.isloggedIn = False

    @staticmethod
    def getAppState():
        if not ApplicationState.instance:
            ApplicationState.instance = ApplicationState()

        return ApplicationState.instance
    

appState1 = ApplicationState.getAppState()
print(appState1.isloggedIn)

appState2 = ApplicationState.getAppState()
appState1.isloggedIn = True

print(appState1.isloggedIn)
print(appState2.isloggedIn)