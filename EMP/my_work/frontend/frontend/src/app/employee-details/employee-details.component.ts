import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-employee-details',
  templateUrl: './employee-details.component.html',
  styleUrls: ['./employee-details.component.css']
})
export class EmployeeDetailsComponent implements OnInit {
  employee: any;

  constructor(private route: ActivatedRoute, private http: HttpClient) { }

  ngOnInit(): void {
    // Get the emp_id parameter from the route
    const empId = this.route.snapshot.paramMap.get('id');

    // Make a GET request to retrieve the employee details
    this.http.get<any>(`http://localhost:3000/employees/${empId}`).subscribe((response) => {
      this.employee = response;
    });
  }
}
