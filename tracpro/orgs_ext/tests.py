from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from tracpro.test import TracProTest


class OrgExtCRUDLTest(TracProTest):
    def test_home(self):
        url = reverse('orgs_ext.org_home')

        self.login(self.admin)

        response = self.url_get('unicef', url)
        self.assertEqual(response.status_code, 200)
