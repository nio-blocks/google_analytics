GoogleAnalytics
===============
Collect data from Google Analytics.

Properties
----------
- **addl_params**: Google APIs tend to have many optional additional paramters. This property allows a configurer to add and remove optional parameters with minimal overhead. To use these properties, just call the get_addl_params method when reporting url parameters in the subclass
- **include_query**: Whether to include queries on polling requests.
- **key_config_file**: Location of private key.
- **lookback_days**: Amount of days to look back when polling.
- **metrics**: List of desired metrics.
- **polling_interval**: Time between polling requests.
- **pretty_results**: Whether or not to return readable results from Google. The raw response contains richer information but is harder to parse. By checking this, the results will be parsed and split into more readable signals. Recommended to be checked unless you need some advanced information from the Google API
- **queries**: A list of analytics IDs
- **reauth_interval**: Time in between authentications with Google
- **retry_interval**: Time between retries for authentication
- **retry_limit**: Max number of times to retry authentication

Inputs
------
- **default**: Any list of signals.

Outputs
-------
- **default**: An output signal of the queried analytics data. Details of the Google Analytics data can be found [here](https://developers.google.com/analytics/devguides/reporting/core/v3/reference#data_response).

Commands
--------
None

Dependencies
------------
- oauth2client
- pycrypto

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

GoogleAnalyticsRealtime
=======================
Collect data from Google Analytics.

Properties
----------
- **addl_params**: Google APIs tend to have many optional additional paramters. This property allows a configurer to add and remove optional parameters with minimal overhead. To use these properties, just call the get_addl_params method when reporting url parameters in the subclass
- **dimensions**: List of analytics dimensions.
- **include_query**: Whether to include queries on polling requests.
- **key_config_file**: Location of private key.
- **metrics**: List of desired metrics.
- **polling_interval**: Time between polling requests.
- **pretty_results**: Whether or not to return readable results from Google. The raw response contains richer information but is harder to parse. By checking this, the results will be parsed and split into more readable signals. Recommended to be checked unless you need some advanced information from the Google API
- **queries**: A list of analytics IDs
- **reauth_interval**: Time in between authentications with Google
- **retry_interval**: Time between retries for authentication
- **retry_limit**: Max number of times to retry authentication

Inputs
------
- **default**: Any list of signals.

Outputs
-------
- **default**: An output signal of the queried analytics data. Details of the Google Analytics data can be found [here](https://developers.google.com/analytics/devguides/reporting/core/v3/reference#data_response).

Commands
--------
None

Dependencies
------------
