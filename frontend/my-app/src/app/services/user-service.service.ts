import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { User } from '../Interfaces/User';

const httpOptions = {
  headers: new HttpHeaders({}),
};

@Injectable({
  providedIn: 'root',
})
export class UserServiceService {
  private apiURL = 'http://37.32.13.83/auth';

  constructor(private http: HttpClient) {}

  signUp(user: User): Observable<any> {
    const url = `${this.apiURL}/sign-up`;
    return this.http.post(url, user);
  }

  signIn(user: User): Observable<any> {
    const url = `${this.apiURL}/login`;
    return this.http.post(url, user);
  }

  logout(): Observable<any> {
    const url = `${this.apiURL}/logout`;
    let token = `token ${localStorage.getItem('token')}`;
    httpOptions.headers = httpOptions.headers.set('Authorization', token);

    return this.http.post(url, {}, httpOptions);
  }
}
