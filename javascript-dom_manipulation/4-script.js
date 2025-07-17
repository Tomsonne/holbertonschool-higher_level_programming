const element = document.getElementById("add_item");
element.addEventListener("click", function () {
  const ul = document.querySelector("ul.my_list");
  const new_item = document.createElement("li");
  new_item.textContent = "Item";
  ul.append(new_item);
});
