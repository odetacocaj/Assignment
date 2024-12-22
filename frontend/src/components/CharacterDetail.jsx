import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

function CharacterDetail() {
  const { id } = useParams();
  const [character, setCharacter] = useState(null);

  useEffect(() => {
    fetch(`http://127.0.0.1:5000/api/characters/${id}`)
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
        <strong>Actor:</strong> {character.actor}
      </p>
      <p>
        <strong>Details:</strong> {character.details || "No details available."}
      </p>
    </div>
  );
}

export default CharacterDetail;
