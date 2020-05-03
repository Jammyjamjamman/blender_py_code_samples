import bpy


def get_view3d_area(context):
    '''Gets the 3d viewport. It is relative to whatever area the python script runs in.
    Returns None if there's no area.'''
    for ar in context.screen.areas.values():
        if ar.type == 'VIEW_3D':
            return ar


def is_texture_mode(self):
    if self.type == 'SOLID':
        return self.color_type == 'TEXTURE'
    else:
        return False

def set_mode(self, use_tex_mode):
    if use_tex_mode:
        self.color_type = 'TEXTURE'
    else:
        self.color_type = 'MATERIAL'


class VIEW3D_UL_viewshadings(bpy.types.UIList):
    # The draw_item function is called for each item of the collection that is visible in the list.
    #   data is the RNA object containing the collection,
    #   item is the current drawn item of the collection,
    #   icon is the "computed" icon for the item (as an integer, because some objects like materials or textures
    #   have custom icons ID, which are not available as enum items).
    #   active_data is the RNA object containing the active property for the collection (i.e. integer pointing to the
    #   active item of the collection).
    #   active_propname is the name of the active property (use 'getattr(active_data, active_propname)').
    #   index is index of the current item in the collection.
    #   flt_flag is the result of the filtering process for this item.
    #   Note: as index and flt_flag are optional arguments, you do not have to use/declare them here if you don't
    #         need them.
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
        # draw_item must handle the three layout types... Usually 'DEFAULT' and 'COMPACT' can share the same code.
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            # You should always start your row layout by a label (icon + text), or a non-embossed text field,
            # this will also make the row easily selectable in the list! The later also enables ctrl-click rename.
            # We use icon_value of label, as our given icon is an integer value, not an enum ID.
            # Note "data" names should never be translated!
            if  item.type == 'VIEW_3D':
                layout.prop(item.spaces[0].shading, "tex_view", text="test")
            else:
                layout = None
        # 'GRID' layout type should be as compact as possible (typically a single icon!).
        elif self.layout_type in {'GRID'}:
            layout.alignment = 'CENTER'
            layout.label(text="", icon_value=icon)


# And now we can use this list everywhere in Blender. Here is a small example panel.
class UIListPanelExample(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Tex mode panel"
    bl_idname = "OBJECT_PT_ui_list_example"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout

        screen = context.screen
        obj = context.object

        # template_list now takes two new args.
        # The first one is the identifier of the registered UIList to use (if you want only the default list,
        # with no custom draw code, use "UI_UL_list").
        layout.template_list("VIEW3D_UL_viewshadings", "", screen, "areas", screen, "dummy_active")

        # The second one can usually be left as an empty string.
        # It's an additional ID used to distinguish lists in case you
        # use the same list several times in a given area.
#        layout.template_list("MATERIAL_UL_matslots_example", "compact", obj, "material_slots",
#                             obj, "active_material_index", type='COMPACT')

class TextureView(bpy.types.PropertyGroup):
    tex_view = bpy.props.BoolProperty(name="texture view")


def update_areas(self, context):
    screen = context.screen
    screen.V3D_areas.clear()
    for ar in screen.areas:
        if ar.type == 'VIEW_3D':
            prop = screareas.add()
            prop.tex_view = ar.spaces[0].shading.tex_view


def register():
    bpy.utils.register_class(VIEW3D_UL_viewshadings)
    bpy.utils.register_class(UIListPanelExample)
    bpy.utils.register_class(TextureView)
    
    bpy.types.View3DShading.tex_view = bpy.props.BoolProperty(name="my_prop", get=is_texture_mode, set=set_mode, update=update_areas)
    bpy.types.Screen.V3D_areas = bpy.props.CollectionProperty(type=TextureView)
    bpy.types.Screen.dummy_active = bpy.props.IntProperty(default=0)


def unregister():
    bpy.utils.unregister_class(VIEW3D_UL_viewshadings)
    bpy.utils.unregister_class(UIListPanelExample)
    bpy.utils.register_class(MyPropertyGroup)
    bpy.types.Screen.my_prop_grp = bpy.props.PointerProperty(type=MyPropertyGroup)


if __name__ == "__main__":
    register()