"""
texture_view.py

Sets the 3D viewport to a mode which lets you view textures
linked to meshes.

James Sherratt
"""
import bpy


def get_view3d_area():
    '''Gets the 3d viewport. It is relative to whatever area the python script runs in.
    Returns None if there's no area.'''
    for ar in bpy.context.screen.areas.values():
        if ar.type == 'VIEW_3D':
            return ar


def render_view3d():
    '''Sets the viewport shading to '(rendered) material'.'''
    area = get_view3d_area()
    # Check there is a 3d view.
    if area is not None:
        area.spaces[0].shading.type = 'MATERIAL'


def tex_view3d():
    '''Sets the viewport colour to '(unshaded) texture'.'''
    area = get_view3d_area()
    # Check there is a 3d view.
    if area is not None:
        area.spaces[0].shading.type = 'SOLID'
        area.spaces[0].shading.color_type = 'TEXTURE'

# Simple texture view.
tex_view3d()
