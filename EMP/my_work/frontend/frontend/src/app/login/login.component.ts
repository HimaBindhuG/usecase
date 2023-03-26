import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { NgForm } from '@angular/forms';
import { AuthService } from '../auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  user = { email: '', password: '' };

  constructor(private http: HttpClient, private authService: AuthService, private router: Router) {}

  submitForm(form: NgForm) {
    const username = form.value['username'];
    const password = form.value['password'];
    const loginType = form.value['login-type'];
    const email = form.value["email"];

    if (loginType === 'employee') {
      // For employee login validation
      this.http.post('http://127.0.0.1:3000/login/', { username, password }).subscribe((response: any) => {
        console.log('Employee login successful');
        localStorage.setItem('token', response.token);
        this.authService.setLoggedIn(true);
      }, (error) => {
        console.error('Employee login failed', error);
      });
    } 
    else if (loginType === 'manager') {
      // Manager login validation
      this.http.post('http://127.0.0.1:9000/login/', { username, password }).subscribe((response: any) => {
        console.log('Manager login successful');
        localStorage.setItem('token', response.token);
        this.authService.setLoggedIn(true);
      }, (error) => {
        console.error('Manager login failed', error);
      });
    }  
    else if (loginType === 'admin') {
      // Admin login validation
      this.http.post('http://localhost:5000/login/', { email, password }).subscribe((response: any) => {
        console.log('Admin login successful');
        localStorage.setItem('token', response.token);
        this.authService.setIsAuthenticated(true);
        if (response.admin) {
          this.router.navigate(['/admin/create']);
        } else {
          this.router.navigate(['/admin/dashboard']);
        }
      }, (error) => {
        console.error('Admin login failed', error);
      });
    }
  }
}
