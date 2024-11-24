import { FaFileAlt, FaShieldAlt, FaNetworkWired } from 'react-icons/fa';

const SimulationCard = ({ title, description, onClick, progress }) => {
  // Define icon based on the simulation title
  const getIcon = (title) => {
    switch (title) {
      case 'File Operations':
        return <FaFileAlt className="text-4xl text-blue-500 mr-4" />;
      case 'Ransomware':
        return <FaShieldAlt className="text-4xl text-red-500 mr-4" />;
      case 'Network Traffic':
        return <FaNetworkWired className="text-4xl text-green-500 mr-4" />;
      default:
        return null;
    }
  };

  return (
    <div
      className="bg-white rounded-lg shadow-lg p-6 hover:shadow-2xl transition-shadow duration-300 ease-in-out cursor-pointer"
      onClick={onClick}
    >
      {/* Title and Icon */}
      <div className="flex items-center justify-center mb-4">
        {getIcon(title)}
        <h3 className="text-xl font-semibold text-gray-900">{title}</h3>
      </div>

      {/* Description */}
      <p className="text-gray-600 mb-6 text-center">{description}</p>

      {/* Progress Bar */}
      <div className="w-full bg-gray-200 h-2 rounded-full">
        <div
          className={`h-2 rounded-full ${progress < 50 ? 'bg-red-500' : 'bg-green-500'}`}
          style={{ width: `${progress}%` }}
        ></div>
      </div>
      <p className="text-xs text-gray-600 mt-2 text-center">{progress}% Complete</p>

      {/* Start Simulation Button */}
      <div className="flex justify-center mt-4">
        <button
          className="bg-accent text-white py-2 px-4 rounded-lg hover:bg-accent-dark transition-colors duration-300"
        >
          Start Simulation
        </button>
      </div>
    </div>
  );
};

export default SimulationCard;
