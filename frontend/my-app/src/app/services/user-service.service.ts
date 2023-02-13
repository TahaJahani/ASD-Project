import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { User } from '../Interfaces/User';

@Injectable({
  providedIn: 'root'
})
export class UserServiceService {
  private apiURL = 'http://localhost:3000/auth';

  constructor(private http : HttpClient) { }

  signUp(user : User) : Observable<any> {
    const url = `${this.apiURL}/sign-up`;
    return this.http.post(url, user);
  }
}
