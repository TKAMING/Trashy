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

    if (username.value === "" || password.value === "" || confirm.value === "" || admin_email.value === "") {
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

function prevent_submition() {
    event.preventDefault();
}