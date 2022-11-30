# django-debug-vscode-docker-devcontainer
Scaffolding to set up debugging for Django in Docker with VS Code using Dev Containers

# Setup
- Install [VS Code](https://code.visualstudio.com/) and the [Remote Development](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack) Extension Pack.

- Clone this repository, then open this folder in VS Code (_File_ > _Open Folder_).

- You should see a dialog box pop up that says "Reopen in Container", say yes.
<img src="yourapp/static/reopen_in_container.png">

- Python [Dev Container](https://code.visualstudio.com/docs/containers/quickstart-python) startup is still wonky. You might have to close out and "Reopen in Container" a second time if the post-create commands and Python extensions don't load up immediately.

- Click the "Debug" menu icon on the left pane, then click the "Play" button to run the debugger. This screenshot shows the various things you should do **<span style="color: #669C35;">in green</span>**, which are numbered.
<img src="yourapp/static/debug_experience.png">

- The web app can be accessed at [127.0.0.1:5111](http://127.0.0.1:5111) or any hostname you've set up in `/etc/hosts` to test breakpoints.
