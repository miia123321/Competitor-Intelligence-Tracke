import plotly.graph_objs as go
from typing import List, Dict

def generate_trend_chart(events: List[Dict], title: str = "Competitor Trends") -> str:
    """Generate a simple trend chart and return as HTML div."""
    # For demo: count events by type
    type_counts = {}
    for event in events:
        t = event.get('type', 'Other')
        type_counts[t] = type_counts.get(t, 0) + 1
    data = [go.Bar(x=list(type_counts.keys()), y=list(type_counts.values()))]
    layout = go.Layout(title=title, xaxis=dict(title='Event Type'), yaxis=dict(title='Count'))
    fig = go.Figure(data=data, layout=layout)
    return fig.to_html(full_html=False)
