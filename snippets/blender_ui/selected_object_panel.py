"""
selected_object_panel.py

Code demonstrating how to create a panel that's only visible when an object is active and selected.

James Sherratt
"""
import bpy


class HelloSelectedObject(bpy.types.Panel):
    """Creates a Panel in the Object properties tab.
    This panel is only visible when an object in the 
    3D viewport is selected."""
    bl_label = "Hello Selected Object"
    bl_idname = "OBJECT_PT_helloselected"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.label(text="Hello! This panel only shows when an object is selected.",
            icon='WORLD_DATA')
    
    @classmethod
    def poll(cls, context):
        """This method determines when the panel is visible."""
        ob = context.object
        return (ob is not None) and (ob.select_get() == True)


def register():
    bpy.utils.register_class(HelloSelectedObject)


def unregister():
    bpy.utils.unregister_class(HelloSelectedObject)


if __name__ == "__main__":
    register()
