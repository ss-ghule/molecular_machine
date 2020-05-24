__version__='1.0.0'

#test_file_path='/home/vanka/ruchi/output_only/system3/system3_a/system3_a_md_29_12_19.xyz'
test_file_path='/home/vanka/ruchi/output_only/system1/system1_a/system1_a_30_1_20.xyz'


input_parent_dir_path='/home/vanka/ruchi/output_only'
input_system_name='system1'
input_subsystem_name='system1_b'
input_file_name='system1_b_md_30_1_20.xyz'
output_parent_dir_path='output'

#GENERAL PARAMETERS
ring_atom_no=0
track_atom_no=199

start_frame_no=0
end_frame_no=1000
step_size=10

frame_no_pos=1
track_range=2
simulation_time_step=0.5 #in femto

rotation_method='rot_part_atomic_r_t_3'
translation_method='trans_com'
RKE_method='energy_rot_hybrid_1'
TKE_method='energy_trans_com'
axis='x'

tasks='0'

ring_atom_no_list=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200]

track_atom_no_list=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200]

code_dir_path='/home/vanka/siddharth/molecular_machines_project/molecular_machines'