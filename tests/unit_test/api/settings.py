import os
import pytest

from moziris.api.settings import Settings
from moziris.base.testcase import BaseTest


class Test(BaseTest):
    @pytest.mark.details(
        description="Unit tests for the Settings class."
    )
    def run(self):
        assert Settings.DEFAULT_MIN_SIMILARITY == 0.8, "Settings.DEFAULT_MIN_SIMILARITY is 0.8"
        assert os.path.isdir(Settings.package_root), "Settings.package_root directory exists"
        assert os.path.isdir(Settings.code_root), "Settings.code_root directory exists"
