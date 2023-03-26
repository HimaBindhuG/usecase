import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ManagerService } from './manager.service';

@Component({
  selector: 'app-manager',
  templateUrl: './manager.component.html',
  styleUrls: ['./manager.component.css']
})
export class ManagerComponent implements OnInit {

  employees: any[] = [];

  constructor(private router: Router, private managerService: ManagerService) { }

  ngOnInit(): void {
    this.managerService.getEmployees()
      .subscribe((data: any) => {
        this.employees = data;
      }, (err) => {
        console.log(err);
      });
  }

  logout(): void {
    // Add any logout logic here
    this.router.navigate(['/login']);
  }

}
