import React from 'react';
import { AiOutlineInfoCircle, AiOutlineExclamationCircle, AiOutlineCheckCircle, AiOutlineCloseCircle } from 'react-icons/ai'; // Icons for log types

// Sample log data with various levels (info, warning, error, success)
const logs = [
  { message: 'Simulated file operation started.', timestamp: '2024-11-24 10:00:00', type: 'info' },
  { message: 'Ransomware simulation running.', timestamp: '2024-11-24 10:05:12', type: 'warning' },
  { message: 'Network traffic simulated successfully.', timestamp: '2024-11-24 10:10:30', type: 'success' },
  { message: 'Error encountered during simulation.', timestamp: '2024-11-24 10:15:45', type: 'error' },
];

// Define styles for different log types
const logTypeStyles = {
  info: 'bg-blue-100 text-blue-800',
  success: 'bg-green-100 text-green-800',
  warning: 'bg-yellow-100 text-yellow-800',
  error: 'bg-red-100 text-red-800',
};

// Map log types to icons
const logTypeIcons = {
  info: <AiOutlineInfoCircle className="text-blue-800 text-4xl" />,
  success: <AiOutlineCheckCircle className="text-green-800 text-4xl" />,
  warning: <AiOutlineExclamationCircle className="text-yellow-800 text-4xl" />,
  error: <AiOutlineCloseCircle className="text-red-800 text-4xl" />,
};

const Logs = () => {
  return (
    <div className=" bg-gray-50 py-2 px-4 sm:px-6 lg:px-8">
      <h2 className="text-4xl font-semibold text-center text-primary mb-8">System Logs</h2>

      <div className="space-y-6">
        {logs.map((log, index) => (
          <div
            key={index}
            className={`flex items-start p-6 rounded-lg shadow-lg transition-all transform hover:scale-105 hover:shadow-2xl cursor-pointer ${logTypeStyles[log.type]}`}
            onClick={() => alert(`Log details: ${log.message}`)}
          >
            {/* Log Icon */}
            <div className="mr-5">{logTypeIcons[log.type]}</div>

            <div className="flex-1">
              <p className="font-semibold text-lg text-gray-900">{log.message}</p>
              <p className="text-xs text-gray-600 mt-1">{new Date(log.timestamp).toLocaleString()}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Logs;
