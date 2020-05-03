"""
texture_mode_checkbox.py

Example code for creating a BoolProperty, which lets you
switch viewports between textured and material mode.

James Sherratt
"""
import bpy
from bpy.props import BoolProperty


def get_view3d_area(context):
    '''Gets the 3d viewport. It is relative to whatever area the python script runs in.
    Returns None if there's no area.'''
    for ar in context.screen.areas.values():
        if ar.type == 'VIEW_3D':
            return ar


def is_texture_mode(self):
    if self.type == 'SOLID':
        return self.color_type == 'TEXTURE'
    else:
        return False

def set_mode(self, use_tex_mode):
    if use_tex_mode:
        self.color_type = 'TEXTURE'
    else:
        self.color_type = 'MATERIAL'


bpy.types.View3DShading.tex_view = bpy.props.BoolProperty(name="my_prop", get=is_texture_mode, set=set_mode)


class TexViewPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Texture View"
    bl_idname = "OBJECT_PT_tex_view"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout
        
        spaces = get_view3d_area(context).spaces

        for i, space in enumerate(spaces):
            shade = space.shading
            row = layout.row()
            row.label(text=f"viewport {i+1}:")
            row.prop(shade, "tex_view")


def register():
    bpy.utils.register_class(TexViewPanel)


def unregister():
    bpy.utils.unregister_class(TexViewPanel)


if __name__ == "__main__":
    register()
