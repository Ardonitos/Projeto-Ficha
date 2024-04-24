function ifEmptyReturnNull(value) {
  if (value === "") {
    return null;
  } else {
    return value;
  }
}

const btnQuery = document.querySelector(".query");
btnQuery.addEventListener("click", function () {
  const name = ifEmptyReturnNull(document.querySelector(".name").value);
  const date = ifEmptyReturnNull(document.querySelector(".date").value);

  const postObject = {
    name,
    date,
  };
  fetch(`${window.origin}/read`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(postObject),
  })
    .then((response) => response.json())
    .then((data) => {
      const tabela = document.querySelector(".dataTable");
      const tbody = tabela.querySelector("tbody");

      tbody.innerHTML = "";

      data.forEach((object) => {
        const tr = document.createElement("tr");

        Object.values(object).forEach((value) => {
          const td = document.createElement("td");
          td.textContent = value;
          tr.appendChild(td);
        });

        tbody.appendChild(tr);
      });
    });
});
