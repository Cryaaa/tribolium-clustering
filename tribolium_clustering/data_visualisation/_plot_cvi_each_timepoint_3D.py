def plot_cvi_each_timepoint_3D(cvi_scores_concatenated, timepoints_list, cluster_numbers, cvi_name = '', timepoint_label = 'Timepoints'):
    import numpy as np
    from matplotlib import pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    from matplotlib import cm

    x = np.array(timepoints_list)
    y = np.array(cluster_numbers)
    z = cvi_scores_concatenated

    X, Y = np.meshgrid(x, y)
    Z = np.reshape(z, X.shape)  # Z.shape must be equal to X.shape = Y.shape

    fig = plt.figure(figsize = (20,20))
    ax = fig.add_subplot(projection='3d')

    ax.plot_surface(X, Y, Z,cmap=cm.coolwarm)

    ax.set_xlabel(timepoint_label)
    ax.set_ylabel('Number of Clusters')
    ax.set_zlabel(cvi_name)

    ax.view_init(elev=20., azim=65)

    plt.show()