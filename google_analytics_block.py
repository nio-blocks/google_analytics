from nio.properties import IntProperty, VersionProperty

from .google_analytics_base import GoogleAnalyticsBase


class GoogleAnalytics(GoogleAnalyticsBase):

    lookback_days = IntProperty(title="Lookback Days (inclusive)", default=0)
    version = VersionProperty("1.0.0")

    def get_url_suffix(self):
        return 'analytics/v3/data/ga'

    def get_url_parameters(self):
        params = super().get_url_parameters()

        params["start-date"] = "{0}daysAgo".format(self.lookback_days())
        params["end-date"] = "today"
        params["dimensions"] = "ga:userType"

        return params
