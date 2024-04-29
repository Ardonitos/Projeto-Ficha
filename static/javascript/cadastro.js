function ifEmptyReturnNull(value) {
  if (value === "") {
    return null;
  } else {
    return value;
  }
}

function ifEmptyReturnZero(value) {
  if (value === "") {
    return "0";
  } else {
    return value;
  }
}

function submitInsert(object) {
  fetch(`${window.origin}/insert`, {
    method: "POST",
    body: JSON.stringify(object),
    headers: {
      "content-type": "application/json",
    },
  });
}

const btnInsert = document.querySelector(".insert");
btnInsert.addEventListener("click", function () {
  const name = ifEmptyReturnNull(document.querySelector(".name").value);
  const product = ifEmptyReturnNull(document.querySelector(".product").value);
  const date = ifEmptyReturnNull(document.querySelector(".date").value);
  const amount = ifEmptyReturnZero(document.querySelector(".amount").value);
  const amountPaid = ifEmptyReturnZero(
    document.querySelector(".amount-paid").value
  );
  const amountDue = null;

  insertQuery = {
    name,
    product,
    date,
    amount,
    amountPaid,
    amountDue,
  };

  if (name !== null && date !== null) {
    submitInsert(insertQuery);
  }
});
