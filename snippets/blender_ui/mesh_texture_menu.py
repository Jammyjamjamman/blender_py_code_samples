"""
mesh_texture_menu.py

Panel which shows the Image properties for an image, which is linked to the
"diffuse" property of a material with nodes (e.g. principled BSDF). Sti
"""
import bpy


class HelloTexturePanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Hello World Panel"
    bl_idname = "OBJECT_PT_hellotexture"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout

        ob = context.object

        row = layout.row()
        row.label(text="Hello texture!", icon='WORLD_DATA')

        layout = self.layout

        tex = ob.active_material.node_tree.nodes['Image Texture']
        # This is not ideal because this layout does not change when the 
        layout.template_image(data=tex, property="image", image_user=tex.image_user)



def register():
    bpy.utils.register_class(HelloTexturePanel)


def unregister():
    bpy.utils.unregister_class(HelloTexturePanel)


if __name__ == "__main__":
    register()
