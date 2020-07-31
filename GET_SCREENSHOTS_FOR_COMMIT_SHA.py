import requests as r


def make_table(sha, languages):
    table = '|'
    for language in languages:
        table += f' {language} |'
    table += '\n|' + '-|' * len(languages)
    for row in [
        'HomeScreenEmptyScreenshot',
        'HomeScreenDarkEmptyScreenshot',
        'ContactsActivityScreenshot',
        'PillsActivityScreenshot',
        'AlarmsActivityFullScreenshot',
        'VideoTutorialsActivityScreenshot',
        'SettingsActivityScreenshot',
        'RecentCallsActivityScreenshot',
        'DialerActivityScreenshot',
        'NotificationsActivityEmptyScreenshot',
        'NotificationsActivityEmptyScreenshot',
        'AlarmsActivityEmptyScreenshot',
        'PillsEmptyActivityScreenshot'
    ]:
        table += '\n|'
        for language in languages:
            table += f' ![img](https://github.com/UriahShaulMandel/BaldPhoneScreenshots/blob/{sha}/screenshots/screenshots/{row}_{language}.png?raw=true)            |'
    return table


def get_commit_sha(baldphone_commit_sha):
    commits = r.get("https://api.github.com/repos/UriahShaulMandel/BaldPhoneCompanion/commits").json()
    relevant_commits = [c for c in commits if c["commit"]["message"] == baldphone_commit_sha]
    chosen_commit = max(relevant_commits, key=lambda x: x["commit"]['committer']["date"])
    chosen_commit_sha = chosen_commit["sha"]
    return chosen_commit_sha


sha = get_commit_sha('4423b0ab5189db39a2f9a1924cdcdf55d2f61458')
print(
    f"Paste the following markdown code:\n{make_table(sha, ['en', 'iw', 'fr', 'de', 'it', 'es', 'cs', 'sl', 'de', 'pt', 'pt-rBR', 'pl'])}\n\nIn the following link: https://dillinger.io/"
)
