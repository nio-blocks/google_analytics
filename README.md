GoogleAnalytics
================

Collect data from Google Analytics

## Getting Started

This will walk you through how to get started using the Google Analytics APIs.

1. Go to the [Google Developers Console](https://console.developers.google.com/). Select your project (or create one!)
2. Go to **APIs & Auth** > **APIs** and make sure that the Analytics API is active.
3. Go to **APIs & Auth** > **Credentials**
4. Click on **Create new Client ID**
5. Select **Service Account** and wait for the key pair to be created.
6. Once created, click **Generate new JSON Key** and download and save the JSON file. 
7. Place this file in one of the following locations, and note the filename:
  - Next to the block file
  - In the project directory
8. In the block config, put the location of the file in the **Private Key Config File** config.
9. Go to the Google Analytics Administration Page, then click **User Management**
10. Copy the email address from the Developer Console and grant it permissions to the Google Analytics account.

### Getting your Google Analytics ID

This is not the same thing as your tracking ID. Instead, it is an ID tied to a view, and this is the best way I can seem to find it:

1. Go to the [Google Dev Query Explorer](https://ga-dev-tools.appspot.com/explorer/)
2. Authorize your account (if it isn't already)
3. Select your **Account**, **Property**, and **View**
4. The relevant ID will appear under **ids** (it should look like `ga:########`).
