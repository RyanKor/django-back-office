let inc = document.querySelector(".income").getContext("2d");
let chart = new Chart(inc, {
  // The type of chart we want to create
  type: "line",

  // The data for our dataset
  data: {
    labels: ["January", "February", "March", "April", "May", "June", "July"],
    datasets: [
      {
        label: "Income (VND)",
        backgroundColor: "rgb(202, 212, 255)",
        borderColor: "rgb(202, 212, 255)",
        data: [0, 10, 5, 2, 20, 30, 45],
      },
    ],
  },

  // Configuration options go here
  options: {},
});
//   Cannot change width, height with CSS files
// Reference
// https://www.chartjs.org/docs/latest/general/responsive.html
// chart.canvas.style.height = "25vh";
// chart.canvas.style.width = "25vw";
