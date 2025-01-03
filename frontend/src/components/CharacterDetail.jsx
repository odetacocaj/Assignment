import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

function CharacterDetail() {
  const { id } = useParams();
  const [character, setCharacter] = useState(null);

  useEffect(() => {
    fetch(`https://assignment-h2sh.onrender.com/api/characters/${id}`)
      .then((response) => response.json())
      .then((data) => setCharacter(data));
  }, [id]);
  if (!character) {
    return <div>Loading...</div>;
  }

  return (
    <div className="character-detail">
      <img src={character.image_url} alt={character.name} />
      <h1>{character.name}</h1>
      <p>
        <strong>Played by:</strong> {character.actor}
      </p>
      <p>
        <strong>Played in:</strong> {character.description || "No details available."}
      </p>
    </div>
  );
}

export default CharacterDetail;
