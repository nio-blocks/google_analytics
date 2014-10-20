from nio.common.discovery import Discoverable, DiscoverableType
from .http_blocks.rest.rest_block import RESTPolling
from nio.metadata.properties import StringProperty


class GoogleAnalytics(GoogleOAuth):

    def get_google_scope(self):
        # Use the Google Analytics scope - as an example
        return 'https://www.googleapis.com/auth/analytics.readonly'

    def get_url_suffix(self):
        return 'analytics/v3/data/ga'

    def get_url_parameters(self):
        return {
            "ids": "ga:86273910",
            "start-date": "2014-10-06",
            "end-date": "2014-10-20",
            "metrics": "ga:hits,ga:sessions,ga:users",
            "dimensions": "ga:userType"
        }

    URL_FORMAT = ('https://www.googleapis.com/analytics/v3/data/ga?'
                  'ids={PROP_IDS}&'
                  'start-date={START_DATE}&'
                  'end-date={END_DATE}&'
                  'metrics={METRICS}&'
                  'key={API_KEY}')

    dev_key = StringProperty(title="API Key", default="[[GOOGLE_API_KEY]]")

    def __init__(self):
        super().__init__()

    def _prepare_url(self, paging=False):
        url = self.URL_FORMAT.format(
            API_KEY=self.dev_key,
            PROP_IDS="ga:86273910",
            START_DATE="2014-09-04",
            END_DATE="2014-09-18",
            METRICS="ga:hits"
        )

        self._url = url
        return {"Content-Type": "application/json"}

    def _process_response(self, resp):
        status = resp.status_code
        body = resp.json()
        print(body)
