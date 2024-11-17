import psutil
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation

# Constants
WARNING_THRESHOLD = 80  # Set RAM usage warning level in percentage

# Initialize data
x_data, y_data = [], []
time_step = 0

def get_ram_info():
    """Fetch RAM usage and detailed information."""
    memory_info = psutil.virtual_memory()
    swap_info = psutil.swap_memory()
    
    # Handle missing attributes
    cached = getattr(memory_info, 'cached', None)
    buffers = getattr(memory_info, 'buffers', None)
    
    return {
        "total": round(memory_info.total / (1024 ** 3), 2),
        "available": round(memory_info.available / (1024 ** 3), 2),
        "used": round(memory_info.used / (1024 ** 3), 2),
        "percent": memory_info.percent,
        "cached": round(cached / (1024 ** 3), 2) if cached else "N/A",
        "buffer": round(buffers / (1024 ** 3), 2) if buffers else "N/A",
        "swap_total": round(swap_info.total / (1024 ** 3), 2),
        "swap_used": round(swap_info.used / (1024 ** 3), 2),
        "swap_percent": swap_info.percent,
    }

def update_graph(frame):
    """Update the mini graph and display RAM info."""
    global time_step, x_data, y_data

    # Get current RAM usage
    ram_info = get_ram_info()
    usage_percent = ram_info["percent"]

    # Update data for graph
    x_data.append(time_step)
    y_data.append(usage_percent)
    if len(x_data) > 20:
        x_data.pop(0)
        y_data.pop(0)

    # Update graph
    ax.clear()
    ax.plot(x_data, y_data, color="blue", marker="o", label="RAM Usage (%)")
    ax.set_ylim(0, 100)
    if len(x_data) > 1:
        ax.set_xlim(max(0, x_data[0]), x_data[-1])
    else:
        ax.set_xlim(0, 1)
    ax.set_title("Real-Time RAM Usage")
    ax.legend(loc="upper left")
    ax.grid(True)

    # Update GUI labels
    total_label.config(text=f"Total RAM: {ram_info['total']} GB")
    used_label.config(text=f"Used RAM: {ram_info['used']} GB")
    available_label.config(text=f"Available RAM: {ram_info['available']} GB")
    percent_label.config(text=f"Usage: {usage_percent}%")
    cached_label.config(text=f"Cached: {ram_info['cached']} GB")
    buffer_label.config(text=f"Buffer: {ram_info['buffer']} GB")
    swap_label.config(
        text=f"Swap: {ram_info['swap_used']} GB / {ram_info['swap_total']} GB ({ram_info['swap_percent']}%)"
    )

    # Show warning if usage exceeds threshold
    if usage_percent >= WARNING_THRESHOLD:
        warning_label.config(text="⚠️ High RAM Usage!", fg="red")
    else:
        warning_label.config(text="RAM Usage Normal", fg="green")

    # Increment time step
    time_step += 1

# Create main Tkinter window
root = tk.Tk()
root.title("RAM Measuring Tool  v1.0.1  by 47cyber")
root.geometry("700x500")
root.resizable(False, False)

# Create UI components
frame_info = ttk.Frame(root, padding=10)
frame_info.pack(side=tk.TOP, fill=tk.X)

total_label = ttk.Label(frame_info, text="Total RAM: -- GB", font=("Arial", 12))
total_label.pack(anchor=tk.W)

used_label = ttk.Label(frame_info, text="Used RAM: -- GB", font=("Arial", 12))
used_label.pack(anchor=tk.W)

available_label = ttk.Label(frame_info, text="Available RAM: -- GB", font=("Arial", 12))
available_label.pack(anchor=tk.W)

percent_label = ttk.Label(frame_info, text="Usage: --%", font=("Arial", 12))
percent_label.pack(anchor=tk.W)

cached_label = ttk.Label(frame_info, text="Cached: -- GB", font=("Arial", 12))
cached_label.pack(anchor=tk.W)

buffer_label = ttk.Label(frame_info, text="Buffer: -- GB", font=("Arial", 12))
buffer_label.pack(anchor=tk.W)

swap_label = ttk.Label(frame_info, text="Swap: -- GB / -- GB (--%)", font=("Arial", 12))
swap_label.pack(anchor=tk.W)

# Use tk.Label for color customization
warning_label = tk.Label(frame_info, text="RAM Usage Normal", font=("Arial", 14))
warning_label.pack(anchor=tk.W)

# Matplotlib figure for mini graph
fig = Figure(figsize=(6, 3), dpi=100)
ax = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Animation for updating the graph
ani = FuncAnimation(fig, update_graph, interval=1000, cache_frame_data=False)

# Run the Tkinter main loop
root.mainloop()
