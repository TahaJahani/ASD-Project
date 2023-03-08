import { Injectable } from '@angular/core';
import { Subject, Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class UiService {
  public isLoggedIn: boolean = localStorage.getItem('token') ? true : false;
  private subject = new Subject<any>();

  constructor() {}

  changeIsLoggedIn(): void {
    this.isLoggedIn = localStorage.getItem('token') ? true : false;
    this.subject.next(this.isLoggedIn);
  }

  getIsLoggedIn(): Observable<any> {
    return this.subject.asObservable();
  }
}
