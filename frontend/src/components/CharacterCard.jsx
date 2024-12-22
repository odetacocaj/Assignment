/* eslint-disable react/prop-types */
import { Link } from "react-router-dom";

// eslint-disable-next-line react/prop-types
function CharacterCard({ character }) {
  return (
    <div className="card">
      <Link to={`/character/${character.id}`}>
        <div className="card-top">
          <img src={character.image_url} alt={character.name} />
        </div>
        <div className="card-bottom">
          <h3>{character.name}</h3>
          <p>Played by:{character.actor}</p>
        </div>
      </Link>
    </div>
  );
}

export default CharacterCard;
