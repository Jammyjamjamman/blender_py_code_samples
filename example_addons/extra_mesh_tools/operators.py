"""
Tools for creating meshes from python data.

James Sherratt
"""
import bpy

# Create a mesh from verts.
# Credit: ludiccc and DrPositron https://blender.stackexchange.com/a/159185
def add_mesh(name, verts, faces, edges=[], col_name="Collection"):
    """Adds a new mesh to the collection, given verts, faces and edges."""
    mesh = bpy.data.meshes.new(name)
    obj = bpy.data.objects.new(mesh.name, mesh)
    col = bpy.data.collections.get(col_name)
    col.objects.link(obj)
    bpy.context.view_layer.objects.active = obj
    mesh.from_pydata(verts, edges, faces)


def append_mesh(name, verts, faces, edges=[], col_name="Collection"):
    """Append new mesh data to an already existing object."""
    # Create a temporary mesh.
    add_mesh("{}_tmp_extra_mesh_tools".format(name), verts, faces, edges, col_name)
    # Set the temporary mesh as selected
    bpy.context.active_object.select_set(True)
    ob_to_append_to = bpy.context.view_layer.objects[name]
    ob_to_append_to.select_set(True)
    bpy.context.view_layer.objects.active = ob_to_append_to
    bpy.ops.object.join()


if __name__ == "__main__":
    # Example usage.
    import extra_mesh_tools.operators as mesh_op
    verts = [( 1.0,  1.0,  0.0), 
            ( 1.0, -1.0,  0.0),
            (-1.0, -1.0,  0.0),
            (-1.0,  1.0,  0.0),
            ]
    faces = [[0, 1, 2, 3]]
    mesh_op.add_mesh("myBeautifulMesh_1", verts, faces)

    verts = [( 3.0,  1.0,  0.0), 
            ( 3.0, -1.0,  2.0),
            ( 2.0, -1.0,  2.0),
            ( 2.0,  1.0,  0.0),
            ]
    faces = [[0, 1, 2, 3]]
    mesh_op.append_mesh("myBeautifulMesh_1", verts, faces)
