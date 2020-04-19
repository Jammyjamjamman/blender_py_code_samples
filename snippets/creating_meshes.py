"""
creating_meshes.py

James Sherratt
"""
import bpy


# Delete any selected meshes.
bpy.ops.object.delete()

# Create a new cone. bpy.ops.mesh.primitive...() can be used to create blender-supplied meshes.
bpy.ops.mesh.primitive_cone_add(vertices=8, radius1=0.5, radius2=0, depth=2)

# Create a mesh from verts.
# Credit: ludiccc and DrPositron https://blender.stackexchange.com/a/159185
def add_mesh(name, verts, faces, edges=[], col_name="Collection"):
    mesh = bpy.data.meshes.new(name)
    obj = bpy.data.objects.new(mesh.name, mesh)
    col = bpy.data.collections.get(col_name)
    col.objects.link(obj)
    bpy.context.view_layer.objects.active = obj
    mesh.from_pydata(verts, edges, faces)


verts = [( 1.0,  1.0,  0.0), 
         ( 1.0, -1.0,  0.0),
         (-1.0, -1.0,  0.0),
         (-1.0,  1.0,  0.0),
         ]
faces = [[0, 1, 2, 3]]
add_mesh("myBeautifulMesh_1", verts, faces)

verts = [( 3.0,  1.0,  0.0), 
         ( 3.0, -1.0,  0.0),
         ( 2.0, -1.0,  0.0),
         ( 2.0,  1.0,  0.0),
         ]
add_mesh("myBeautifulMesh_2", verts, faces)

# Select meshes (which is the default type).
bpy.ops.object.select_by_type()
# Make one of the selected meshes active.
bpy.context.view_layer.objects.active = bpy.context.view_layer.objects.selected[0]
# Merge into 1 object.
bpy.ops.object.join()

# Enter editmode in the object.
bpy.ops.object.mode_set(mode='EDIT')
# Add a mesh to the object.
bpy.ops.mesh.primitive_uv_sphere_add(radius=1, enter_editmode=False, location=(1.25, 0, 0))
# back to object mode.
bpy.ops.object.mode_set(mode='OBJECT')
