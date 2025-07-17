const element = document.getElementById("update_header");
element.addEventListener("click", function () {
  const header = document.querySelector("header");
  header.textContent = "New Header!!!";
});
