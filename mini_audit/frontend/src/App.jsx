import { useState, useEffect } from "react";

function App() {
  const [text, setText] = useState("");
  const [versions, setVersions] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/versions")
      .then((res) => res.json())
      .then((data) => setVersions(data));
  }, []);
  const saveVersion = async () => {
    const response = await fetch("http://localhost:5000/save-version", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ newText: text }),
    });

    const data = await response.json();
    setVersions(data);
  };

  return (
    <div style={styles.container}>
      <h1>Mini Audit Trail Generator</h1>

      <textarea
        style={styles.textarea}
        placeholder="Type something..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      ></textarea>

      <button style={styles.button} onClick={saveVersion}>
        Save Version
      </button>

      <h2>Version History</h2>

      <div style={styles.historyBox}>
        {versions.length === 0 && <p>No versions saved yet.</p>}

        {versions.map((v) => (
          <div key={v.id} style={styles.versionItem}>
            <p><b>Time:</b> {v.timestamp}</p>
            <p><b>Added:</b> {v.addedWords.join(", ")}</p>
            <p><b>Removed:</b> {v.removedWords.join(", ")}</p>
            <p><b>Old Length:</b> {v.oldLength} | <b>New Length:</b> {v.newLength}</p>
            <hr />
          </div>
        ))}
      </div>
    </div>
  );
}

const styles = {
  container: {
    width: "60%",
    margin: "auto",
    padding: "20px",
    fontFamily: "Arial",
  },
  textarea: {
    width: "100%",
    height: "150px",
    fontSize: "16px",
    padding: "10px",
  },
  button: {
    marginTop: "10px",
    padding: "10px 20px",
    fontSize: "16px",
    cursor: "pointer",
  },
  historyBox: {
    marginTop: "20px",
    background: "#f3f3f3",
    padding: "15px",
    borderRadius: "8px",
  },
  versionItem: {
    marginBottom: "15px",
  },
};

export default App;
