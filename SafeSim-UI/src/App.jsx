import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import Dashboard from './components/Dashboard';
import Configurations from './components/Configurations';
import Logs from './components/Logs';

const App = () => {
  return (
    <Router>
      <Navbar />
      <div className=" bg-background text-white py-10 px-6">
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/configurations" element={<Configurations />} />
          <Route path="/logs" element={<Logs />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
