import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private isAuthenticated = false;

  constructor() { }

  setIsAuthenticated(value: boolean) {
    this.isAuthenticated = value;
  }

  setLoggedIn(value: boolean) {
    this.isAuthenticated = value;
  }

  isLoggedIn() {
    return this.isAuthenticated;
  }
}
