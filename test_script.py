import bpy
import os

# Create a material with a texture.
bpy.ops.mesh.primitive_ico_sphere_add(radius=1, enter_editmode=False, location=(0, 0, 2))
mymesh = bpy.context.active_object
# Create a material and link it to the mesh
mymat = bpy.data.materials.new("mymat")
mymesh.active_material = mymat
# Not necessary, but demonstrates how to get a material from a mesh.
mymat = mymesh.active_material

# Setup nodes in the material.
mymat.use_nodes = True
node_tree = mymat.node_tree

# Add an image
img_node = node_tree.nodes.new('ShaderNodeTexImage')
# Link the image node to the bsdf shader.
diff_node = node_tree.nodes['Principled BSDF']
node_tree.links.new(img_node.outputs['Color'], diff_node.inputs['Base Color'])
# Open an image.
bpy.ops.image.open(filepath="/path/to/mytex.png")

# Set the image on the object.
img_node.image = bpy.data.images['mytex.png']


def get_view3d_area():
    '''Gets the 3d viewport. It is relative to whatever area the python script runs in.'''
    for ar in bpy.context.screen.areas.values():
        if ar.type == 'VIEW_3D':
            return ar


def set_shading_to_mat():
    '''Sets the viewport shading to 'rendered material'.'''
    area = get_view3d_area()
    area.spaces[0].shading.type = 'MATERIAL'


def set_shading_col_img():
    '''Sets the viewport colour to '(unshaded) texture'.'''
    area = get_view3d_area()
    area.spaces[0].shading.color_type = 'TEXTURE'


# Get current objects
bpy.context.scene.objects.values()

# Activate texture shading.
set_shading_col_img()

# Get the active object
bpy.context.view_layer.objects.active = mymesh

# Set an object as selected.
mymesh.select_set(True)
