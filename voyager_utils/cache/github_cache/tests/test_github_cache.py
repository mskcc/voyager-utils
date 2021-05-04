from django.test import TestCase
from django.test.utils import override_settings
from voyager_utils.cache.github_cache.github_cache import GithubCache


class TestStringMethods(TestCase):

    def test_extract_dirname_from_github_link(self):
        github = 'https://github.com/mskcc/argos-cwl'
        res = GithubCache._extract_dirname_from_github_link(github)
        self.assertEqual(res, 'argos-cwl')

    @override_settings(APP_CACHE='/app/cache')
    def test_generate_directory_name(self):
        github = 'https://github.com/mskcc/argos-cwl'
        res = GithubCache._generate_directory_name(github, '1.1.2')
        self.assertEqual(res, '/app/cache/mskcc_argos-cwl/1.1.2')
