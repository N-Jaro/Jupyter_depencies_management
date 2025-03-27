# util.py

import matplotlib.pyplot as plt
import math

def plot_multichannel_image(sample_array, cmap='viridis'):
    """
    Plot all channels of a single sample from a 3D numpy array.

    Parameters:
    - sample_array (np.ndarray): A numpy array of shape (H, W, C), where C is the number of channels.
    - cmap (str): Colormap to use for plotting (default: 'viridis')
    """
    if sample_array.ndim != 3:
        raise ValueError("Input array must be 3D with shape (H, W, C)")

    height, width, channels = sample_array.shape
    n_cols = 4
    n_rows = math.ceil(channels / n_cols)

    fig, axes = plt.subplots(n_rows, n_cols, figsize=(4 * n_cols, 4 * n_rows))
    axes = axes.flatten()

    for i in range(channels):
        ax = axes[i]
        ax.imshow(sample_array[:, :, i], cmap=cmap)
        ax.set_title(f'Channel {i+1}')
        ax.axis('off')

    # Hide any unused subplots
    for j in range(channels, len(axes)):
        axes[j].axis('off')

    plt.tight_layout()
    plt.show()


def greet(name):
    return f"Hello, {name}! Welcome to your Jupyter Notebook."