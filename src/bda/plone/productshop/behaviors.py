from zope import schema
from zope.component import provideAdapter
from zope.i18nmessageid import MessageFactory
from z3c.form.widget import ComputedWidgetAttribute
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from plone.supermodel import model
from plone.autoform.directives import widget
from plone.autoform.interfaces import IFormFieldProvider
from plone.namedfile.field import NamedBlobImage
from plone.app.dexterity.behaviors.exclfromnav import IExcludeFromNavigation
from plone.app.textfield import RichText
from .interfaces import IVariantAspect


_ = MessageFactory('bda.plone.productshop')


class IProductExcludeFromNavigation(IExcludeFromNavigation):
    """Exclude from navigation behavior for products.

    Could not find a sane way of providing default values for general behavior
    attributes based on content interface which the behavior is bound to.
    Registering ComputedWidgetAttribute to context does not help because
    context is the container in case of add form instead of a content instance.
    """


provideAdapter(ComputedWidgetAttribute(
    lambda data: True,
    field=IProductExcludeFromNavigation['exclude_from_nav']),
    name='default')


class IProductBehavior(model.Schema):
    """Product behavior.
    """
    item_number = schema.TextLine(
        title=_(u'item_number_title', default=u'Item number'),
        description=_(u'item_number_description',
                      default=u'Item number of the product'),
        required=False)

    image = NamedBlobImage(
        title=_(u'image_title', default=u'Product Image'),
        description=_(u'image_description',
                      default=u'Preview image of Product'),
        required=False)

    details = RichText(
        title=_(u'details_title', default=u'Details'),
        description=_(u'details_description',
                      default=u'Details about the product'),
        required=False)

    datasheet = RichText(
        title=_(u'datasheet_title', default=u'Datasheet'),
        description=_(u'datasheet_description',
                      default=u'Datasheet of the product'),
        required=False)


class IProductGroupBehavior(IProductBehavior):
    """Product group behavior.
    """
    model.fieldset(
        'settings',
        fields=['default_variant_aspects'])

    widget('default_variant_aspects', CheckBoxFieldWidget)
    default_variant_aspects = schema.List(
        title=_(u'default_variant_aspects_title',
                default=u'Default variant aspects'),
        description=_(u'default_variant_aspects_description',
                      default=u'Variant aspects enabled by default when '
                              u'adding new variants'),
        required=False,
        missing_value=set(),
        value_type=schema.Choice(
            vocabulary=
                'bda.plone.productshop.AvailableVariantAspectsVocabulary'))


class IVariantBehavior(IProductBehavior):
    """Variant base behavior.
    """


class IColorBehavior(model.Schema, IVariantAspect):
    """Color variant behavior.
    """
    model.fieldset(
        'aspects',
        label=_(u'aspects', default=u'Aspects'),
        fields=['color'])

    color = schema.TextLine(
        title=_(u'color_title', default=u'Color'),
        description=_(u'color_description',
                      default=u'Color of the product'),
        required=False)


class IWeightBehavior(model.Schema, IVariantAspect):
    """Weight variant behavior.
    """
    model.fieldset(
        'aspects',
        label=_(u'aspects', default=u'Aspects'),
        fields=['weight'])

    weight = schema.TextLine(
        title=_(u'weight_title', default=u'Weight'),
        description=_(u'weight_description',
                      default=u'Weight of the product'),
        required=False)


class ISizeBehavior(model.Schema, IVariantAspect):
    """Size variant behavior.
    """
    model.fieldset(
        'aspects',
        label=_(u'aspects', default=u'Aspects'),
        fields=['size'])

    size = schema.TextLine(
        title=_(u'size_title', default=u'Size'),
        description=_(u'size_description',
                      default=u'Size of the product'),
        required=False)


class IDemandBehavior(model.Schema, IVariantAspect):
    """Demand variant behavior.
    """
    model.fieldset(
        'aspects',
        label=_(u'aspects', default=u'Aspects'),
        fields=['demand'])

    demand = schema.TextLine(
        title=_(u'demand_title', default=u'Demand'),
        description=_(u'demand_description',
                      default=u'Demand of the product'),
        required=False)


class ILengthBehavior(model.Schema, IVariantAspect):
    """Length variant behavior.
    """
    model.fieldset(
        'aspects',
        label=_(u'aspects', default=u'Aspects'),
        fields=['length'])

    length = schema.TextLine(
        title=_(u'length_title', default=u'Length'),
        description=_(u'length_description',
                      default=u'Length of the product'),
        required=False)


class IWidthBehavior(model.Schema, IVariantAspect):
    """Width variant behavior.
    """
    model.fieldset(
        'aspects',
        label=_(u'aspects', default=u'Aspects'),
        fields=['width'])

    width = schema.TextLine(
        title=_(u'width_title', default=u'Width'),
        description=_(u'width_description',
                      default=u'Width of the product'),
        required=False)


class IHeightBehavior(model.Schema, IVariantAspect):
    """Height variant behavior.
    """
    model.fieldset(
        'aspects',
        label=_(u'aspects', default=u'Aspects'),
        fields=['height'])

    height = schema.TextLine(
        title=_(u'height_title', default=u'Height'),
        description=_(u'height_description',
                      default=u'Height of the product'),
        required=False)


class IIPCodeBehavior(model.Schema, IVariantAspect):
    """International protection code variant behavior.
    """
    model.fieldset(
        'aspects',
        label=_(u'aspects', default=u'Aspects'),
        fields=['ip_code'])

    ip_code = schema.TextLine(
        title=_(u'ip_code_title', default=u'IP Code'),
        description=_(u'ip_code_description',
                      default=u'International protection code of the product'),
        required=False)


class IAngleBehavior(model.Schema, IVariantAspect):
    """Angle variant behavior.
    """
    model.fieldset(
        'aspects',
        label=_(u'aspects', default=u'Aspects'),
        fields=['angle'])

    angle = schema.TextLine(
        title=_(u'angle_title', default=u'Angle'),
        description=_(u'angle_description',
                      default=u'Angle of the product'),
        required=False)
