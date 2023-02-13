import React from 'react';
import './Team.css';

const teamMembers = [
  { name: 'John Doe', position: 'Founder', image: require('./john-doe.jpg') },
  { name: 'Jane Doe', position: 'COO', image: require('./jane-doe.jpg') },
  { name: 'Bob Smith', position: 'CTO', image: require('./bob-smith.jpg') },
];

function Team() {
  return (
    <div className="Team">
      <h1 className="Team-header">Meet Our Team</h1>
      <div className="Team-members">
        {teamMembers.map(member => (
          <div className="Team-member">
            <img src={member.image} alt={`${member.name} headshot`} className="Team-member-image" />
            <h2 className="Team-member-name">{member.name}</h2>
            <p className="Team-member-position">{member.position}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Team;
