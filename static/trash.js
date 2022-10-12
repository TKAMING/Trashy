function message() {
    var first_name = document.getElementById("first_name");
    var last_name = document.getElementById("last_name");
    var email = document.getElementById("email");
    var city = document.getElementById("city");
    var state = document.getElementById("state");
    var zip = document.getElementById("zip");
    var street = document.getElementById("street");
    var house_number = document.getElementById("house_number");
    var msg = document.getElementById("msg");
    const success = document.getElementById("success");
    const danger = document.getElementById("danger");

    if(first_name.value === "" || last_name.value === "" || email.value === "" || city.value === "" || state.value === "" || zip.value === "" || street.value === "" || house_number.value === "") {
        danger.style.display = "block";
        prevent_submition();
    }
    else {
        setTimeout(() => {
            first_name.value = "";
            last_name.value = "";
            email.value = "";
            city.value = "";
            state.value = "";
            zip.value = "";
            street.value = "";
            house_number.value = "";
            msg.value = "";
        }, 2000);

        success.style.display = "block";
    }
    

    setTimeout(() => {
        danger.style.display = "none";
        success.style.display = "none";
    }, 4000);
}

function message_register_admin() {
    var username = document.getElementById("username");
    var password = document.getElementById("password");
    var confirm = document.getElementById("confirm");
    var admin_email = document.getElementById("admin_email");

    if (username.value === "" || password.value === "" || confirm.value === "") {
        danger.style.display = "block";
        prevent_submition();
    }

    else {
        setTimeout(() => {
            username.value = "";
            password.value = "";
            confirm.value = "";
            admin_email.value = "";
        }, 2000);

        success.style.display = "block";
    }

    setTimeout(() => {
        danger.style.display = "none";
        success.style.display = "none";
    }, 4000);
}

function message_login_admin() {
    var login_username = document.getElementById("username");
    var login_password = document.getElementById("password");

    if (login_username.value === "" || login_password.value === "") {
        danger.style.display = "block";
        prevent_submition();
    }

    else {
        setTimeout(() => {
            login_username.value = "";
            login_password.value = "";
        }, 2000);

        success.style.display = "block";
    }

    setTimeout(() => {
        danger.style.display = "none";
        success.style.display = "none";
    }, 4000);

}


function prevent_submition() {
    event.preventDefault();
}

// for the chart 
const labels = ["Yellow can", "Black can", "Brown can", "Blue can"];
const data = {
    labels: labels,
    datasets: [{
      label: 'How many cans from wich color to put out.',
      data: [6, 1, 5, 3],
      backgroundColor: [
        'rgba(255, 205, 86, 0.2)',
        'rgba(26, 26, 26, 0.2)',
        'rgba(66, 33, 0, 0.2)',
        'rgba(54, 162, 235, 0.2)'
      ],
      borderColor: [
        'rgb(255, 205, 86)',
        'rgb(26, 26, 26)',
        'rgb(66, 33, 0)',
        'rgb(54, 162, 235)'
      ],
      borderWidth: 1
    }]
};

const config = {
  type: 'bar',
  data: data,
  options: {
    scales: {
      y: {
        beginAtZero: true
      }
    }
  },
};

const myChart = new Chart(
    document.getElementById('myChart'),
    config
  );