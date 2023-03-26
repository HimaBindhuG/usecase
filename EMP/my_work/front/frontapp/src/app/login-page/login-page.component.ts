// // import { Component } from '@angular/core';
// // import { HttpClient } from '@angular/common/http';

// // @Component({
// //   selector: 'app-login-page',
// //   templateUrl: './login-page.component.html',
// //   styleUrls: ['./login-page.component.css']
// // })
// // export class LoginPageComponent {
// //   constructor(private http: HttpClient) {}

// //   login() {
// //     const username = (<HTMLInputElement>document.getElementById('username')).value;
// //     const password = (<HTMLInputElement>document.getElementById('password')).value;
    

// //     const loginData = {
// //       username: username,
// //       password: password
// //     };
// //     interface Response {
// //       access_token: string;
// //     }

// //     this.http.post('http://localhost:5000/admin/login', loginData)
// //       .subscribe(
// //         (response) => {
// //           // Save the JWT token to local storage
// //           localStorage.setItem('access_token', (<Response>response).access_token);

// //           // Redirect to the admin page
// //           window.location.href = 'admin-page.component.html';
// //         },
// //         (error) => {
// //           alert('Invalid username or password');
// //         }
// //       );
// //   }
// // }
import { Component } from '@angular/core';
import { AuthService } from '../authservice';
import { HttpClient } from '@angular/common/http';
import { FormControl, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-login-page',
  templateUrl: './login-page.component.html',
  styleUrls: ['./login-page.component.css']
})
export class LoginPageComponent {
  username: string='';
  password: string='';
  loginForm : FormGroup;
  constructor(private authService: AuthService) {
    this.loginForm = new FormGroup({
      username : new FormControl('',Validators.required),
      password : new FormControl('',Validators.required),
      logintype : new FormControl('',Validators.required)
    })
  }

  login() {
    // const email = this.username;
    // const password = this.password;
    const email = this.loginForm.get('username')?.value;
    const password = this.loginForm.get('password')?.value;
    console.log(this.loginForm.get('username')?.value)
    console.log(this.loginForm.get('password')?.value)
    const type = this.loginForm.get('logintype')?.value
    this.authService.login(email, password, type).subscribe(
      result => {
        if (type === "admin") {
          window.location.href = "admin-login.component.html";
        } else if (type === "manager") {
          window.location.href = "manager-login.component.html";
        } else if (type === "employee") {
          window.location.href = "employee-login.component.html";
        }
        // window.location.href = "admin-login.component.html"; // change the redirection URL
      },
      error => {
        console.log(error);
        alert('Invalid username or password'); // show an alert message if login fails
      }
    );
  }
}





