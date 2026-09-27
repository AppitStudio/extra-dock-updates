import unittest

from register_keyper_beta import beta_payload


def event():
    return {
        "repository": {"full_name": "AppitStudio/extra-dock-updates"},
        "release": {
            "tag_name": "beta",
            "prerelease": True,
            "name": "B4.4.0",
            "published_at": "2026-09-27T10:41:08Z",
            "assets": [{"name": "extraDock.dmg"}],
        },
    }


class BetaRegistrationTest(unittest.TestCase):
    def test_published_beta_registers_without_mutable_download_url(self):
        self.assertEqual(
            beta_payload(event()),
            {
                "version": "4.4.0",
                "released_at": "2026-09-27T10:41:08Z",
                "is_prerelease": True,
            },
        )

    def test_rejects_wrong_release_or_missing_asset(self):
        for change in (
            {"prerelease": False},
            {"tag_name": "prod"},
            {"name": "B4.4.0;echo unsafe"},
            {"name": "B5.0.0"},
            {"assets": []},
        ):
            with self.subTest(change=change):
                payload = event()
                payload["release"].update(change)
                with self.assertRaises(ValueError):
                    beta_payload(payload)


if __name__ == "__main__":
    unittest.main()
