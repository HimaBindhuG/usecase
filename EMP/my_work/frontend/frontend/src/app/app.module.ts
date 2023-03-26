import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { HttpClientModule } from '@angular/common/http';
import { ReactiveFormsModule } from '@angular/forms';
import { FormsModule } from '@angular/forms'; // added this line


import { AppComponent } from './app.component';
import { HomePageComponent } from './home-page/home-page.component';
import { LoginComponent } from './login/login.component';
import { EmployeeComponent } from './employee/employee.component';
import { ManagerComponent } from './manager/manager.component';
import { AdminComponent } from './admin/admin.component';
import { AdminService } from './admin/admin.service';
import { EmployeeDetailsComponent } from './employee-details/employee-details.component';
import { AuthService } from './auth.service';
import { AdminRegistrationComponent } from './admin-registration/admin-registration.component';

@NgModule({
  declarations: [
    AppComponent,
    HomePageComponent,
    LoginComponent,
    EmployeeComponent,
    ManagerComponent,
    AdminComponent,
    EmployeeDetailsComponent,
    AdminRegistrationComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    ReactiveFormsModule,    
    FormsModule // added this line


  ],
  providers: [AdminService,AuthService],
  bootstrap: [AppComponent],
  exports: [AdminComponent], // add this line

})
export class AppModule { }
