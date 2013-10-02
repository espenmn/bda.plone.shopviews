from plone.app.registry.browser import controlpanel
from plone.registry.interfaces import IRegistry
from ..interfaces import IShopviewSettings

from bda.plone.shopviews import shopviewsMessageFactory  as _

#from zope.component import getUtility


class ShopviewsSettingsEditForm(controlpanel.RegistryEditForm):
    schema = IShopviewSettings
    label = _(u"Shopviews settings")
    description = _(u"Configurations for bda.plone.shopviews")

    def updateFields(self):
        super(ShopviewsSettingsEditForm, self).updateFields()

    def updateWidgets(self):
        super(ShopviewsSettingsEditForm, self).updateWidgets()


class ShopviewsSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = ShopviewsSettingsEditForm
