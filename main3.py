import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd

# Завдання 1

# np.random.seed(0)
# x = np.linspace(-10, 10, 100)
# y = np.sin(x)
# z = np.cos(y)

# fig = go.Figure(data=[go.Scatter3d(
#     x=x,
#     y=y,
#     z=z,
#     mode='lines',
#     line=dict(color='blue', width=4)
# )])
# fig.update_layout(
#     title='3D-Лінійна діаграма',
#     scene=dict(
#         xaxis_title='X',
#         yaxis_title='Y',
#         zaxis_title='Z'
#     ),
#     width=700,
#     height=700
# )
# fig.show()


# Завдання 2

# np.random.seed(42)
# x = np.random.normal(0, 1, 1000)
# y = np.random.normal(0, 1, 1000)
# z = np.random.normal(0, 1, 1000)

# fig = go.Figure(
#     data=[
#         go.Histogram3d(
#             x=x,
#             y=y,
#             z=z,
#             colorscale='Blues'
#         )
#     ]
# )

# fig.update_layout(
#     title='3D-гістограма випадкових даних',
#     scene=dict(
#         xaxis_title='Вісь X',
#         yaxis_title='Вісь Y',
#         zaxis_title='Вісь Z'
#     )
# )

# fig.show()