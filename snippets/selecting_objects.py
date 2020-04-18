"""
selecting_objects.py

James Sherratt
"""
import bpy


### Selecting objects in the 3D View. ###
# Select/ deselect all objects.
bpy.ops.object.select_all()

# Select the cube.
bpy.context.view_layer.objects['Camera'].select_set(True)

# Select by type (the lamp).
# (Note: 'extend' means don't delselect already selected objects.)
bpy.ops.object.select_by_type(extend=True, type='LIGHT')

# Select the active object (the cube).
bpy.context.view_layer.objects.active.select_set(True)

# Set the camera as the active object.
bpy.context.view_layer.objects.active = bpy.context.view_layer.objects['Camera']

### Selecting objects in Python. ###
# Get a list of all objects.
all_objs = bpy.context.view_layer.objects.values()

# List of selected objects.
selected_objs = bpy.context.view_layer.objects.selected.values()

# Get the active object.
active_obj = bpy.context.active_object
