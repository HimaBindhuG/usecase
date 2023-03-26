import { Component } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';
import { AdminService } from '../admin/admin.service';

@Component({
  templateUrl: './admin-registration.component.html',
  styleUrls: ['./admin-registration.component.css']
})
export class AdminRegistrationComponent {

  constructor(private adminService: AdminService, private router: Router) {}

  onSubmit(form: NgForm) {
    const adminData = {
      email: form.value.email,
      password: form.value.password
    };
    this.adminService.createAdmin(adminData).subscribe(() => {
      this.router.navigate(['/admin']);
    }, (error) => {
      console.log(error);
    });
  }

}
