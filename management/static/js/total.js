let total = document.querySelector(".total").getContext("2d");
let totalChart = new Chart(total, {
  // The type of chart we want to create
  type: "pie",

  // The data for our dataset
  data: {
    labels: ["Income", "expenditure"],
    datasets: [
      {
        label: "inc-exp analysis",
        backgroundColor: "orange",
        borderColor: "black",
        data: [7, 45],
      },
    ],
  },

  // Configuration options go here
  options: {},
});
