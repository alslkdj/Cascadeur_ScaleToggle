import csc
import common.selection_operations as so
import common.update_operations as c_uo

def command_name():
    return "Scale.Scale to 0"

def run(scene):
    selected_joints_objs = set(so.selected_objects_by_type(scene, 'Joint'))
    if len(selected_joints_objs) == 0:
        raise Exception("Nothing selected!")
        
    def mod(modelEditor, updateEditor, scene):
        behaviour_viewer = scene.model_viewer().behaviour_viewer()
        data_editor = modelEditor.data_editor()
        frame = scene.get_current_frame()
        
        for joint_id in selected_joints_objs:
            transform_id = behaviour_viewer.get_behaviour_by_name(joint_id, 'Transform')
            data_id = behaviour_viewer.get_behaviour_data(transform_id, 'local_scale')
            data_editor.set_data_value(data_id, frame, (0.0001,0.0001,0.0001))
            
    scene.modify(command_name(), mod)