import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-manager-login',
  templateUrl: './manager-login.component.html',
  styleUrls: ['./manager-login.component.css']
})
export class ManagerLoginComponent implements OnInit {

  loginForm!: FormGroup;
  assignTaskForm!: FormGroup;
  employees: string[] = [];
  leaveRequests: any[] = []; // Change the type of the leaveRequests array
  tasks: any[] = []; // Change the type of the tasks array
  isLoggedIn = false;

  constructor(private formBuilder: FormBuilder, private router: Router) { }

  ngOnInit(): void {
    this.loginForm = this.formBuilder.group({
      username: ['', Validators.required],
      password: ['', Validators.required]
    });

    this.assignTaskForm = this.formBuilder.group({
      taskName: ['', Validators.required],
      assignedTo: ['', Validators.required]
    });
  }

  login(): void {
    if (this.loginForm.invalid) {
      return;
    }

    this.isLoggedIn = true;
    this.router.navigate(['manager']);
  }

  assignTask(): void {
    if (this.assignTaskForm.invalid) {
      return;
    }

    const taskName = this.assignTaskForm.controls['taskName'].value; // Fix property access
    const assignedTo = this.assignTaskForm.controls['assignedTo'].value; // Fix property access

    this.tasks.push({ name: taskName, employeeName: assignedTo, status: 'assigned' }); // Change task object structure

    this.assignTaskForm.reset();
  }

  logout(): void {
    this.isLoggedIn = false;
    this.router.navigate(['']);
  }

  acceptLeaveRequest(leaveRequest: any): void { // Add acceptLeaveRequest method
    leaveRequest.status = 'accepted';
  }

  rejectLeaveRequest(leaveRequest: any): void { // Add rejectLeaveRequest method
    leaveRequest.status = 'rejected';
  }

}
