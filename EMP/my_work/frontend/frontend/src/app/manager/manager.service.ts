import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ManagerService {

  private REST_API_SERVER = "http://localhost:9000/";

  constructor(private httpClient: HttpClient) { }

  public getEmployees(){
    return this.httpClient.get(`${this.REST_API_SERVER}/employees`);
  }

}
