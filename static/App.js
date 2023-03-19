//alert("hello");
function addDiv() {
  const div = document.createElement("div");
  const text = " hi there";
  const divContent = document.createTextNode(text);
  div.appendChild(divContent);

  div.style.color = "red";
  div.style.border = "1px solid green";
  div.style.padding = "4px";
  appDiv = document.querySelector(".App");
  appDiv.insertBefore(div);
};

// export { my };
