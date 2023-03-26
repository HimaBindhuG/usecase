// import { Injectable } from '@angular/core';
// import { HttpClient } from '@angular/common/http';
// import { map, Observable } from 'rxjs';
// import { Admin, Manager, Employee } from './user.model';

// @Injectable({
//   providedIn: 'root'
// })
// export class AdminService {

//   private apiUrl = 'http://localhost:5000/admin'; // example API endpoint

//   private managers: Manager[] = []; // add private array to store manager data
//   private employees: Employee[] = []; // add private array to store employee data

//   constructor(private http: HttpClient) { }

//   createAdmin(admin: Admin): Observable<any> {
//     // HTTP POST request to create an admin
//     return this.http.post(`${this.apiUrl}`, admin);
//   }

//   getManagers(): Observable<Manager[]> {
//     // HTTP GET request to get all managers
//     return this.http.get<Manager[]>(`${this.apiUrl}/manager`);
//   }

//   getEmployees(): Observable<Employee[]> {
//     // HTTP GET request to get all employees
//     return this.http.get<Employee[]>(`${this.apiUrl}/employee`);
//   }

//   getAdmins(): Observable<Admin[]> {
//     // HTTP GET request to get all admins
//     return this.http.get<any[]>(`${this.apiUrl}`).pipe(
//       map((admins: any[]) => {
//         return admins.map((admin) => {
//           return {
//             id: admin.id,
//             name: admin.name,
//             username: admin.username,
//             password: admin.password,
//             dept: admin.dept,
//             address: admin.address,
//             email: admin.email,
//             phone: admin.phone,
//             gender: admin.gender, // add missing properties
//             dob: admin.dob,
//             posting: admin.posting
//           } as Admin;
//         });
//       })
//     );
//   }

//   // define setManagers method to update the private managers array
//   setManagers(managers: Manager[]): void {
//     this.managers = managers;
//   }

//   // define setEmployees method to update the private employees array
//   setEmployees(employees: Employee[]): void {
//     this.employees = employees;
//   }

//   // define getManagersData method to return the private managers array
//   getManagersData(): Manager[] {
//     return this.managers;
//   }

//   // define getEmployeesData method to return the private employees array
//   getEmployeesData(): Employee[] {
//     return this.employees;
//   }

// }


import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map, Observable } from 'rxjs';
import { Admin, Manager, Employee } from './user.model';

@Injectable({
  providedIn: 'root'
})
export class AdminService {

  private apiUrl = 'http://localhost:5000/admin'; // example API endpoint

  private managers: Manager[] = []; // add private array to store manager data
  private employees: Employee[] = []; // add private array to store employee data

  constructor(private http: HttpClient) { }

  createAdmin(admin: Admin): Observable<any> {
    // HTTP POST request to create an admin
    return this.http.post(`${this.apiUrl}`, admin);
  }

  createManager(manager: Manager): Observable<any> {
    // HTTP POST request to create a manager
    return this.http.post(`${this.apiUrl}/manager`, manager);
  }

  createEmployee(employee: Employee): Observable<any> {
    // HTTP POST request to create an employee
    return this.http.post(`${this.apiUrl}/employee`, employee);
  }

  getManagers(): Observable<Manager[]> {
    // HTTP GET request to get all managers
    return this.http.get<any[]>(`${this.apiUrl}/manager`).pipe(
      map((managers: any[]) => {
        return managers.map((manager) => {
          return {
            id: manager.id,
            mag_name: manager.name,
            username: manager.username,
            password: manager.password,
            dept: manager.dept,
            address: manager.address,
            email: manager.email,
            phone: manager.phone,
            gender: manager.gender, // add missing properties
            dob: manager.dob,
            posting: manager.posting
          } as Manager;
        });
      })
    );
    
  }
  

  getEmployees(): Observable<Employee[]> {
    // HTTP GET request to get all employees
    return this.http.get<any[]>(`${this.apiUrl}/employee`).pipe(
      map((employees: any[]) => {
        return employees.map((employee) => {
          return {
            id: employee.id,
            emp_name: employee.name,
            username: employee.username,
            password: employee.password,
            dept: employee.dept,
            address: employee.address,
            email: employee.email,
            phone: employee.phone,
            gender: employee.gender, // add missing properties
            dob: employee.dob,
            posting: employee.posting,
            emp_mag_id:employee.emp_mag_id
          } as Employee;
        });
      })
    );
  }

  getAdmins(): Observable<Admin[]> {
    // HTTP GET request to get all admins
    return this.http.get<any[]>(`${this.apiUrl}`).pipe(
      map((admins: any[]) => {
        return admins.map((admin) => {
          return {
            id: admin.id,
            name: admin.name,
            username: admin.username,
            password: admin.password,
            dept: admin.dept,
            address: admin.address,
            email: admin.email,
            phone: admin.phone,
            gender: admin.gender, // add missing properties
            dob: admin.dob,
            posting: admin.posting
          } as Admin;
        });
      })
    );
  }

  // define setManagers method to update the private managers array
  setManagers(managers: Manager[]): void {
    this.managers = managers;
  }

  // define setEmployees method to update the private employees array
  setEmployees(employees: Employee[]): void {
    this.employees = employees;
  }

  // define getManagersData method to return the private managers array
  getManagersData(): Manager[] {
    return this.managers;
  }

  // define getEmployeesData method to return the private employees array
  getEmployeesData(): Employee[] {
    return this.employees;
  }

}
