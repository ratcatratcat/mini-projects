import webbrowser as wb


def webauto():
    chrome_path = '"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --profile-directory="Profile 2" %s'
    URLS = (
        "youtube.com ",
        "amazon.in",
        "flipkart.com"
    )

    for url in URLS:
        print("opening :" + url)
        wb.get(chrome_path).open(url)


webauto()
