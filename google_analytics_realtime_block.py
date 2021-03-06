from nio.properties import ListProperty, VersionProperty
from nio.types.string import StringType

from .google_analytics_base import GoogleAnalyticsBase


class GoogleAnalyticsRealtime(GoogleAnalyticsBase):

    # Overridden for default property name
    metrics = ListProperty(
        StringType, title="Analytics Metrics", default=["rt:activeUsers"])
    dimensions = ListProperty(
        StringType, title="Analytics Dimensions", default=["rt:city"])
    version = VersionProperty("1.0.1")

    def get_url_suffix(self):
        """ Required override for GoogleOAuth Block """

        return 'analytics/v3/data/realtime'

    def get_url_parameters(self):
        params = super().get_url_parameters()

        params["dimensions"] = ",".join(self.dimensions())

        return params
