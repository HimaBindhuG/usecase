import { Component, Injectable, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class EmployeeService {
  private apiUrl = 'http://localhost:3000/employees';

  constructor(private http: HttpClient) { }

  getEmployees() {
    return this.http.get(this.apiUrl);
  }
}

@Component({
  selector: 'app-employee',
  templateUrl: './employee.component.html',
  styleUrls: ['./employee.component.css']
})
export class EmployeeComponent implements OnInit {
  employees: any[] = [];

  constructor(private http: HttpClient, private router: Router) { }

  ngOnInit(): void {
    // Make a GET request to retrieve all employees
    this.http.get<any[]>('http://localhost:3000/employees').subscribe((response) => {
      this.employees = response;
    });
  }

  addEmployee(name: string, email: string, password: string, dept: string, address: string, gender: string, dob: string, phone: string, posting: string): void {
    // Make a POST request to add a new employee
    this.http.post<any>('http://localhost:3000/employees', { name, email, password, dept, address, gender, dob, phone, posting }).subscribe((response) => {
      // Add the new employee to the employees array
      this.employees.push(response);
    });
  }

  logout(): void {
    this.router.navigate(['/login']);
  }
}
