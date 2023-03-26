import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
    private apiUrl = 'http://localhost:5000/admin/login';

  private token: string = '';

  constructor(private http: HttpClient) { }

  login(username: string, password: string , loginType : string): Observable<any> {
    console.log(username,password,loginType)
    const body = new FormData();
    body.set('username', username);
    body.set('password', password);
    console.log(body);
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })
    };
    // if(loginType === 'employee'){
    //   this.apiUrl = 'http://localhost:3000/employee/login'
    // }
    // else if(loginType === 'manager'){
    //   this.apiUrl = 'http://localhost:9000/manager/login'
    // }
    
    // const body = {
    //   email: email,
    //   password: password
    // };
    console.log(body)
    return this.http.post<any>(this.apiUrl, body);
  }


  setToken(token: string) {
    localStorage.setItem('token', token);
    this.token = token;
  }

  getToken() {
    if (!this.token) {
      this.token = localStorage.getItem('token') || '';
    }
    return this.token;
  }

  isLoggedIn(): boolean {
    return !!this.getToken();
  }

  logout(): void {
    this.token = '';
    localStorage.removeItem('token');
  }
}
