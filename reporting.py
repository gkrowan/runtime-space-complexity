"""
Plot generation and markdown reporting.
"""

import matplotlib.pyplot as plt


def plot_runtime(results):
    """
    Plot runtime vs input size.
    """
    for name, data in results.items():
        plt.plot(data["sizes"], data["runtimes"], label=name)

    plt.title("Runtime Scaling")
    plt.xlabel("Number of Ticks")
    plt.ylabel("Runtime (seconds)")
    plt.legend()
    plt.savefig("runtime_scaling.png")
    plt.clf()


def plot_memory(results):
    """
    Plot memory usage vs input size.
    """
    for name, data in results.items():
        plt.plot(data["sizes"], data["memory"], label=name)

    plt.title("Memory Usage Scaling")
    plt.xlabel("Number of Ticks")
    plt.ylabel("Peak Memory (MB)")
    plt.legend()
    plt.savefig("memory_scaling.png")
    plt.clf()

def results_table(results, output_path="results_table.md"):
    """
    Generate markdown table of results, save to file.
    """
    headers = ["Strategy", "Input Size", "Runtime (s)", "Memory (MB)"]
    table = ["| " + " | ".join(headers) + " |", "|---" * len(headers) + "|"]

    for name, data in results.items():
        for size, runtime, memory in zip(data["sizes"], data["runtimes"], data["memory"]):
            row = f"| {name} | {size} | {runtime:.6f} | {memory:.2f} |"
            table.append(row)

    table_md = "\n".join(table)

    with open(output_path, "w") as f:
        f.write(table_md)

    return table_md