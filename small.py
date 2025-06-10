###
# File: ./dimergeco_figure/small.py
# Created Date: Tuesday, June 10th 2025
# Author: Zihan
# -----
# Last Modified: Tuesday, 10th June 2025 4:25:35 pm
# Modified By: the developer formerly known as Zihan at <wzh4464@gmail.com>
# -----
# HISTORY:
# Date      		By   	Comments
# ----------		------	---------------------------------------------------------
###

# T_m: 5, T_n: 5

import pandas as pd
import matplotlib.pyplot as plt
from figure import *

def create_performance_plot():
    # 准备数据
    sizes = ['5x5', '10x10', '15x15', '20x20']
    methods = ['SCC', 'NMTF', 'PNMTF', 'DiMergeCo-SCC']
    
    # NMI数据
    nmi_data = {
        'SCC': [0.48, 0.61, 0.72, 0.76],
        'NMTF': [0.32, 0.48, 0.58, 0.60],
        'PNMTF': [0.33, 0.51, 0.55, 0.57],
        'DiMergeCo-SCC': [0.35, 0.60, 0.69, 0.74]
    }
    
    # ARI数据
    ari_data = {
        'SCC': [0.34, 0.49, 0.57, 0.68],
        'NMTF': [0.18, 0.31, 0.42, 0.52],
        'PNMTF': [0.14, 0.33, 0.39, 0.48],
        'DiMergeCo-SCC': [0.23, 0.42, 0.55, 0.62]
    }
    
    # 设置颜色和标记
    colors = ["#e41a1c", "#377eb8", "#4daf4a", "#984ea3"]
    markers = ["o", "s", "^", "D"]
    
    # 绘制NMI图
    plt.figure(figsize=(8, 6))
    for i, method in enumerate(methods):
        plt.plot(sizes, nmi_data[method], marker=markers[i], markersize=8,
                label=method, color=colors[i], linewidth=2)
    
    plt.title("NMI Performance", pad=15, fontproperties=font_prop,
              fontsize=BASE_FONT_SIZE * FONT_SCALES['title'])
    plt.xlabel("Co-cluster Size", fontproperties=font_prop,
               fontsize=BASE_FONT_SIZE * FONT_SCALES['axis_label'])
    plt.ylabel("NMI", fontproperties=font_prop,
               fontsize=BASE_FONT_SIZE * FONT_SCALES['axis_label'])
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.ylim(0.0, 1.0)
    plt.legend(frameon=True, prop=legend_font)
    plt.tight_layout()
    plt.savefig("nmi_small.png", dpi=300, bbox_inches="tight")
    plt.close()
    
    # 绘制ARI图
    plt.figure(figsize=(8, 6))
    for i, method in enumerate(methods):
        plt.plot(sizes, ari_data[method], marker=markers[i], markersize=8,
                label=method, color=colors[i], linewidth=2)
    
    plt.title("ARI Performance", pad=15, fontproperties=font_prop,
              fontsize=BASE_FONT_SIZE * FONT_SCALES['title'])
    plt.xlabel("Co-cluster Size", fontproperties=font_prop,
               fontsize=BASE_FONT_SIZE * FONT_SCALES['axis_label'])
    plt.ylabel("ARI", fontproperties=font_prop,
               fontsize=BASE_FONT_SIZE * FONT_SCALES['axis_label'])
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.ylim(0.0, 1.0)
    plt.legend(frameon=True, prop=legend_font)
    plt.tight_layout()
    plt.savefig("ari_small.png", dpi=300, bbox_inches="tight")
    plt.close()

def main():
    if font_prop is None:
        print("Warning: Using default font as Times New Roman could not be loaded")
    
    create_performance_plot()

if __name__ == "__main__":
    main()
