function ifEmptyReturnNull(value) {
  if (value === "") {
    return null;
  } else {
    return value;
  }
}

const btnPaid = document.querySelector(".btnPaid");
btnPaid.addEventListener("click", function () {
  const name = ifEmptyReturnNull(document.querySelector(".name").value);
  const amountPaid = ifEmptyReturnNull(
    document.querySelector(".amountPaid").value
  );
  const date = ifEmptyReturnNull(document.querySelector(".date").value);
  console.log("works 1");
  const updateObject = {
    name,
    amountPaid,
    date,
  };

  if (name !== null && amountPaid !== null) {
    console.log("works 2");
    fetch(`${window.origin}/update`, {
      method: "PUT",
      body: JSON.stringify(updateObject),
      headers: {
        "content-type": "application/json",
      },
    });
  }
});
