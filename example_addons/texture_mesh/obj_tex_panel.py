import bpy
from bpy.types import Panel


class SimpleTexturePanel(Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Simple Texture Panel"
    bl_idname = "OBJECT_PT_simple_tex"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout
        wm = context.window_manager

        row = layout.row()
        row.prop(wm, "obj_tex_file")

        row = layout.row()
        row.template_icon_view(wm, "my_previews")
