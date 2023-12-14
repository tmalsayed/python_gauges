import sys
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWebEngineWidgets import QWebEngineView
import plotly.graph_objects as go
from plotly.offline import plot

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Load the UI file directly
        uic.loadUi('MainWindow.ui', self)

        # Create the Plotly graph once
        plot_div = self.create_plot_div()

        # Set up QWebEngineViews in containers
        self.setup_container(self.plotContainer, plot_div)
        self.setup_container(self.plotContainer_2, plot_div)
        self.setup_container(self.plotContainer_3, plot_div)
        self.setup_container(self.plotContainer_4, plot_div)

    def create_plot_div(self):
        # Define the graph using Plotly
        fig = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[4, 5, 6])])
        # Save the figure to a div
        return plot(fig, output_type='div', include_plotlyjs='cdn')

    def setup_container(self, container, plot_div):
        # Ensure the container has a layout
        if not container.layout():
            container.setLayout(QtWidgets.QVBoxLayout())
        # Create a QWebEngineView to display the Plotly graph
        view = QWebEngineView()
        view.setHtml(plot_div)
        # Add the view to the container's layout
        container.layout().addWidget(view)

if __name__ == "__main__":
    # IMPORTANT: Set the attribute before creating the QApplication
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)

    # Initialize the PyQt5 application
    app = QtWidgets.QApplication(sys.argv)

    # Create the main window and show it
    window = MainWindow()
    window.show()

    # Start the event loop
    sys.exit(app.exec_())
