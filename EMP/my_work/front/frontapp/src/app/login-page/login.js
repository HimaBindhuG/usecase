function login() {
    const form = document.getElementById("login-form");
    const username = form.elements["username"].value;
    const password = form.elements["password"].value;
    const loginType = form.elements["logintype"].value;
  
    // Authenticate user and get JWT token from server
    fetch('/admin/login', {
      method: 'POST',
      body: JSON.stringify({ email: username, password: password }),
      headers: {
        'Content-Type': 'application/json'
      }
    })
    .then(response => {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error('Invalid username or password');
      }
    })
    .then(data => {
      // Store JWT token in local storage
      localStorage.setItem('token', data.token);
  
      // Redirect to admin login page
      if (loginType === "admin") {
        window.location.href = "admin-login.component.html";
      } else if (loginType === "manager") {
        window.location.href = "manager-login.component.html";
      } else if (loginType === "employee") {
        window.location.href = "employee-login.component.html";
      }
    })
    .catch(error => {
      alert(error.message);
    });
  
    event.preventDefault();
  };
  