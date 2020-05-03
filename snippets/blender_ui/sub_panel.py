import bpy


class ObjectButtonsPanel:
    """Settings for both our new panels."""
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"


class HelloWorldPanel(ObjectButtonsPanel, bpy.types.Panel):
    """Creates a Panel in the Object properties window."""
    bl_label = "Hello World Panel"
    bl_idname = "OBJECT_PT_hello"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.label(text="Hello world!", icon='WORLD_DATA')


class MySubPanel(ObjectButtonsPanel, bpy.types.Panel):
    """The subpanel."""
    bl_label = "My Subpanel"
    bl_idname = "OBJECT_PT_mysubpanel"
    bl_parent_id = "OBJECT_PT_hello" # This is what defines the panel as a subpanel.
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout

        ob = context.object

        row = layout.row()
        row.label(text="this is the subpanel.")

def register():
    bpy.utils.register_class(HelloWorldPanel)
    bpy.utils.register_class(MySubPanel)


def unregister():
    bpy.utils.unregister_class(HelloWorldPanel)
    bpy.utils.register_class(MySubPanel)


if __name__ == "__main__":
    register()
