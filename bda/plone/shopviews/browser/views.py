from zope.interface import implements, Interface, Attribute
from Products.Five import BrowserView

from bda.plone.shopviews import shopviewsMessageFactory  as _

from Products.CMFCore.utils import getToolByName
from Products.CMFCore.interfaces import IFolderish

from plone.dexterity.utils import iterSchemata
from zope.schema import getFields
from plone.dexterity.interfaces import IDexterityContent


class IColorsView(Interface):
    """
    Redirect  view interface
    """
    
class IProductsView(Interface):
    """
    Products  view interface
    """
    
    #def currency(self):
    #    """Get the currency"""
        
    def test():
        """ test method"""
        
    def all_keywords():
        """ get all keywords in folder so we can sort on them """

    def colors():
        """ get (all) color (field) in your content type for folder """

    def variations():
        """ get (all) variation (field) in your content type for folder """

    def rtfields():
        """ get all rich text fields """

class ColorsView(BrowserView):
    """
    Browser view that does the following.
    - redirects to parent folder of product.
    - sets color to context's color
    - uses this in the folder view
    """
    implements(IColorsView)
    
    
    def __call__(self):
        request = self.request
        color = self.context.color
        redirect_url = self.context.aq_parent.absolute_url() + '/productlist_view?color=' + color
        #return self.context.redirect(redirect_url)
        return redirect_url

class ProductsView(BrowserView):
    """
    Products browser view
    """
    implements(IProductsView)
    
    #property
    #def currency(self):
    #    return self.data_provider.currency

    def test(self):
        """
        test method
        """
        
        dummy = _(u'a dummy string')
        return {'dummy': dummy}

    def find_objects(self):
        #not working at the moment
        #so the same code is 3 times below
        catalog = getToolByName(self, 'portal_catalog')
        if context.is_folderish: 
            folder_path = '/'.join(context.getPhysicalPath())
        else:
            folder_path = '/'.join(context.aq_parent.getPhysicalPath())
        results = []
        results = catalog.searchResults(path={'query': folder_path})
        return results
                
    @property    
    def all_keywords(self):
        #results = self.find_objects
        context = self.context
        catalog = getToolByName(self, 'portal_catalog')
        #if IFolderish.isProvidedBy(context.aq_base): 
        folder_path = '/'.join(context.getPhysicalPath())
        #else:
        #    folder_path = '/'.join(context.aq_parent.getPhysicalPath())
        results = []
        results = catalog.searchResults(path={'query': folder_path})
        
        tags = set()
        for item in results:
            tags.update(item.Subject)
        return sorted(tags)
        
    @property    
    def variations(self):
        #results = self.find_objects
        context = self.context
        catalog = getToolByName(self, 'portal_catalog')
        #if IFolderish.isProvidedBy(context.aq_base): 
        folder_path = '/'.join(context.getPhysicalPath())
        #else:
        #    folder_path = '/'.join(context.aq_parent.getPhysicalPath())
        results = []
        results = catalog.searchResults(path={'query': folder_path})
        
        tags = []
        for item in results:
            tags.append(item.variation)
        return sorted(tags)
        
    @property    
    def colors(self):
        #results = self.find_objects
        context = self.context
        parent = context.aq_parent.aq_inner
        catalog = getToolByName(self, 'portal_catalog')
        folder_path = '/'.join(parent.getPhysicalPath())
        results = []
        results = catalog.searchResults(path={'query': folder_path})
        
        colors = []
        for item in results:
            if item.color:
                colors.append(item.color)
        return sorted(colors)

    @property
    def rtfields(self):
        richtext_fields = []
        context=self.context
        if IDexterityContent.providedBy(context):
            for schemata in iterSchemata(context):
                for name, field in getFields(schemata).items():
                    #checking for rich text field
                    #if isinstance(field, RichText):
                    if str(field.__class__) == "<class 'plone.app.textfield.RichText'>":
                        richtext_fields.append(name)
        return richtext_fields

    @property
    def get_groups(self):
        current = api.user.get_current()
        groups_tool = getToolByName(self, 'portal_groups')
        return groups_tool.getGroupsByUserId(current)
    
    @property    
    def get_user(self):
        return  api.user.get_current()
        
        
    #@property    
    #def get_group(self):       
    #    return plone.api.user.get_users(groupname='forhandler')
        