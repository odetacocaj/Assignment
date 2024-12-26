import { Link } from "react-router-dom";

const Header = () => {
  return (
    <header className="header">
      <Link className="title" to="/">
        <h1 className="title">Vahalla Characters</h1>
      </Link>
    </header>
  );
};

export default Header;
