const element = document.getElementById("red_header");
element.addEventListener("click", function () {
  const header = document.querySelector("header");
  header.classList.add("red");
});