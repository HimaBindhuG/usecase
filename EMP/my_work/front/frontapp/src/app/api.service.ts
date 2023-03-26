import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private apiUrl = 'http://localhost:3000'; // Your API URL goes here

  constructor(private http: HttpClient) { }

  applyEmployeeLeave(formData: any) {
    return this.http.post(`${this.apiUrl}/employee/leave`, formData);
  }

  checkEmployeeLeaveStatus(leaveId: string) {
    return this.http.get(`${this.apiUrl}/employee/leave/${leaveId}`);
  }

  checkEmployeeTask(taskId: string) {
    return this.http.get(`${this.apiUrl}/employee/task/${taskId}`);
  }

  updateEmployeeTask(taskId: string, taskStatus: string) {
    const formData = { taskId, taskStatus };
    return this.http.put(`${this.apiUrl}/employee/task/${taskId}`, formData);
  }
}
