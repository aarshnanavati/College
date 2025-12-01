const express = require("express");
const cors = require("cors");
const { v4: uuidv4 } = require("uuid");

const app = express();
app.use(express.json());
app.use(cors());

let versions = [];
let previousText = "";

function compareTexts(oldText, newText) {
  const oldWords = oldText.trim().split(/\s+/).filter(Boolean);
  const newWords = newText.trim().split(/\s+/).filter(Boolean);

  const added = newWords.filter((w) => !oldWords.includes(w));
  const removed = oldWords.filter((w) => !newWords.includes(w));

  return { added, removed };
}

app.post("/save-version", (req, res) => {
  const { newText } = req.body;
  console.log("Received request:", newText);

  const diff = compareTexts(previousText, newText);

  const entry = {
    id: uuidv4(),
    timestamp: new Date().toLocaleString(),
    addedWords: diff.added,
    removedWords: diff.removed,
    oldLength: previousText.length,
    newLength: newText.length,
  };

  versions.push(entry);
  previousText = newText;

  res.json(versions);
});

app.get("/versions", (req, res) => {
  res.json(versions);
});

app.listen(5000, () => console.log("Backend running on port 5000"));
