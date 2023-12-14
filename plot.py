import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWebEngineWidgets import QWebEngineView
import plotly.graph_objects as go
from plotly.offline import plot

# Set the rendering mode to 'browser' or 'iframe' depending on your needs
# (this line can be omitted if you're using the default renderer)
# pio.renderers.default = 'browser'

# Define the graph using Plotly
fig = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[4, 5, 6])])

# Save the figure to a temporary HTML file
plot_div = plot(fig, output_type='div', include_plotlyjs='cdn')

# IMPORTANT: Set the attribute before creating the QApplication
QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)

# Initialize the PyQt5 application
app = QtWidgets.QApplication(sys.argv)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a central widget
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        # Create a QVBoxLayout instance
        layout = QtWidgets.QVBoxLayout()
        central_widget.setLayout(layout)

        # Create a QWebEngineView to display the Plotly graph
        view = QWebEngineView()
        view.setHtml(plot_div)

        # Add the view to the layout
        layout.addWidget(view)

# Create the main window and show it
window = MainWindow()
window.show()

# Start the event loop
sys.exit(app.exec_())
