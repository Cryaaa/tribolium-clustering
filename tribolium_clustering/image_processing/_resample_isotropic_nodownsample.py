def resample_isotropic_nodownsample(image_3d,voxelsize_yzx):
    import numpy as np
    import pyclesperanto_prototype as cle
    # we need to select a powerful GPU for this
    cle.select_device("GTX")
    if voxelsize_yzx[2] == voxelsize_yzx[1]:
        voxelsize_yzx = np.array(voxelsize_yzx)
        norm_voxelsize = voxelsize_yzx/voxelsize_yzx[2]
        input_image = cle.push_zyx(image_3d)
        resampled_image = cle.resample(input_image, factor_x=norm_voxelsize[2], 
                                       factor_y=norm_voxelsize[1], factor_z=norm_voxelsize[0])
        image_array = cle.pull_zyx(resampled_image)
        return image_array
