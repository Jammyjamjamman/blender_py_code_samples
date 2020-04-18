"""
texturing_objects.py

Sets a texture using the cycles node tree.
Hint: look at texture_view.py to see how to set the viewport to view textures.

James Sherratt
"""
import bpy


# Create a mesh.
bpy.ops.mesh.primitive_ico_sphere_add(radius=1, enter_editmode=False, location=(0, 0, 2))
# select the new mesh in python.
mymesh = bpy.context.active_object


# Create a material and link it to the mesh.
mymat = bpy.data.materials.new("mymat")
mymesh.active_material = mymat
# Not necessary, but demonstrates how to get a material from a mesh.
mymat = mymesh.active_material

# Setup node trees in the material (this will set the shader to 'Principled BSDF').
mymat.use_nodes = True
node_tree = mymat.node_tree

# Add an image node.
img_node = node_tree.nodes.new('ShaderNodeTexImage')
# Select the BSDF shader node so we can link the texture colour output (the image)
# to the colour input of the shader.
diff_node = node_tree.nodes['Principled BSDF']
# Link the image node to the bsdf shader.
node_tree.links.new(img_node.outputs['Color'], diff_node.inputs['Base Color'])
# Open an image. (Set the path of "/path/to/mytex.png" appropriately.
# An example image is supplied in the repo.)
bpy.ops.image.open(filepath="/path/to/mytex.png")

# set the image in the texture node to the image loaded above.
img_node.image = bpy.data.images['mytex.png']
