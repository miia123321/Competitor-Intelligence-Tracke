import React, { useEffect, useState } from 'react';

function Dashboard() {
  const [competitors, setCompetitors] = useState([]);
  const [events, setEvents] = useState([]);
  const [trendChartHtml, setTrendChartHtml] = useState('');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('/competitors')
      .then(res => res.json())
      .then(data => setCompetitors(data));
    fetch('/events')
      .then(res => res.json())
      .then(data => {
        setEvents(data.events);
        setTrendChartHtml(data.trend_chart_html);
        setLoading(false);
      });
  }, []);

  return (
    <div>
      <h1>CompetiScan Dashboard</h1>
      <h2>Competitors</h2>
      <ul>
        {competitors.map(c => (
          <li key={c.id}>{c.name} (<a href={c.website} target="_blank" rel="noopener noreferrer">Website</a>)</li>
        ))}
      </ul>
      <h2>Recent Events</h2>
      <ul>
        {events.map(e => (
          <li key={e.id}>{e.headline} <span style={{color:'#888'}}>[{e.type}]</span></li>
        ))}
      </ul>
      <h2>Trend Chart</h2>
      <div dangerouslySetInnerHTML={{__html: trendChartHtml}} />
      {loading && <p>Loading...</p>}
    </div>
  );
}

export default Dashboard;
