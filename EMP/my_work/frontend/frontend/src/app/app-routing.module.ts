import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { EmployeeDetailsComponent } from './employee-details/employee-details.component';
import { AuthGuard } from './auth.guard';
import { AdminRegistrationComponent } from './admin-registration/admin-registration.component';

import { HomePageComponent } from './home-page/home-page.component';
import { LoginComponent } from './login/login.component';
import { EmployeeComponent } from './employee/employee.component';
import { ManagerComponent } from './manager/manager.component';
import { AdminComponent } from './admin/admin.component';

const routes: Routes = [
  { path: '', component: HomePageComponent },
  { path: 'login', component: LoginComponent },
  // { path: 'employee', component: EmployeeComponent },
  // { path: 'manager', component: ManagerComponent },
  { path: 'admin/create', component: AdminComponent, canActivate: [AuthGuard] },
  // { path: 'employee/:id', component: EmployeeDetailsComponent }, // Add this line
  // { path: '**', redirectTo: '/login' },
  // { path: '', redirectTo: '/login', pathMatch: 'full' },
  { path: 'admin/register', component: AdminRegistrationComponent }

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
