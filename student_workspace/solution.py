import numpy as np

class SalesAnalyzer:
    def __init__(self, sales_matrix: list):
        self.sales = np.array(sales_matrix)

    def total_sales_per_product(self):
        return self.sales.sum(axis=1).tolist()

    def total_sales_per_region(self):
        return self.sales.sum(axis=0).tolist()

    def best_selling_product(self):
        totals = self.sales.sum(axis=1)
        idx = np.argmax(totals)
        return int(idx), int(totals[idx])

    def normalize_sales(self):
        max_val = np.max(self.sales)
        if max_val == 0:
            return self.sales.tolist()
        normalized = self.sales / max_val
        return np.round(normalized, 2).tolist()