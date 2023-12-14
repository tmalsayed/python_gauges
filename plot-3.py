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

        # Create different Plotly graphs
        scatter_plot_div = self.create_plot_div()
        gauge_indicator_div = self.create_gauge_indicator()
        number_delta_indicator_div = self.create_number_delta_indicator()
        indicator_plot_div_1 = self.create_indicator_plot_div(42, 'Indicator 1')
        line_indicator = self.create_plot_line_2()
        numbers_1 = self.numbers()
        guage_2 = self.create_guage_2()
        down_arrow_1 = self.down_arrow()
        # Set up QWebEngineViews in containers
        self.setup_container(self.plotContainer, scatter_plot_div)
        self.setup_container(self.plotContainer_2, gauge_indicator_div)
        self.setup_container(self.plotContainer_3, number_delta_indicator_div)
        self.setup_container(self.plotContainer_4, indicator_plot_div_1)
        self.setup_container(self.plotContainer_5, line_indicator)
        self.setup_container(self.plotContainer_6, numbers_1)
        self.setup_container(self.plotContainer_7, guage_2)
        self.setup_container(self.plotContainer_8, down_arrow_1)


    def create_plot_div(self):
        # Define the scatter graph using Plotly
        fig = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[4, 5, 6])])
        # Save the figure to a div
        return plot(fig, output_type='div', include_plotlyjs='cdn')



    def create_indicator_plot_div(self, value, title):
        # Define an indicator graph using Plotly
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=value,
            title={'text': title},
            domain={'x': [0, 1], 'y': [0, 1]}
        ))
        # Save the figure to a div
        return plot(fig, output_type='div', include_plotlyjs='cdn')

    def create_gauge_indicator(self):
        # Define the gauge indicator using Plotly
        fig = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=420,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Speed", 'font': {'size': 24}},
            delta={'reference': 400, 'increasing': {'color': "RebeccaPurple"}},
            gauge={
                'axis': {'range': [None, 500], 'tickwidth': 1, 'tickcolor': "darkblue"},
                'bar': {'color': "darkblue"},
                'bgcolor': "white",
                'borderwidth': 2,
                'bordercolor': "gray",
                'steps': [
                    {'range': [0, 250], 'color': 'cyan'},
                    {'range': [250, 400], 'color': 'royalblue'}],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 490}
            }
        ))
        fig.update_layout(paper_bgcolor="lavender", font={'color': "darkblue", 'family': "Arial"})
        return plot(fig, output_type='div', include_plotlyjs='cdn')

    def create_number_delta_indicator(self):
        # Define the number+delta indicator using Plotly
        fig = go.Figure(go.Indicator(
            mode="number+delta",
            value=492,
            delta={"reference": 512, "valueformat": ".0f"},
            title={"text": "Users online"},
            domain={'y': [0, 1], 'x': [0.25, 0.75]}
        ))

        fig.add_trace(go.Scatter(
            y=[325, 324, 405, 400, 424, 404, 417, 432, 419, 394, 410, 426, 413, 419, 404, 408, 401, 377, 368, 361, 356, 359, 375, 397, 394, 418, 437, 450, 430, 442, 424, 443, 420, 418, 423, 423, 426, 440, 437, 436, 447, 460, 478, 472, 450, 456, 436, 418, 429, 412, 429, 442, 464, 447, 434, 457, 474, 480, 499, 497, 480, 502, 512, 492]
        ))
        fig.update_layout(xaxis={'range': [0, 62]})
        return plot(fig, output_type='div', include_plotlyjs='cdn')

    def create_plot_line_2(self):
        fig = go.Figure(go.Indicator(
            mode = "number+gauge+delta",
            gauge = {'shape': "bullet"},
            delta = {'reference': 300},
            value = 220,
            domain = {'x': [0.1, 1], 'y': [0.2, 0.9]},
            title = {'text': ""}))

        # Update layout for title positioning
        fig.update_layout(
            title = {
                'text': "Avg order size",
                'y': 0.9,  # Sets the title position near the top of the plot
                'x': 0.5,  # Centers the title
                'xanchor': 'center',
                'yanchor': 'top'
            }
        )
        return plot(fig, output_type='div', include_plotlyjs='cdn')
    
    def create_guage_2(self):
        fig = go.Figure(go.Indicator(
            domain = {'x': [0, 1], 'y': [0, 1]},
            value = 450,
            mode = "gauge+number+delta",
            title = {'text': "Speed"},
            delta = {'reference': 380},
            gauge = {'axis': {'range': [None, 500]},
                    'steps' : [
                        {'range': [0, 250], 'color': "lightgray"},
                        {'range': [250, 400], 'color': "gray"}],
                    'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}}))
        return plot(fig, output_type='div', include_plotlyjs='cdn')

    def numbers(self):
        fig = go.Figure(go.Indicator(
            mode = "number+delta",
            value = 400,
            number = {'prefix': "$"},
            delta = {'position': "top", 'reference': 320},
            domain = {'x': [0, 1], 'y': [0, 1]}))

        fig.update_layout(paper_bgcolor = "lightgray")
        return plot(fig, output_type='div', include_plotlyjs='cdn')

    def down_arrow(self):
        # Create a figure with an indicator
        fig = go.Figure(go.Indicator(
            mode = "number+delta+gauge",
            value = 400,
            number = {'prefix': "$"},
            delta = {'position': "top", 'reference': 320},
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Speed"}
        ))

        # Update layout for the figure
        fig.update_layout(
            paper_bgcolor = "lightgray",
            grid = {'rows': 2, 'columns': 2, 'pattern': "independent"}
        )

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


# import sys
# from PyQt5 import QtWidgets, uic, QtCore
# from PyQt5.QtWebEngineWidgets import QWebEngineView
# import plotly.graph_objects as go
# from plotly.offline import plot

# class MainWindow(QtWidgets.QMainWindow):
#     def __init__(self):
#         super().__init__()
#         # Load the UI file directly
#         uic.loadUi('MainWindow.ui', self)

#         # Create different Plotly graphs
#         scatter_plot_div = self.create_plot_div()
#         indicator_plot_div_1 = self.create_indicator_plot_div(42, 'Indicator 1')
#         indicator_plot_div_2 = self.create_indicator_plot_div(73, 'Indicator 2')
#         indicator_plot_div_3 = self.create_indicator_plot_div(56, 'Indicator 3')

#         # Set up QWebEngineViews in containers
#         self.setup_container(self.plotContainer, scatter_plot_div)
#         self.setup_container(self.plotContainer_2, indicator_plot_div_1)
#         self.setup_container(self.plotContainer_3, indicator_plot_div_2)
#         self.setup_container(self.plotContainer_4, indicator_plot_div_3)

#     def create_plot_div(self):
#         # Define the scatter graph using Plotly
#         fig = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[4, 5, 6])])
#         # Save the figure to a div
#         return plot(fig, output_type='div', include_plotlyjs='cdn')

#     def create_indicator_plot_div(self, value, title):
#         # Define an indicator graph using Plotly
#         fig = go.Figure(go.Indicator(
#             mode="gauge+number",
#             value=value,
#             title={'text': title},
#             domain={'x': [0, 1], 'y': [0, 1]}
#         ))
#         # Save the figure to a div
#         return plot(fig, output_type='div', include_plotlyjs='cdn')

#     def setup_container(self, container, plot_div):
#         # Ensure the container has a layout
#         if not container.layout():
#             container.setLayout(QtWidgets.QVBoxLayout())
#         # Create a QWebEngineView to display the Plotly graph
#         view = QWebEngineView()
#         view.setHtml(plot_div)
#         # Add the view to the container's layout
#         container.layout().addWidget(view)

# if __name__ == "__main__":
#     # IMPORTANT: Set the attribute before creating the QApplication
#     QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)

#     # Initialize the PyQt5 application
#     app = QtWidgets.QApplication(sys.argv)

#     # Create the main window and show it
#     window = MainWindow()
#     window.show()

#     # Start the event loop
#     sys.exit(app.exec_())
