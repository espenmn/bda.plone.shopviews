from plone.app.registry.browser import controlpanel
from plone.registry.interfaces import IRegistry
from bda.plone.shopviews.interfaces import IShopviewsSettings

from bda.plone.shopviews import shopviewsMessageFactory  as _

class ShopviewsSettingsEditForm(controlpanel.RegistryEditForm):
    schema = IShopviewsSettings
    label = _(u"Shopviews settings")
    description = _(u"Configurations for bda.plone.shopviews")

    def updateFields(self):
        super(ShopviewsSettingsEditForm, self).updateFields()

    def updateWidgets(self):
        super(ShopviewsSettingsEditForm, self).updateWidgets()


class ShopviewsSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = ShopviewsSettingsEditForm
