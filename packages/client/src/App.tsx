import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Footer from "./components/ui/Footer";
import NavBar from "./components/ui/NavBar";
import Home from "./pages/Home";
import About from "./pages/About";
import Contact from "./pages/Contact";
import Properties from "./pages/Properties";

function App() {
  return (
    <Router>
      <div className="flex min-h-screen flex-col bg-white">
        <NavBar />
        <main className="flex-1 pt-16">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/about" element={<About />} />
            <Route path="/contact" element={<Contact />} />
            <Route path="/properties" element={<Properties />} />
          </Routes>
        </main>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
