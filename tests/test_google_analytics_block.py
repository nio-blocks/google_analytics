from nio.testing.block_test_case import NIOBlockTestCase

from ..google_analytics_block import GoogleAnalytics
from ..google_analytics_realtime_block import GoogleAnalyticsRealtime
from ..google_analytics_base import GoogleAnalyticsBase


class TestGoogleAnalyticsBase(NIOBlockTestCase):

    def test_configure_start_stop(self):
        blk = GoogleAnalyticsBase()
        self.configure_block(blk, {})
        blk.start()
        blk.stop()


class TestGoogleAnalytics(NIOBlockTestCase):

    def test_configure_start_stop(self):
        blk = GoogleAnalytics()
        self.configure_block(blk, {})
        blk.start()
        blk.stop()


class TestGoogleAnalyticsRealtime(NIOBlockTestCase):

    def test_configure_start_stop(self):
        blk = GoogleAnalyticsRealtime()
        self.configure_block(blk, {})
        blk.start()
        blk.stop()
