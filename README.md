# DarkRagweed
Ikariam hacking framework + script repository

## Source
The /src/ folder contains the Python 3 framework to interact with the game. It relies on the classic "API" that is used in classic PC browsers, using mainly POST requests.

## Scripts
Any script run using a code injection technique will be executed on the scope of the user that executes the code.

The /scripts/ folder holds several scripts specially designed and crafted to be injected into the game's code using Cross Site Scripting (xss) vulnerabilities. These scripts ought to behave differently if they target the classic PC Browser game or the Android/iOS app, which relies on webView.

It must be known that scripts running on classic PC browsers **must** use the classic URL request API and scripts running on WebView **must** use the corresponding mobile API urls. This is due to session cookies, which can only be used with the corresponding API that created them. 

Code to detect whether the script is running in PC or WebView is provided on most scripts.

Available Scripts:
- [x] debugAlert

```Detects whether the script is being executed in WebView or PC, reads accordingly the "oneclick" value, and shows it in an alert```

- [ ] sendMessage

```When executed, sends a private message to the target userID```

- [ ] sendResource

```When executed, sends the indicated amount of resources (wood,wine,crystal,sulfur or rock) to the target userID```


## Debugging Scripts
A script that is not working can be debuged with very trivial software
* For scripts intended to run on PC, use the "Inspect Element" of your favorite browser. With the "Network" tab you can track the HTML requests your script does, with the console you can check manually if Javascript objects/variables exists, and with the "Element" tab the HTML code can be checked for code injection problems.

* For scripts intented to run on WebView, you can use an Android Phone + Chromium/Chrome WebView debugger. You'll need an Android phone with the app installed and USB Debugging activated. Type ```chrome://inspect/#devices``` on the browser's URL tab, allow debugging from your PC, start the app and select the WebView from the target list. You'll get access to the same set of utils that you have on PC with "Inspect Element".
