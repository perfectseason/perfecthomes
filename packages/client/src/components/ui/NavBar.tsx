import { Link } from "react-router-dom";
import logo from "../../assets/products/logo.jpg";

const Navbar = () => {
  return (
    <nav className="bg-white shadow-md fixed top-0 left-0 w-full z-50">
      <div className="max-w-7xl mx-auto px-6 py-4 flex justify-between items-start">
        <img src={logo} alt="Logo" className="h-10 w-10 rounded-full" />
        <h1 className="flex text-xl p-2 font-bold text-gray-500">
          PERFECT SEASON
        </h1>

        <div className="space-x-6">
          <Link to="/" className="hover:text-blue-600 transition">
            Home
          </Link>
          <Link to="/about" className="hover:text-blue-600 transition">
            About
          </Link>
          <Link to="/contact" className="hover:text-blue-600 transition">
            Contact
          </Link>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
