import matplotlib.pyplot as plt
import numpy as np

def plot_dashboard():
    # Data for bar chart
    years = ["2023", "2024", "2025"]
    revenue = [3, 8, 15]
    profit = [2, 6, 12]
    x = np.arange(len(years))

    # Create figure and subplots
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    fig.suptitle("Opportunities in the Data Economy", fontsize=16, fontweight='bold', color='blue')
    
    # Bar chart
    axes[0].bar(x - 0.2, revenue, 0.4, label="Revenue", color='royalblue')
    axes[0].bar(x + 0.2, profit, 0.4, label="Profit", color='navy')
    axes[0].set_xticks(x)
    axes[0].set_xticklabels(years)
    axes[0].set_ylabel("Value")
    axes[0].set_title("Revenue vs Profit Over Years")
    axes[0].legend()
    
    # Pie chart
    labels = ["Data-Driven Decision Making", "Market Expansion", "New Revenue Streams", "Operational Efficiency"]
    sizes = [25, 25, 25, 25]
    colors = ["royalblue", "navy", "lightblue", "steelblue"]
    
    axes[1].pie(sizes, labels=labels, autopct='%1.0f%%', colors=colors, startangle=140)
    axes[1].set_title("Key Opportunities")
    
    plt.tight_layout()
    plt.show()

plot_dashboard()