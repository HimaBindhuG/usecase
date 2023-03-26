import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-employee-login',
  templateUrl: './employee-login.component.html',
  styleUrls: ['./employee-login.component.css']
})
export class EmployeeLoginComponent implements OnInit {
  loginForm: FormGroup;

  // leaveForm: FormGroup = new FormGroup({
  //   leaveType: ['', Validators.required],
  //   startDate: ['', Validators.required],
  //   endDate: ['', Validators.required]
  // });

  // checkLeaveStatusForm: FormGroup = new FormGroup({
  //   leaveId: ['', Validators.required]
  // });

  // checkTaskForm: FormGroup = new FormGroup({
  //   taskId: ['', Validators.required]
  // });

  // updateTaskForm: FormGroup = new FormGroup({
  //   taskId: ['', Validators.required],
  //   taskStatus: ['', Validators.required]
  // });

  constructor(private fb: FormBuilder, private apiService: ApiService) { 
    this.loginForm = this.fb.group({
      leaveType: new FormControl('', Validators.required),
      startDate: new FormControl('', Validators.required),
      endDate: new FormControl('', Validators.required),
      leaveId: new FormControl('', Validators.required),
      taskId: new FormControl('', Validators.required),
      taskStatus: new FormControl('', Validators.required)
    });
  }

  ngOnInit() {}

  applyLeave() {
    const formData = this.loginForm.value;
    this.apiService.applyEmployeeLeave(formData).subscribe(
      (      response: any) => {
        console.log(response);
        // Handle the response here
      },
      (      error: any) => {
        console.error(error);
        alert("Failed to apply for leave.");
      }
    );
  }

  checkLeaveStatus() {
    const formData = this.loginForm.value;
    this.apiService.checkEmployeeLeaveStatus(formData.leaveId).subscribe(
      response => {
        console.log(response);
        // Handle the response here
      },
      error => {
        console.error(error);
        alert("Failed to check leave status.");
      }
    );
  }

  checkTask() {
    const formData = this.loginForm.value;
    this.apiService.checkEmployeeTask(formData.taskId).subscribe(
      (      response: any) => {
        console.log(response);
        // Handle the response here
      },
      (      error: any) => {
        console.error(error);
        alert("Failed to check task.");
      }
    );
  }

  updateTask() {
    const formData = this.loginForm.value;
    this.apiService.updateEmployeeTask(formData.taskId, formData.taskStatus).subscribe(
      (      response: any) => {
        console.log(response);
        // Handle the response here
      },
      (      error: any) => {
        console.error(error);
        alert("Failed to update task status.");
      }
    );
  }

  logout() {
    // Call AuthService logout method here
  }
}
