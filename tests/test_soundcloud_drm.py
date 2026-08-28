import unittest

from yt_dlp.extractor.soundcloud import SoundcloudBaseIE

from yt_dlp_plugins.extractor.soundcloud_drm import SoundCloudDRMIE


class SoundCloudDRMAuthenticationTests(unittest.TestCase):
    def test_authenticated_headers_are_forwarded_to_drm_requests(self):
        self.assertTrue(issubclass(SoundCloudDRMIE, SoundcloudBaseIE))

        extractor = object.__new__(SoundCloudDRMIE)
        extractor._HEADERS = {'Authorization': 'OAuth test-token'}

        headers = extractor._sc_headers()

        self.assertEqual(headers['Authorization'], 'OAuth test-token')
        self.assertEqual(headers['Origin'], 'https://soundcloud.com')


if __name__ == '__main__':
    unittest.main()
