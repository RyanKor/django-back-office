let exp = document.querySelector(".expenditure").getContext("2d");
let expChart = new Chart(exp, {
  // The type of chart we want to create
  type: "line",

  // The data for our dataset
  data: {
    labels: ["January", "February", "March", "April", "May", "June", "July"],
    datasets: [
      {
        label: "Expenditure (VND)",
        backgroundColor: "skyblue",
        borderColor: "rgb(202, 212, 255)",
        data: [0, 10, 5, 2, 20, 30, 45],
      },
    ],
  },

  // Configuration options go here
  options: {},
});
