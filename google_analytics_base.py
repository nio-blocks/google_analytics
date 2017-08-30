from urllib.request import unquote

from nio.properties import ListProperty
from nio.types.string import StringType
from nio.util.discovery import not_discoverable

from .google_oauth_base.google_oauth_block import GoogleOAuth


@not_discoverable
class GoogleAnalyticsBase(GoogleOAuth):

    queries = ListProperty(StringType, title="Analytics IDs",
                           default=["ga:########"])
    metrics = ListProperty(StringType, title="Analytics Metrics",
                           default=["ga:hits"])

    def get_google_scope(self):
        """ Required override for GoogleOAuth Block """
        return 'https://www.googleapis.com/auth/analytics.readonly'

    def get_url_suffix(self):
        """ Required override for GoogleOAuth Block """

        # To be implemented in subclass
        return NotImplemented

    def get_url_parameters(self):
        """ Required override for GoogleOAuth Block """

        params = {
            "ids": unquote(self.current_query),
            "metrics": ",".join(self.metrics())
        }

        # Include any additional parameters from the parent block
        params.update(self.get_addl_params())

        self.logger.debug("Accessing Analytics API using {0}".format(params))
        return params
