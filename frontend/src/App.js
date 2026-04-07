import React, { useEffect, useState } from "react";

function App() {
  const [data, setData] = useState({});

  useEffect(() => {
    fetch("http://localhost:5001/api1").then(res => res.json()).then(d => setData(prev => ({...prev, api1: d})));
    fetch("http://localhost:5002/api2").then(res => res.json()).then(d => setData(prev => ({...prev, api2: d})));
    fetch("http://localhost:5003/api3").then(res => res.json()).then(d => setData(prev => ({...prev, api3: d})));
  }, []);

  return (
    <div>
      <h1>React Frontend 🚀</h1>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}

export default App;