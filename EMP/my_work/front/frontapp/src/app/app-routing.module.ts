import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AdminLoginComponent } from './admin-login/admin-login.component';
import { EmployeeLoginComponent } from './employee-login/employee-login.component';
import { HomepageComponent } from './homepage/homepage.component';
import { LoginPageComponent } from './login-page/login-page.component';
import { ManagerLoginComponent } from './manager-login/manager-login.component';
import { EditProfileComponent } from './edit-profile/edit-profile.component';
import { CreateAdminComponent } from './create-admin/create-admin.component';

const routes: Routes = [
  { path: '', component: HomepageComponent },
  { path: 'homepage.component.html', component: HomepageComponent },
  { path: 'login-page.component.html', component: LoginPageComponent },
  { path: 'admin-login.component.html', component: AdminLoginComponent },
  { path: 'employee-login.component.html', component: EmployeeLoginComponent },  
  { path: 'manager-login.component.html', component: ManagerLoginComponent },
  { path: 'edit-profile.component.html', component: EditProfileComponent },
  { path: 'create-admin.component.html', component: CreateAdminComponent },

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
