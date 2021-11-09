import os
os.environ["KIVY_TEXT"]="pil"
from kivymd.app import MDApp
from kivy.lang import Builder 
KV = '''
MDBoxLayout:
    # Will always be at the bottom of the screen.
    MDBottomAppBar:
        MDToolbar:
            title: "Title"
            icon: "git"
            type: "bottom"
            left_action_items: [["menu", lambda x: x]]
'''
class demo(MDApp):
    def build(self):
       return Builder.load_string(KV);

        
demo().run()

"""
['_CommonElevationBehavior__shadow_groups', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__draw_shadow__', '__eq__', '__events__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__metaclass__', '__module__', '__ne__', '__new__', '__proxy_getter', '__proxy_setter', '__pyx_vtable__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '_apply_transform', '_background_origin', '_background_x', '_background_y', '_clear_shadow_groups', '_elevation', '_fake_elevation', '_get_center', '_get_hard_shadow_a', '_get_soft_shadow_a', '_hard_shadow_a', '_indices_left', '_indices_right', '_iterate_layout', '_kwargs_applied_init', '_make_vertices', '_make_vertices_indices', '_on_resize', '_points_on_circle', '_proxy_ref', '_rectangle_left_pos', '_rectangle_left_width', '_rectangle_right_pos', '_rectangle_right_width', '_rounded_rectangle_height', '_rounding_percentage', '_set_hard_shadow_a', '_set_soft_shadow_a', '_shadow_origin', '_shadow_origin_x', '_shadow_origin_y', '_shadow_pos', '_shift', '_soft_shadow_a', '_soft_shadow_texture', '_total_angle', '_trigger_layout', '_update_canvas', '_update_elevation', '_update_mesh', '_update_shadow', '_update_shadow_pos', '_update_specific_text_color', '_vertices_left', '_vertices_right', '_walk', '_walk_reverse', 'a', 'add_widget', 'anchor_title', 'angle', 'apply_class_lang_rules', 'apply_property', 'b', 'background', 'background_hue', 'background_origin', 'background_palette', 'bind', 'canvas', 'center', 'center_x', 'center_y', 'children', 'clear_widgets', 'cls', 'collide_point', 'collide_widget', 'create_property', 'dec_disabled', 'device_ios', 'disabled', 'dispatch', 'dispatch_children', 'dispatch_generic', 'do_layout', 'draw_shadow', 'elevation', 'events', 'export_as_image', 'export_to_png', 'fbind', 'force_shadow_pos', 'funbind', 'g', 'get_center_x', 'get_center_y', 'get_disabled', 'get_parent_window', 'get_property_observers', 'get_right', 'get_root_window', 'get_top', 'get_window_matrix', 'getter', 'hard_shadow_cl', 'hard_shadow_offset', 'hard_shadow_pos', 'hard_shadow_size', 'hard_shadow_texture', 'height', 'icon', 'icon_color', 'ids', 'inc_disabled', 'is_event_type', 'layout_hint_with_bounds', 'left_action_items', 'line_color', 'md_bg_color', 'minimum_height', 'minimum_size', 'minimum_width', 'mode', 'notch_center_x', 'notch_radius', 'on__shadow_pos', 'on_action_button', 'on_disabled', 'on_elevation', 'on_icon', 'on_icon_color', 'on_kv_post', 'on_left_action_items', 'on_md_bg_color', 'on_mode', 'on_opacity', 'on_right_action_items', 'on_shadow_group', 'on_shadow_pos', 'on_touch_down', 'on_touch_move', 'on_touch_up', 'on_type', 'opacity', 'opposite_colors', 'orientation', 'padding', 'parent', 'pos', 'pos_hint', 'properties', 'property', 'proxy_ref', 'r', 'radius', 'register_event_type', 'remove_notch', 'remove_shadow', 'remove_widget', 'right', 'right_action_items', 'round', 'set_center_x', 'set_center_y', 'set_disabled', 'set_md_bg_color', 'set_notch', 'set_right', 'set_shadow', 'set_top', 'setter', 'shadow_group', 'shadow_pos', 'shadow_preset', 'size', 'size_hint', 'size_hint_max', 'size_hint_max_x', 'size_hint_max_y', 'size_hint_min', 'size_hint_min_x', 'size_hint_min_y', 'size_hint_x', 'size_hint_y', 'soft_shadow_cl', 'soft_shadow_offset', 'soft_shadow_pos', 'soft_shadow_size', 'spacing', 'specific_secondary_text_color', 'specific_text_color', 'theme_cls', 'title', 'to_local', 'to_parent', 'to_widget', 'to_window', 'top', 'type', 'uid', 'unbind', 'unbind_uid', 'unregister_event_types', 'update_action_bar', 'update_action_bar_text_colors', 'update_background_origin', 'update_group_property', 'update_md_bg_color', 'update_opposite_colors', 'walk', 'walk_reverse', 'widget_style', 'width', 'x', 'y']
[
"""