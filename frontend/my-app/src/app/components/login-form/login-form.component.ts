import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { User } from '../../Interfaces/User';

@Component({
  selector: 'app-login-form',
  templateUrl: './login-form.component.html',
  styleUrls: ['./login-form.component.css'],
})
export class LoginFormComponent implements OnInit {
  @Output() login: EventEmitter<User> = new EventEmitter();

  username: string = '';
  password: string = '';

  constructor() {}

  ngOnInit(): void {}

  onSubmit(): void {
    if (this.username === '' || this.password === '') {
      alert('Please fill in all fields');
      return;
    }

    const requestedLoginUser: User = {
      username: this.username,
      password: this.password,
    };

    this.login.emit(requestedLoginUser);
  }
}
