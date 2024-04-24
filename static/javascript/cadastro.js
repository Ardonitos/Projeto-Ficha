function ifEmptyReturnNull(value) {
  if (value === "") {
    return null;
  } else {
    return value;
  }
}

function submitInsert(object) {
  fetch(`${window.origin}/insert`, {
    method: "POST",
    credentials: "include",
    body: JSON.stringify(object),
    cache: "no-cache",
    headers: new Headers({
      "content-type": "application/json",
    }),
  });
}

const btnInsert = document.querySelector(".insert");
btnInsert.addEventListener("click", function () {
  const name = ifEmptyReturnNull(document.querySelector(".name").value);
  const product = ifEmptyReturnNull(document.querySelector(".product").value);
  const date = ifEmptyReturnNull(document.querySelector(".date").value);
  const amount = ifEmptyReturnNull(document.querySelector(".amount").value);
  const amountPaid = ifEmptyReturnNull(
    document.querySelector(".amount-paid").value
  );
  const amountDue = ifEmptyReturnNull(
    document.querySelector(".amount-due").value
  );

  insertQuery = {
    name,
    product,
    date,
    amount,
    amountPaid,
    amountDue,
  };

  submitInsert(insertQuery);
});
