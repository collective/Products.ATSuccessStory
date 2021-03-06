# -*- coding: utf-8 -*-
#
# File: ATSuccessStoryFolder.py
#
# Copyright (c) 2008 by []
# Generator: ArchGenXML Version 2.1
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """Franco Pellegrini <frapell@menttes.com>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
import interfaces
from Products.ATContentTypes.content.folder import ATFolder
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.ATSuccessStory.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((


),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

ATSuccessStoryFolder_schema = getattr(ATFolder, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class ATSuccessStoryFolder(ATFolder):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IATSuccessStoryFolder)

    meta_type = 'ATSuccessStoryFolder'
    _at_rename_after_creation = True

    schema = ATSuccessStoryFolder_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

registerType(ATSuccessStoryFolder, PROJECTNAME)
# end of class ATSuccessStoryFolder

##code-section module-footer #fill in your manual code here
##/code-section module-footer



