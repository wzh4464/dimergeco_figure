###
# File: ./figure/main.py
# Created Date: Monday, February 10th 2025
# Author: Zihan
# -----
# Last Modified: Monday, 10th February 2025 9:34:42 pm
# Modified By: the developer formerly known as Zihan at <wzh4464@gmail.com>
# -----
# HISTORY:
# Date      		By   	Comments
# ----------		------	---------------------------------------------------------
###
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager

# 设置后端
matplotlib.use("Agg")


# 添加字体文件并验证
def setup_font(font_path):
    try:
        # 添加字体文件
        font_manager.fontManager.addfont(font_path)
        prop = font_manager.FontProperties(fname=font_path)

        # 验证字体是否成功加载
        if prop.get_name():
            print(f"Successfully loaded font: {prop.get_name()}")
        else:
            raise Exception("Font not properly loaded")

        return prop
    except Exception as e:
        print(f"Error loading font: {e}")
        return None


# 设置字体路径和加载字体
font_path = "/backup/codes/actions-runner/_work/PhDThesis/PhDThesis/Times New Roman.ttf"
font_prop = setup_font(font_path)

# 基准字体大小及各元素字体大小比例
BASE_FONT_SIZE = 20
FONT_SCALES = {
    'base': 1.0,           # 基准大小
    'title': 1.4,         # 标题
    'axis_label': 1.2,    # 坐标轴标签
    'tick_label': 1.2,    # 刻度标签
    'legend': 1.0,        # 图例
    'annotation': 0.8,    # 注释
}

# 创建legend字体属性
legend_font = font_manager.FontProperties(
    family='serif',
    size=BASE_FONT_SIZE * FONT_SCALES['legend'],
    fname=font_path
)

# 全局字体设置
plt.rcParams.update(
    {
        "font.family": "serif",
        "font.serif": [font_prop.get_name() if font_prop else "serif"],
        "font.size": BASE_FONT_SIZE * FONT_SCALES['base'],
        "axes.titlesize": BASE_FONT_SIZE * FONT_SCALES['title'],
        "axes.labelsize": BASE_FONT_SIZE * FONT_SCALES['axis_label'],
        "xtick.labelsize": BASE_FONT_SIZE * FONT_SCALES['tick_label'],
        "ytick.labelsize": BASE_FONT_SIZE * FONT_SCALES['tick_label'],
        "legend.fontsize": BASE_FONT_SIZE * FONT_SCALES['legend'],
    }
)


# First Plot - Efficiency vs. Number of Nodes
def create_efficiency_plot():
    data = {
        "nodes": [1, 4, 8, 16, 24],
        "Amazon 1000": [1, 0.67, 0.52, 0.44, 0.39],
        "Classic4": [1, 0.88, 0.76, 0.55, 0.52],
        "RCV1-Large": [1, 0.82, 0.66, 0.55, 0.47],
    }
    df = pd.DataFrame(data)

    markers = ["o", "s", "^"]
    colors = ["#e41a1c", "#377eb8", "#4daf4a"]

    plt.figure(figsize=(8, 6))

    for i, column in enumerate(df.columns[1:]):
        plt.plot(
            df["nodes"],
            df[column],
            marker=markers[i],
            markersize=8,
            label=column,
            color=colors[i],
            linewidth=2,
        )

    plt.title("Efficiency vs. Number of Nodes", pad=15, fontproperties=font_prop, 
             fontsize=BASE_FONT_SIZE * FONT_SCALES['title'])
    plt.xlabel("Number of Nodes", fontproperties=font_prop, 
              fontsize=BASE_FONT_SIZE * FONT_SCALES['axis_label'])
    plt.ylabel("Efficiency", fontproperties=font_prop, 
              fontsize=BASE_FONT_SIZE * FONT_SCALES['axis_label'])
    plt.ylim(0.0, 1.1)
    plt.xticks(range(0, 26, 5))
    plt.yticks()
    plt.xlim(0, 26)
    plt.legend(frameon=True, prop=legend_font)
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.savefig("efficiency.png", dpi=300, bbox_inches="tight")
    plt.close()


# Second Plot - Optimization of Partition Setting
def create_optimization_plot():
    data_updated = {
        "partition #": [25, 36, 49, 81, 100, 121],
        "repetition #": [2, 3, 4, 4, 4, 5],
        "time(s)": [3701, 2397, 1660, 721, 512, 665],
    }
    df_updated = pd.DataFrame(data_updated)
    colors = ["#377eb8", "#ff7f00"]

    fig, ax1 = plt.subplots(figsize=(8, 6))

    # First y-axis - Repetition #
    ax1.plot(
        df_updated["partition #"],
        df_updated["repetition #"],
        marker="D",
        markersize=8,
        color=colors[0],
        label="Repetition #",
        linewidth=2,
    )

    ax1.set_xlabel("Partition #", fontproperties=font_prop, 
                  fontsize=BASE_FONT_SIZE * FONT_SCALES['axis_label'])
    ax1.set_ylabel("Repetition #", fontproperties=font_prop, 
                  fontsize=BASE_FONT_SIZE * FONT_SCALES['axis_label'])
    ax1.tick_params(axis="both")
    ax1.axvline(x=100, color="red", linestyle="--", linewidth=1.5)

    # 添加注释
    ax1.annotate(
        "Partition 100",
        xy=(100, 1),
        xytext=(105, 2),
        arrowprops=dict(facecolor="red", shrink=0.05),
        fontsize=BASE_FONT_SIZE * FONT_SCALES['annotation'],
        color="red",
        fontweight="bold",
        fontproperties=font_prop,
    )

    ax1.set_ylim(0, 8)
    ax1.set_yticks(range(0, 9))

    # Second y-axis - Time(s)
    ax2 = ax1.twinx()
    ax2.plot(
        df_updated["partition #"],
        df_updated["time(s)"],
        marker="v",
        markersize=8,
        color=colors[1],
        label="Time(s)",
        linewidth=2,
    )

    ax2.set_ylabel("Time(s)", fontproperties=font_prop, 
                  fontsize=BASE_FONT_SIZE * FONT_SCALES['axis_label'])
    ax2.tick_params(axis="y")
    ax2.set_ylim(0, 4000)
    ax2.set_yticks(range(0, 4500, 500))

    plt.title("Optimisation of Partition Setting", pad=15, fontproperties=font_prop,
             fontsize=BASE_FONT_SIZE * FONT_SCALES['title'])
    ax1.grid(True, linestyle="--", alpha=0.7)

    # Combine legends
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(
        lines1 + lines2,
        labels1 + labels2,
        loc="upper right",
        frameon=True,
        prop=legend_font
    )

    plt.tight_layout()
    plt.savefig("optimisation.png", dpi=300, bbox_inches="tight")
    plt.close()


def main():
    if font_prop is None:
        print("Warning: Using default font as Times New Roman could not be loaded")

    create_efficiency_plot()
    create_optimization_plot()


if __name__ == "__main__":
    main()
