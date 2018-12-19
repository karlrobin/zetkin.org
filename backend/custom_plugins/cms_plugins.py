# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from . import models

@plugin_pool.register_plugin
class Blurb(CMSPluginBase):
    model = models.Blurb
    name = 'Blurb'
    render_template = 'custom_plugins/blurb.html'


@plugin_pool.register_plugin
class Grid(CMSPluginBase):
    allow_children = True
    child_classes = ['Blurb']
    render_template = 'custom_plugins/grid.html'
