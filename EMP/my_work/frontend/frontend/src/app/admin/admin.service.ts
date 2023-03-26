import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

interface Admin {
  email: string;
  password: string;
}

@Injectable({
  providedIn: 'root'
})
export class AdminService {

  constructor(private http: HttpClient) {}

  createAdmin(admin: Admin): Observable<any> {
    return this.http.post<any>('http://localhost:5000/login/', admin);
  }

  loginAdmin(admin: Admin): Observable<any> {
    return this.http.post<any>('http://localhost:5000/login', admin);
  }

  logoutAdmin(): Observable<any> {
    return this.http.post<any>('http://localhost:5000/admin/logout', {});
  }

}
