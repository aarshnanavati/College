import Addtodo from "./components/Addtodo";
import Appname from "./components/Appname";
import TodoItem1 from "./components/Todoitem1";
import TodoItem2 from "./components/Todoitem2";
import './App.css';

function App() {
  return (
    <center class="todo-container">
      <Appname></Appname>
      <Addtodo></Addtodo>
      <div class = 'items-container'></div>
        <TodoItem1></TodoItem1>
        <TodoItem2></TodoItem2>
    </center>
  );
}

export default App;
