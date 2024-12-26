/* eslint-disable react/prop-types */
import { Link } from "react-router-dom";

// eslint-disable-next-line react/prop-types
function CharacterCard({ character }) {
  const defaultImage =
    "https://www.pngitem.com/pimgs/m/579-5798505_user-placeholder-svg-hd-png-download.png";

  return (
    <div className="card">
      <Link to={`/character/${character.id}`}>
        <div className="card-top">
          <img src={character.image_url || defaultImage} alt={character.name} />
        </div>
        <div className="card-bottom">
          <h3>{character.name}</h3>
          <p>Played by: {character.actor}</p>
        </div>
      </Link>
    </div>
  );
}

export default CharacterCard;
