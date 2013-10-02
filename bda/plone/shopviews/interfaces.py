""" Define interfaces for bda.plone.shopviews.
"""

from zope.interface import (
    Interface,
    Attribute,
)

from zope import schema
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('bda.plone.shop')

#import zope.interface
#from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm


class IShopviews(zope.interface.Interface):
    """ A layer specific for this add-on product.

    This interface is referred in browserlayer.xml.

    All views and viewlets register against this layer will appear on
    your Plone site only when the add-on installer has been run.
    """
    
    
class IShopSettings(Interface):
    """Shopview controlpanel schema.
    """

    shopviews_fields=schema.List(
        title=_(u"Specify all al the fields that you want to block"),
        description=_(u"help_shopviews_fields", default=u'One fieldname on each line'),
        required=False,
        value_type=schema.TextLine(),
        default=[])

     