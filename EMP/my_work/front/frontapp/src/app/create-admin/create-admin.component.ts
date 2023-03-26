import { Component, OnInit } from '@angular/core';
import { Admin, Employee, Manager } from '../user.model';
import { AdminService } from '../admin.service';

@Component({
  selector: 'app-create-admin',
  templateUrl: './create-admin.component.html',
  styleUrls: ['./create-admin.component.css']
})
export class CreateAdminComponent implements OnInit {
  admin: Admin = new Admin(); // initialize the admin object
  admins: Admin[] = [];
  managers: Manager[] = [];
  employees: Employee[] = [];

  constructor(private adminService: AdminService) { }

  ngOnInit() {
    this.fetchAdmins();
    this.fetchManagers();
    this.fetchEmployees();
  }

  onSubmit(): void {
    this.addAdmin(this.admin);
  }

  addAdmin(admin: Admin): void {
    this.adminService.createAdmin(admin).subscribe(() => {
      this.fetchAdmins(); // fetch updated list of admins after creating new admin
      // success message
    }, error => {
      // error message
    });
  }

  fetchAdmins(): void {
    this.adminService.getAdmins().subscribe((admins: Admin[]) => {
      this.admins = admins;
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
