""" 
Description:

You are building a system that generates different types of charts:

Bar Chart

Line Chart

Pivot Table / Table Chart

The overall workflow for generating any chart is the same:

Load data from a data source (CSV, database, or API)

Process / aggregate data (e.g., sum, average, grouping)

Render chart (specific to chart type)

Export chart (image, PDF, or dashboard)

Only step 2 (processing) and step 3 (rendering) differ depending on the chart type.
"""
from abc import ABC,abstractmethod
class ChartGenerator(ABC):
    
    def generate_chart(self):
        self.load_data_from_db()
        self.clean_up_data()
        self.process_data()
        self.render_chart()
        self.save()

    def load_data_from_db(self):
        print("loading data from database....")

    def clean_up_data(self):
        print("cleaning data...")

    @abstractmethod
    def process_data(self):
        pass 

    @abstractmethod
    def render_chart(self):
        pass 

    def save(self):
        print("Saving report...")


class PivotTableGenerator(ChartGenerator):
    
    def process_data(self):
        print("processing data for pivot table")
    def render_chart(self):
        print("generating pivot table")


class BarChartGenerator(ChartGenerator):
   
    def process_data(self):
        print("processing data for bar chart")
    def render_chart(self):
        print("generating bar chart")


if __name__ == "__main__":
    
    charts = [
        BarChartGenerator(),
        PivotTableGenerator(),
       
    ]

    for i, chart in enumerate(charts, start=1):
        print(f"\n=== Generating Chart {i}: {chart.__class__.__name__} ===")
        chart.generate_chart()  # calls the template method

    # Simulate multiple runs for same chart type (like multiple datasets)
    print("\n=== Generating multiple Bar Charts ===")
    for dataset_number in range(1, 4):
        print(f"\nDataset {dataset_number}:")
        bar_chart = BarChartGenerator()
        bar_chart.generate_chart()
