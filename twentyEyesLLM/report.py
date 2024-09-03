"""
This module provides methods to handle different output formats and extensions.
"""


class Report:
    """
    Class to generate reports from inference history.

    Attributes:
        aggregated_history (dict): Aggregated history of inferences by date.
        category_count (dict): Count of inferences per category.
    """

    def __init__(self, history: dict) -> None:
        """
        Initialize the Report object with the given history.

        Args:
            history (dict): The history of inferences.
        """
        self.aggregated_history = {}
        self.category_count = {"WORK": 0, "STUDY": 0, "FUN": 0, "NSFW": 0, "OTHER": 0}

        for inference in history["inferences"]:
            self._calculate_category(inference["category"])
            datetime_str = inference["datetime"].split("T")[0]

            if datetime_str not in self.aggregated_history:
                self.aggregated_history[datetime_str] = []

            self.aggregated_history[datetime_str].append(inference)

    def _calculate_category(self, category: str) -> None:
        """
        Update the count of the given category.

        Args:
            category (str): The category to update.
        """
        if category in self.category_count:
            self.category_count[category] += 1

    def to_markdown(self) -> str:
        """
        Generate a markdown report from the aggregated history.

        Returns:
            str: The generated markdown report.
        """
        md = "# Activities Report\n\n##\n\n## History\n\n"

        for date, inferences in self.aggregated_history.items():
            md += f"### {date}\n\n"

            for inference in inferences:
                time_str = inference["datetime"].split("T")[1][0:5]
                md += f'**{time_str}:** {inference["content"]}\n\n'

        md += "## Summarized activities by category\n\n"
        total_count = sum(self.category_count.values())

        percentages = {
            category: (count / total_count) * 100 if total_count > 0 else 0
            for category, count in self.category_count.items()
        }

        for category, percentage in percentages.items():
            md += f"- {category}: **{percentage:.0f}%**\n"

        return md
