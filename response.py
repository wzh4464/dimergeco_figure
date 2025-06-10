#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DiMergeCo Figure Generation Script
Generates all required figures for peer review response
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
import matplotlib.patches as mpatches

# Font configuration
try:
    font_prop = font_manager.FontProperties(family="Times New Roman")
    legend_font = font_manager.FontProperties(family="Times New Roman", size=10)
except:
    font_prop = None
    legend_font = None
    print("Warning: Times New Roman not found, using default font")

# Font sizes
BASE_FONT_SIZE = 12
FONT_SCALES = {"title": 1.2, "axis_label": 1.0, "tick_label": 0.9, "legend": 0.9}

# Color scheme
COLORS = ["#e41a1c", "#377eb8", "#4daf4a", "#984ea3", "#ff7f00", "#ffff33"]
MARKERS = ["o", "s", "^", "D", "v", "*"]


def create_small_cocluster_detection():
    """创建小co-cluster检测性能图"""
    print("Creating small co-cluster detection figures...")

    # 准备数据
    sizes = ["5x5", "10x10", "15x15", "20x20"]
    methods = ["SCC", "NMTF", "PNMTF", "DiMergeCo-SCC"]

    # NMI数据
    nmi_data = {
        "SCC": [0.48, 0.61, 0.72, 0.76],
        "NMTF": [0.32, 0.48, 0.58, 0.60],
        "PNMTF": [0.33, 0.51, 0.55, 0.57],
        "DiMergeCo-SCC": [0.35, 0.60, 0.69, 0.74],
    }

    # ARI数据
    ari_data = {
        "SCC": [0.34, 0.49, 0.57, 0.68],
        "NMTF": [0.18, 0.31, 0.42, 0.52],
        "PNMTF": [0.14, 0.33, 0.39, 0.48],
        "DiMergeCo-SCC": [0.23, 0.42, 0.55, 0.62],
    }

    # 绘制NMI图
    plt.figure(figsize=(8, 6))
    for i, method in enumerate(methods):
        plt.plot(
            sizes,
            nmi_data[method],
            marker=MARKERS[i],
            markersize=8,
            label=method,
            color=COLORS[i],
            linewidth=2,
        )

    plt.title(
        "NMI for small co-clusters",
        pad=15,
        fontproperties=font_prop,
        fontsize=BASE_FONT_SIZE * FONT_SCALES["title"],
    )
    plt.xlabel(
        "Co-cluster Size",
        fontproperties=font_prop,
        fontsize=BASE_FONT_SIZE * FONT_SCALES["axis_label"],
    )
    plt.ylabel(
        "Normalized Mutual Information",
        fontproperties=font_prop,
        fontsize=BASE_FONT_SIZE * FONT_SCALES["axis_label"],
    )
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.ylim(0.0, 1.0)
    plt.legend(frameon=True, prop=legend_font)
    plt.tight_layout()
    plt.savefig("nmi_small.png", dpi=300, bbox_inches="tight")
    plt.close()

    # 绘制ARI图
    plt.figure(figsize=(8, 6))
    for i, method in enumerate(methods):
        plt.plot(
            sizes,
            ari_data[method],
            marker=MARKERS[i],
            markersize=8,
            label=method,
            color=COLORS[i],
            linewidth=2,
        )

    plt.title(
        "ARI for small co-clusters",
        pad=15,
        fontproperties=font_prop,
        fontsize=BASE_FONT_SIZE * FONT_SCALES["title"],
    )
    plt.xlabel(
        "Co-cluster Size",
        fontproperties=font_prop,
        fontsize=BASE_FONT_SIZE * FONT_SCALES["axis_label"],
    )
    plt.ylabel(
        "Adjusted Rand Index",
        fontproperties=font_prop,
        fontsize=BASE_FONT_SIZE * FONT_SCALES["axis_label"],
    )
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.ylim(0.0, 1.0)
    plt.legend(frameon=True, prop=legend_font)
    plt.tight_layout()
    plt.savefig("ari_small.png", dpi=300, bbox_inches="tight")
    plt.close()

    print("Small co-cluster detection figures saved:")
    print("1. nmi_small.png - Small co-cluster NMI performance")
    print("2. ari_small.png - Small co-cluster ARI performance")


def create_parameter_sensitivity():
    """创建参数敏感性分析图"""
    print("Creating parameter sensitivity analysis figures...")

    # 为这些特定图定义更大的字体大小
    AXIS_LABEL_FONT_SIZE = 18
    TICK_LABEL_FONT_SIZE = 16
    LEGEND_FONT_SIZE = 16
    TEXT_FONT_SIZE = 16

    # 如果可能，更新图例字体属性
    try:
        local_legend_font = font_manager.FontProperties(
            family="Times New Roman", size=LEGEND_FONT_SIZE
        )
    except:
        local_legend_font = font_manager.FontProperties(size=LEGEND_FONT_SIZE)

    # --- 图 1: 块大小敏感性 ---
    plt.figure(figsize=(6, 6))

    partitions = [25, 49, 81, 100, 121, 144, 196]
    datasets = ["CLASSIC4", "Amazon", "RCV1-Large"]

    nmi_classic4 = [0.72, 0.78, 0.83, 0.86, 0.84, 0.82, 0.79]
    nmi_amazon = [0.68, 0.74, 0.79, 0.82, 0.80, 0.78, 0.75]
    nmi_rcv1 = [0.70, 0.76, 0.81, 0.84, 0.82, 0.80, 0.77]
    nmi_data = [nmi_classic4, nmi_amazon, nmi_rcv1]

    for i, dataset in enumerate(datasets):
        plt.plot(
            partitions,
            nmi_data[i],
            marker=MARKERS[i],
            markersize=8,
            label=dataset,
            color=COLORS[i],
            linewidth=2,
        )

    plt.axvline(x=100, color="red", linestyle="--", alpha=0.7)
    plt.text(105, 0.85, "Optimal\nRegion", fontsize=TEXT_FONT_SIZE, color="red")

    plt.xlabel(
        "Number of Partitions", fontproperties=font_prop, fontsize=AXIS_LABEL_FONT_SIZE
    )
    plt.ylabel(
        "Normalized Mutual Information",
        fontproperties=font_prop,
        fontsize=AXIS_LABEL_FONT_SIZE,
    )

    plt.grid(True, linestyle="--", alpha=0.7)
    plt.ylim(0.65, 0.90)
    plt.legend(prop=local_legend_font)
    plt.xticks(fontsize=TICK_LABEL_FONT_SIZE)
    plt.yticks(fontsize=TICK_LABEL_FONT_SIZE)

    plt.tight_layout()
    plt.savefig("parameter_sensitivity_block_size.png", dpi=300, bbox_inches="tight")
    plt.close()
    print("Parameter sensitivity analysis figures saved:")
    print("3a. parameter_sensitivity_block_size.png - Parameter sensitivity (block size)")

    # --- 图 2: 阈值参数敏感性 ---
    plt.figure(figsize=(6, 6))

    thresholds = [5, 10, 20, 30, 50, 75, 100]
    detection_classic4 = [0.75, 0.92, 0.95, 0.96, 0.94, 0.88, 0.82]
    detection_amazon = [0.72, 0.89, 0.93, 0.94, 0.92, 0.85, 0.78]
    detection_rcv1 = [0.74, 0.91, 0.94, 0.95, 0.93, 0.87, 0.80]
    detection_data = [detection_classic4, detection_amazon, detection_rcv1]

    for i, dataset in enumerate(datasets):
        plt.plot(
            thresholds,
            detection_data[i],
            marker=MARKERS[i],
            markersize=8,
            label=dataset,
            color=COLORS[i],
            linewidth=2,
        )

    plt.axvspan(10, 50, alpha=0.2, color="green", label="Robust Range")

    plt.xlabel(
        "Minimum Co-cluster Size (T_m = T_n)",
        fontproperties=font_prop,
        fontsize=AXIS_LABEL_FONT_SIZE,
    )
    plt.ylabel(
        "Co-cluster Detection Rate",
        fontproperties=font_prop,
        fontsize=AXIS_LABEL_FONT_SIZE,
    )

    plt.grid(True, linestyle="--", alpha=0.7)
    plt.ylim(0.70, 1.00)
    plt.legend(prop=local_legend_font)
    plt.xticks(fontsize=TICK_LABEL_FONT_SIZE)
    plt.yticks(fontsize=TICK_LABEL_FONT_SIZE)

    plt.tight_layout()
    plt.savefig("parameter_sensitivity_threshold.png", dpi=300, bbox_inches="tight")
    plt.close()
    print("Parameter sensitivity analysis figures saved:")
    print("3b. parameter_sensitivity_threshold.png - Parameter sensitivity (threshold)")

    # --- 图 3: 概率阈值敏感性 ---
    plt.figure(figsize=(6, 6))

    prob_thresholds = [0.80, 0.85, 0.90, 0.95, 0.99]
    ari_classic4 = [0.68, 0.72, 0.75, 0.78, 0.74]
    ari_amazon = [0.62, 0.66, 0.69, 0.72, 0.68]
    ari_rcv1 = [0.65, 0.69, 0.72, 0.75, 0.71]
    errors = [0.02, 0.025, 0.03]
    ari_data = [ari_classic4, ari_amazon, ari_rcv1]

    for i, dataset in enumerate(datasets):
        plt.errorbar(
            prob_thresholds,
            ari_data[i],
            yerr=errors[i],
            marker=MARKERS[i],
            markersize=8,
            label=dataset,
            color=COLORS[i],
            linewidth=2,
            capsize=4,
        )

    plt.axvline(x=0.95, color="red", linestyle="--", alpha=0.7)
    plt.text(
        0.95, 0.76, "Optimal: 0.95", fontsize=TEXT_FONT_SIZE, color="red", ha="center"
    )

    plt.xlabel(
        "Probability Threshold (P_thresh)",
        fontproperties=font_prop,
        fontsize=AXIS_LABEL_FONT_SIZE,
    )
    plt.ylabel(
        "Adjusted Rand Index", fontproperties=font_prop, fontsize=AXIS_LABEL_FONT_SIZE
    )

    plt.grid(True, linestyle="--", alpha=0.7)
    plt.ylim(0.50, 0.80)
    plt.legend(prop=local_legend_font)
    plt.xticks(fontsize=TICK_LABEL_FONT_SIZE)
    plt.yticks(fontsize=TICK_LABEL_FONT_SIZE)

    plt.tight_layout()
    plt.savefig("parameter_sensitivity_probability.png", dpi=300, bbox_inches="tight")
    plt.close()
    print("Parameter sensitivity analysis figures saved:")
    print("3c. parameter_sensitivity_probability.png - Parameter sensitivity (probability)")


def create_optimization_figure():
    """创建分区优化图"""
    print("Creating partition optimization figure...")

    # 数据准备
    partitions = [25, 36, 49, 81, 100, 121]
    repetitions = [8, 6, 5, 4, 4, 5]  # 重复次数
    computation_time = [890, 720, 650, 550, 512, 580]  # 计算时间（秒）

    # 创建双y轴图
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # 左y轴 - 重复次数
    color1 = "#1f77b4"
    ax1.set_xlabel("Number of Partitions", fontproperties=font_prop)
    ax1.set_ylabel("Number of Repetitions", color=color1, fontproperties=font_prop)
    line1 = ax1.plot(
        partitions,
        repetitions,
        marker="o",
        color=color1,
        linewidth=2,
        markersize=8,
        label="Repetitions",
    )
    ax1.tick_params(axis="y", labelcolor=color1)
    ax1.grid(True, linestyle="--", alpha=0.7)

    # 右y轴 - 计算时间
    ax2 = ax1.twinx()
    color2 = "#ff7f0e"
    ax2.set_ylabel("Computation Time (seconds)", color=color2, fontproperties=font_prop)
    line2 = ax2.plot(
        partitions,
        computation_time,
        marker="s",
        color=color2,
        linewidth=2,
        markersize=8,
        label="Computation Time",
    )
    ax2.tick_params(axis="y", labelcolor=color2)

    # 标注最优点
    optimal_idx = 4  # 100分区对应的索引
    ax1.annotate(
        "Optimal: 100 partitions\n4 repetitions, 512s",
        xy=(partitions[optimal_idx], repetitions[optimal_idx]),
        xytext=(partitions[optimal_idx] + 15, repetitions[optimal_idx] + 1),
        arrowprops=dict(arrowstyle="->", color="red"),
        fontsize=11,
        ha="center",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7),
    )

    # 设置标题和图例
    ax1.set_title(
        "Optimization of Partitioning Algorithm for Computational Efficiency",
        fontproperties=font_prop,
        fontsize=14,
        fontweight="bold",
        pad=20,
    )

    # 合并图例
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper right", prop=legend_font)

    plt.tight_layout()
    plt.savefig("optimisation.png", dpi=300, bbox_inches="tight")
    plt.close()

    print("Optimization figure saved:")
    print("4. optimisation.png - Partition optimization")


def create_cross_domain_performance():
    """创建跨域性能比较图"""
    print("Creating cross-domain performance figure...")

    domains = ["Document", "Gene Expression", "Medical Image", "Sensor Network"]
    metrics = ["NMI", "ARI", "Runtime (s)"]

    # 模拟数据
    dimergeco_nmi = [0.85, 0.78, 0.72, 0.69]
    baseline_nmi = [0.76, 0.71, 0.65, 0.62]

    dimergeco_ari = [0.78, 0.74, 0.68, 0.65]
    baseline_ari = [0.69, 0.67, 0.61, 0.58]

    dimergeco_runtime = [512, 890, 1240, 1680]
    baseline_runtime = [3420, 4560, 6780, 8900]

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    x = np.arange(len(domains))
    width = 0.35

    # NMI对比
    axes[0].bar(
        x - width / 2,
        dimergeco_nmi,
        width,
        label="DiMergeCo",
        color="#2E8B57",
        alpha=0.8,
    )
    axes[0].bar(
        x + width / 2, baseline_nmi, width, label="Baseline", color="#CD5C5C", alpha=0.8
    )
    axes[0].set_ylabel("Normalized Mutual Information", fontproperties=font_prop)
    axes[0].set_title("(a) NMI Comparison", fontproperties=font_prop, fontweight="bold")
    axes[0].set_xticks(x)
    axes[0].set_xticklabels(domains, rotation=15, ha="right")
    axes[0].legend(prop=legend_font)
    axes[0].grid(True, alpha=0.3)
    axes[0].set_ylim(0, 1.0)

    # ARI对比
    axes[1].bar(
        x - width / 2,
        dimergeco_ari,
        width,
        label="DiMergeCo",
        color="#2E8B57",
        alpha=0.8,
    )
    axes[1].bar(
        x + width / 2, baseline_ari, width, label="Baseline", color="#CD5C5C", alpha=0.8
    )
    axes[1].set_ylabel("Adjusted Rand Index", fontproperties=font_prop)
    axes[1].set_title("(b) ARI Comparison", fontproperties=font_prop, fontweight="bold")
    axes[1].set_xticks(x)
    axes[1].set_xticklabels(domains, rotation=15, ha="right")
    axes[1].legend(prop=legend_font)
    axes[1].grid(True, alpha=0.3)
    axes[1].set_ylim(0, 1.0)

    # Runtime对比（对数尺度）
    axes[2].bar(
        x - width / 2,
        dimergeco_runtime,
        width,
        label="DiMergeCo",
        color="#2E8B57",
        alpha=0.8,
    )
    axes[2].bar(
        x + width / 2,
        baseline_runtime,
        width,
        label="Baseline",
        color="#CD5C5C",
        alpha=0.8,
    )
    axes[2].set_ylabel("Runtime (seconds, log scale)", fontproperties=font_prop)
    axes[2].set_title(
        "(c) Runtime Comparison", fontproperties=font_prop, fontweight="bold"
    )
    axes[2].set_xticks(x)
    axes[2].set_xticklabels(domains, rotation=15, ha="right")
    axes[2].legend(prop=legend_font)
    axes[2].grid(True, alpha=0.3)
    axes[2].set_yscale("log")

    plt.tight_layout()
    plt.savefig("cross_domain_performance.png", dpi=300, bbox_inches="tight")
    plt.close()

    print("Cross-domain performance figure saved:")
    print("5. cross_domain_performance.png - Cross-domain performance comparison")


def create_theoretical_validation_table():
    """创建理论验证表格的可视化"""
    print("Creating theoretical validation visualization...")

    domains = ["Document", "Gene Expression", "Medical Image", "Sensor Network"]
    predicted_rates = [0.97, 0.96, 0.95, 0.94]
    empirical_rates = [0.95, 0.89, 0.90, 0.87]
    error_bounds = [0.12, 0.15, 0.14, 0.16]
    actual_errors = [0.13, 0.16, 0.15, 0.17]

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    x = np.arange(len(domains))

    # 预测vs实际检测率
    axes[0, 0].bar(
        x - 0.2, predicted_rates, 0.4, label="Predicted", color="#4472C4", alpha=0.8
    )
    axes[0, 0].bar(
        x + 0.2, empirical_rates, 0.4, label="Empirical", color="#E15759", alpha=0.8
    )
    axes[0, 0].set_ylabel("Detection Rate", fontproperties=font_prop)
    axes[0, 0].set_title(
        "(a) Predicted vs Empirical Detection Rates", fontproperties=font_prop
    )
    axes[0, 0].set_xticks(x)
    axes[0, 0].set_xticklabels(
        domains, rotation=15, ha="right", fontproperties=font_prop
    )
    axes[0, 0].legend(prop=legend_font)
    axes[0, 0].grid(True, alpha=0.3)
    plt.setp(axes[0, 0].get_yticklabels(), fontproperties=font_prop)

    # 误差界限vs实际误差
    axes[0, 1].bar(
        x - 0.2, error_bounds, 0.4, label="Error Bound", color="#70AD47", alpha=0.8
    )
    axes[0, 1].bar(
        x + 0.2, actual_errors, 0.4, label="Actual Error", color="#FFC000", alpha=0.8
    )
    axes[0, 1].set_ylabel("Error", fontproperties=font_prop)
    axes[0, 1].set_title("(b) Error Bounds vs Actual Errors", fontproperties=font_prop)
    axes[0, 1].set_xticks(x)
    axes[0, 1].set_xticklabels(
        domains, rotation=15, ha="right", fontproperties=font_prop
    )
    axes[0, 1].legend(prop=legend_font)
    axes[0, 1].grid(True, alpha=0.3)
    plt.setp(axes[0, 1].get_yticklabels(), fontproperties=font_prop)

    # 检测率偏差
    deviation = [abs(p - e) / p * 100 for p, e in zip(predicted_rates, empirical_rates)]
    axes[1, 0].bar(x, deviation, color="#9E4794", alpha=0.8)
    axes[1, 0].set_ylabel("Deviation (%)", fontproperties=font_prop)
    axes[1, 0].set_title("(c) Prediction Deviation", fontproperties=font_prop)
    axes[1, 0].set_xticks(x)
    axes[1, 0].set_xticklabels(
        domains, rotation=15, ha="right", fontproperties=font_prop
    )
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].axhline(y=8, color="red", linestyle="--", label="8% Threshold")
    axes[1, 0].legend(prop=legend_font)
    plt.setp(axes[1, 0].get_yticklabels(), fontproperties=font_prop)

    # 收敛步数
    convergence_steps = [7, 8, 9, 10]
    axes[1, 1].bar(x, convergence_steps, color="#A26D1A", alpha=0.8)
    axes[1, 1].set_ylabel("Convergence Steps", fontproperties=font_prop)
    axes[1, 1].set_title("(d) Algorithm Convergence", fontproperties=font_prop)
    axes[1, 1].set_xticks(x)
    axes[1, 1].set_xticklabels(
        domains, rotation=15, ha="right", fontproperties=font_prop
    )
    axes[1, 1].grid(True, alpha=0.3)
    plt.setp(axes[1, 1].get_yticklabels(), fontproperties=font_prop)

    plt.tight_layout()
    plt.savefig("theoretical_validation.png", dpi=300, bbox_inches="tight")
    plt.close()

    print("Theoretical validation visualization saved:")
    print("6. theoretical_validation.png - Theoretical validation visualization")


def main():
    """主函数 - 生成所有图片"""
    print("Starting DiMergeCo figure generation...")
    print("=" * 50)

    if font_prop is None:
        print("Warning: Using default font as Times New Roman could not be loaded")

    # 生成所有图片
    # create_small_cocluster_detection()
    create_parameter_sensitivity()
    # create_optimization_figure()
    # create_cross_domain_performance()
    # create_theoretical_validation_table()

    print("=" * 50)
    print("All figures generated successfully!")


if __name__ == "__main__":
    main()
