import os
import bpy


def main(self, context):
    path = context.window_manager.obj_tex_file
    if (path is not None) and (path != ""):
        ac_obj = context.object
        # Create a material and link it to the mesh
        basename = os.path.basename(path)
        mat = bpy.data.materials.new(basename)
        ac_obj.active_material = mat

        # Setup nodes in the material.
        mat.use_nodes = True
        node_tree = mat.node_tree

        # Add an image
        img_node = node_tree.nodes.new('ShaderNodeTexImage')
        # Link the image node to the bsdf shader.
        diff_node = node_tree.nodes['Principled BSDF']
        node_tree.links.new(img_node.outputs['Color'], diff_node.inputs['Base Color'])
        # Open an image.
        bpy.ops.image.open(filepath=path)

        # Set the image on the object.
        img_node.image = bpy.data.images[basename]


class TexOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "texture_mesh.tex_operator"
    bl_label = "Simple Object Texture Operator"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        main(self, context)
        return {'FINISHED'}