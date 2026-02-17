import os
import sys
import unittest


ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SCRIPTS_DIR = os.path.join(ROOT_DIR, "scripts")
if SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, SCRIPTS_DIR)

import repo_helpers  # noqa: E402


class RepoHelpersTests(unittest.TestCase):
    def test_normalize_repo_slug_accepts_slug_ssh_and_https(self) -> None:
        self.assertEqual(repo_helpers.normalize_repo_slug("owner/repo"), "owner/repo")
        self.assertEqual(repo_helpers.normalize_repo_slug("git@github.com:owner/repo.git"), "owner/repo")
        self.assertEqual(repo_helpers.normalize_repo_slug("https://github.com/owner/repo"), "owner/repo")

    def test_normalize_repo_slug_rejects_invalid_values(self) -> None:
        self.assertIsNone(repo_helpers.normalize_repo_slug(""))
        self.assertIsNone(repo_helpers.normalize_repo_slug("https://example.com/owner/repo"))
        self.assertIsNone(repo_helpers.normalize_repo_slug("owner"))

    def test_pages_url_from_slug_handles_user_pages_repo(self) -> None:
        self.assertEqual(repo_helpers.pages_url_from_slug("octocat/octocat.github.io"), "https://octocat.github.io/")
        self.assertEqual(repo_helpers.pages_url_from_slug("octocat/my-dashboard"), "https://octocat.github.io/my-dashboard/")

    def test_normalize_dashboard_url_accepts_host_and_keeps_query(self) -> None:
        self.assertEqual(repo_helpers.normalize_dashboard_url("example.com"), "https://example.com/")
        self.assertEqual(
            repo_helpers.normalize_dashboard_url("https://example.com/foo?x=1"),
            "https://example.com/foo?x=1",
        )

    def test_normalize_dashboard_url_rejects_non_http_schemes(self) -> None:
        self.assertEqual(repo_helpers.normalize_dashboard_url("ftp://example.com"), "")


if __name__ == "__main__":
    unittest.main()
