function addTask() {
  var taskInput = document.getElementById("taskInput");
  var taskList = document.getElementById("taskList");
  if (taskInput.value.trim() === "") {
    alert("Please enter a task");
    return;
  }
  var li = document.createElement("li");
  li.textContent = taskInput.value;
  var removeButton = document.createElement("button");
  removeButton.textContent = "Remove";
  removeButton.onclick = function () {
    taskList.removeChild(li);
  };
  li.appendChild(removeButton);
  taskList.appendChild(li);
  taskInput.value = "";
}
