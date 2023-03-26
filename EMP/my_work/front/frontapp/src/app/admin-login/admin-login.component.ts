import { Component, OnInit } from '@angular/core';
import { FormBuilder,FormControl, FormGroup, Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { AdminService } from '../admin.service';
import {Employee, Manager } from '../user.model';

@Component({
  selector: 'app-admin-login',
  templateUrl: './admin-login.component.html',
  styleUrls: ['./admin-login.component.css']
})
export class AdminLoginComponent implements OnInit {
  // employee: Employee = new Employee('', '', '', '', '', '', '', '', '', 0);
  employee: Employee = new Employee();
  manager: Manager = new Manager(); // initialize the admin object
  managers: Manager[] = [];
  employees: Employee[] = [];
  loginForm: any;
  employeeForm: any;
  managerForm: any;

  constructor(
    private fb: FormBuilder,
    private http: HttpClient,
    private router: Router,
    private adminService: AdminService
  ) {}

  ngOnInit() {
    this.fetchManagers();
    this.fetchEmployees();
    this.loginForm = this.fb.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', Validators.required]
    });

    this.employeeForm = this.fb.group({
      emp_name: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      password: ['', Validators.required],
      phone: ['', Validators.required],
      address: ['', Validators.required],
      dateOfBirth: ['', Validators.required],
      gender: ['', Validators.required],
      manager: ['', Validators.required]
    });

    this.managerForm = this.fb.group({
      mag_name: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      password: ['', Validators.required],
      phone: ['', Validators.required],
      address: ['', Validators.required],
      dateOfBirth: ['', Validators.required],
      gender: ['', Validators.required],
      emp_mag_id: ['', Validators.required]
    });
  }
  onSubmitemployee(): void {
    const emp_name = this.employeeForm.get('emp_name').value;
    const email = this.employeeForm.get('email').value;
    const phone = this.employeeForm.get('phone').value;

    console.log('Employee created with name:', emp_name);
    console.log('Email:', email);
    console.log('Phone:', phone);
    this.addEmployee(this.employee);
  }
  onSubmitmanager(): void {
    const mag_name = this.managerForm.get('mag_name').value;
    const email = this.managerForm.get('email').value;
    const phone = this.managerForm.get('phone').value;
  
    console.log('manager created with name:', mag_name);
    console.log('Email:', email);
    console.log('Phone:', phone);
    
    this.addManager(this.manager);
  }
  
  
 
  // loginForm: FormGroup = this.fb.group({
  //   email: ['', [Validators.required, Validators.email]],
  //   password: ['', Validators.required]
  // });

  

  // ngOnInit() {
  //   this.loginForm = this.fb.group({
  //     email: ['', [Validators.required, Validators.email]],
  //     password: ['', Validators.required]
  //   });

  //   this.employeeForm = this.fb.group({
  //     name: ['', Validators.required],
  //     email: ['', [Validators.required, Validators.email]],
  //     password: ['', Validators.required],
  //     phone: ['', Validators.required],
  //     address: ['', Validators.required],
  //     dateOfBirth: ['', Validators.required],
  //     gender: ['', Validators.required],
  //     manager: ['', Validators.required]
  //   });
  // }

  // onSubmit() {
  //   // Handle login logic here
  // }

  addEmployee(employee: Employee): void {
    this.adminService.createEmployee(employee).subscribe(() => {
      this.fetchEmployees(); // fetch updated list of admins after creating new admin
      // success message
    }, error => {
      // console.log(this.employee);
    });
  }


  addManager(manager: Manager): void {
    this.adminService.createManager(manager).subscribe(() => {
      this.fetchManagers(); // fetch updated list of admins after creating new admin
      // success message
    }, error => {
      // console.log(this.manager);
    });
  }

  fetchManagers(): void {
    this.adminService.getManagers().subscribe((managers: Manager[]) => {
      this.managers = managers;
    });
  }

  fetchEmployees(): void {
    this.adminService.getEmployees().subscribe((employees: Employee[]) => {
      this.employees = employees;
    });
  }

}
