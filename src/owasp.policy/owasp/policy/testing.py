from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting

from plone.testing import z2

from zope.configuration import xmlconfig

class OwaspPolicy(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)
    
    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import owasp.policy
        xmlconfig.file('configure.zcml', owasp.policy, context=configurationContext)
        
        # Install products that use an old-style initialize() function
        z2.installProduct(app, 'Products.PythonField')
        z2.installProduct(app, 'Products.TALESField')
        z2.installProduct(app, 'Products.TemplateFields')
        z2.installProduct(app, 'Products.PloneFormGen')
        z2.installProduct(app, 'Products.membrane')        
    
    def tearDownZope(self, app):
        # Uninstall products installed above
        z2.uninstallProduct(app, 'Products.PloneFormGen')
        z2.uninstallProduct(app, 'Products.TemplateFields')
        z2.uninstallProduct(app, 'Products.TALESField')
        z2.uninstallProduct(app, 'Products.PythonField')
        z2.uninstallProduct(app, 'Products.membrane')        
        
    def setUpPloneSite(self, portal):
        applyProfile(portal, 'owasp.policy:default')

OWASP_POLICY_FIXTURE = OwaspPolicy()
OWASP_POLICY_INTEGRATION_TESTING = IntegrationTesting(bases=(OWASP_POLICY_FIXTURE,), name="Owasp:Integration")
