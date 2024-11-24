import { Link } from 'react-router-dom';  // We will use React Router for navigation
import { useState } from 'react'; // For mobile toggle

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false); // Manage mobile menu toggle state

  const toggleMenu = () => setIsOpen(!isOpen); // Toggle the mobile menu visibility

  return (
    <nav className="bg-primary p-4 shadow-lg">
      <div className="max-w-7xl mx-auto flex justify-between items-center">
        {/* Logo Section */}
        <h1 className="text-white text-3xl font-semibold">SafeSim</h1>
        
        {/* Desktop Links */}
        <div className="hidden md:flex space-x-8">
          <Link
            to="/"
            className="text-white hover:text-accent transition-colors duration-200 text-lg"
          >
            Dashboard
          </Link>
          <Link
            to="/configurations"
            className="text-white hover:text-accent transition-colors duration-200 text-lg"
          >
            Configurations
          </Link>
          <Link
            to="/logs"
            className="text-white hover:text-accent transition-colors duration-200 text-lg"
          >
            Logs
          </Link>
        </div>
        
        {/* Mobile Menu Button */}
        <div className="md:hidden flex items-center">
          <button
            onClick={toggleMenu}
            className="text-white p-2 rounded-md focus:outline-none"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              className="w-6 h-6"
            >
              {isOpen ? (
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth="2"
                  d="M6 18L18 6M6 6l12 12"
                />
              ) : (
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth="2"
                  d="M4 6h16M4 12h16M4 18h16"
                />
              )}
            </svg>
          </button>
        </div>
      </div>

      {/* Mobile Menu */}
      <div
        className={`md:hidden ${isOpen ? 'block' : 'hidden'} bg-primary py-4 space-y-4 mt-4`}
      >
        <Link
          to="/"
          className="text-white block text-lg hover:text-accent transition-colors duration-200"
          onClick={toggleMenu}
        >
          Dashboard
        </Link>
        <Link
          to="/configurations"
          className="text-white block text-lg hover:text-accent transition-colors duration-200"
          onClick={toggleMenu}
        >
          Configurations
        </Link>
        <Link
          to="/logs"
          className="text-white block text-lg hover:text-accent transition-colors duration-200"
          onClick={toggleMenu}
        >
          Logs
        </Link>
      </div>
    </nav>
  );
};

export default Navbar;
