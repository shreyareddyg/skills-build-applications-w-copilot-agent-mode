import React, { useState, useEffect } from 'react';

function Teams() {
  const [teams, setTeams] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`;

  useEffect(() => {
    console.log('Fetching teams from:', apiUrl);
    fetch(apiUrl)
      .then(response => response.json())
      .then(data => {
        console.log('Teams data fetched:', data);
        const results = Array.isArray(data) ? data : (data.results || []);
        setTeams(results);
        setLoading(false);
      })
      .catch(err => {
        console.error('Error fetching teams:', err);
        setError(err.message);
        setLoading(false);
      });
  }, [apiUrl]);

  if (loading) return <div className="text-center"><div className="spinner-border" role="status"></div></div>;
  if (error) return <div className="alert alert-danger">Error: {error}</div>;

  return (
    <div>
      <h2 className="mb-4">Teams</h2>
      <div className="row">
        {teams.map((team, index) => (
          <div key={team.id || index} className="col-md-6 mb-4">
            <div className="card">
              <div className="card-header bg-dark text-white">
                <h5 className="card-title mb-0">{team.name}</h5>
              </div>
              <div className="card-body">
                <h6>Members:</h6>
                <ul className="list-group list-group-flush">
                  {(team.members || []).map((member, idx) => (
                    <li key={idx} className="list-group-item">{member}</li>
                  ))}
                </ul>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Teams;
