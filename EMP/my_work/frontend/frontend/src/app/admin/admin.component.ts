import { Component } from '@angular/core';
import { AdminService } from './admin.service';

@Component({
  selector: 'app-admin',
  templateUrl: './admin.component.html',
  styleUrls: ['./admin.component.css']
})
export class AdminComponent {
  email: string = '';
  password: string = '';
  errorMessage: string = '';

  constructor(private adminService: AdminService) {}

  onLogin(): void {
    this.adminService.loginAdmin(this.email, this.password)
      .subscribe(
        (response) => {
          console.log('Login successful', response);
        },
        (error) => {
          console.error('Login failed', error);
          this.errorMessage = 'Login failed, please check your credentials';
        }
      );
  }

  logout(): void {
    this.adminService.logoutAdmin()
      .subscribe(
        () => {
          console.log('Logout successful');
        },
        (error: any) => {
          console.error('Logout failed', error);
        }
      );
  }
}





 





// import { Component, OnInit } from '@angular/core';
// import { FormBuilder, FormGroup, NgForm, Validators } from '@angular/forms';
// import { AdminService } from './admin.service';
// import { Admin } from './interfaces';
// import { Router } from '@angular/router';
// import { Observable } from 'rxjs';
// import { HttpClient } from '@angular/common/http';

// @Component({
//   selector: 'app-admin',
//   templateUrl: './admin.component.html',
//   styleUrls: ['./admin.component.css'],
// })
// export class AdminComponent implements OnInit {
//   adminForm: FormGroup;
//   admins: Admin[] | null | undefined;
//   admin = { email: '', password: '' };

//   constructor(private fb: FormBuilder, private adminService: AdminService, private router: Router) {
//     this.adminForm = this.fb.group({
//       name: ['', Validators.required],
//       email: ['', Validators.required],
//       password:['', Validators.required],
//       dept: ['', Validators.required],
//       address: ['', Validators.required],
//       gender: ['', Validators.required],
//       dob: ['', Validators.required],
//       phone: ['', Validators.required],
//       posting: ['', Validators.required],
//     });
//     this.admins = [];
//   }

//   ngOnInit():void {
//     this.getAdmins();
//   }

//   getAdmins(): void {
//     this.adminService.getAdmins().subscribe(admins => {
//       this.admins = admins;
//     });
//   }

//   onSubmit(): void {
//     const adminData = this.adminForm.value;
//     this.adminService.createAdmin(adminData).subscribe(() => {
//       // Clear the form and reset validation
//       this.adminForm.reset();
//       Object.keys(this.adminForm.controls).forEach(key => {
//         this.adminForm.get(key)?.setErrors(null);
//       });
//       // Update the list of admins
//       this.getAdmins();
//     });
//   }

//   logout() {
//     this.router.navigate(['/login']);
//   }
// }
