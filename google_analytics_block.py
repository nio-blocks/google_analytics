from nio.common.discovery import Discoverable, DiscoverableType
from nio.metadata.properties import ListProperty, IntProperty
from .google_oauth_base.google_oauth_block import GoogleOAuth


@Discoverable(DiscoverableType.block)
class GoogleAnalytics(GoogleOAuth):

    analytics_ids = ListProperty(
        str, title="Analytics IDs", default=["ga:########"])
    metrics = ListProperty(
        str, title="Analytics Metrics", default=["ga:hits"])
    lookback_days = IntProperty(title="Lookback Days (inclusive)", default=0)

    def get_google_scope(self):
        """ Required override for GoogleOAuth Block """
        return 'https://www.googleapis.com/auth/analytics.readonly'

    def get_url_suffix(self):
        """ Required override for GoogleOAuth Block """
        return 'analytics/v3/data/ga'

    def get_url_parameters(self):
        """ Required override for GoogleOAuth Block """
        params = {
            "ids": ",".join(self.analytics_ids),
            "start-date": "{0}daysAgo".format(self.lookback_days),
            "start-date": self._get_start_date(),
            "end-date": "today",
            "metrics": ",".join(self.metrics),
            "dimensions": "ga:userType"
        }

        # Include any additional parameters from the parent block
        params.update(self.get_addl_params())

        self._logger.debug("Accessing Analytics API using {0}".format(params))
        return params
