import { BrowserRouter, Route, Routes } from "react-router-dom";
import CharacterList from "./components/CharactersList";
import CharacterDetail from "./components/CharacterDetail";
import Header from "./components/Header";
import Footer from "./components/Footer";
import "./App.css";

function App() {
  return (
    <>
      <BrowserRouter>
        <Header />
        <div className="app">
          <main className="main-content">
            <Routes>
              <Route path="/" element={<CharacterList />} />
              <Route path="/character/:id" element={<CharacterDetail />} />
            </Routes>
          </main>
        </div>
        <Footer />
      </BrowserRouter>
    </>
  );
}

export default App;
