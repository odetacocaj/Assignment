import { useEffect, useState } from "react";
import CharacterCard from "./CharacterCard";

function CharacterList() {
  const [characters, setCharacters] = useState([]);
  const [searchQuery, setSearchQuery] = useState("");

  useEffect(() => {
    fetchCharacters();
  }, []);

  const fetchCharacters = async (query = "") => {
    let url = "http://127.0.0.1:5000/api/characters";
    if (query) {
      url += `?search=${query}`;
    }

    try {
      const response = await fetch(url);
      const data = await response.json();
      setCharacters(data);
    } catch (error) {
      console.error("Error fetching characters:", error);
    }
  };

  
  const handleSearchChange = (e) => {
    const query = e.target.value;
    setSearchQuery(query); 
    fetchCharacters(query); 
  };

  return (
    <div className="character-list">
      <input
        type="text"
        value={searchQuery}
        onChange={handleSearchChange}
        placeholder="Search for characters..."
        className="search-bar"
      />
      <div className="card-container">
        {characters.map((character) => (
          <CharacterCard key={character.id} character={character} />
        ))}
      </div>
    </div>
  );
}

export default CharacterList;
