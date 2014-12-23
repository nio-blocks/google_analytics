from nio.common.discovery import Discoverable, DiscoverableType
from nio.metadata.properties import ListProperty
from .google_analytics_base import GoogleAnalyticsBase


@Discoverable(DiscoverableType.block)
class GoogleAnalyticsRealtime(GoogleAnalyticsBase):

    # Overridden for default property name
    metrics = ListProperty(
        str, title="Analytics Metrics", default=["rt:activeUsers"])
    dimensions = ListProperty(
        str, title="Analytics Dimensions", default=["rt:city"])

    def get_url_suffix(self):
        """ Required override for GoogleOAuth Block """
        return 'analytics/v3/data/realtime'

    def get_url_parameters(self):
        params = super().get_url_parameters()

        params["dimensions"] = ",".join(self.dimensions)

        return params