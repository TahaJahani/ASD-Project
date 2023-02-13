import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { User } from '../Interfaces/User';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json'
  })
}

@Injectable({
  providedIn: 'root'
})
export class UserServiceService {
  private apiURL = 'http://37.32.13.83/auth';

  constructor(private http : HttpClient) { }

  signUp(user : User) : Observable<any> {
    const url = `${this.apiURL}/sign-up`;
    return this.http.post(url, user, httpOptions);
  }
}
