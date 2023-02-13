import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import {User} from '../../Interfaces/User';

@Component({
  selector: 'app-register-form',
  templateUrl: './register-form.component.html',
  styleUrls: ['./register-form.component.css']
})
export class RegisterFormComponent implements OnInit {
  @Output() register : EventEmitter<User> = new EventEmitter();

  email: string = '';
  username: string = '';
  firstName:  string = '';
  lastName: string = '';
  password: string = '';
  confirmPassword: string = '';
  emailPattern = new RegExp('^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$');
  constructor() { }

  ngOnInit(): void {}

  onSubmit(): void {
    if (this.password !== this.confirmPassword) {
      alert('Password and Confirm Password do not match');
      return;
    } 
    if (this.email === '' || this.username === '' || this.password === '' || this.confirmPassword === '' || this.firstName === '' || this.lastName === '') {
      alert('Please fill in all fields');
      return;
    }
    if (this.password.length < 8) {
      alert('Password must be at least 8 characters');
      return;
    }
    if (this.username.length < 3) {
      alert('Username must be at least 3 characters');
      return;
    }
    if (!this.emailPattern.test(this.email)) {
      alert('Invalid email address');
      return;
    }

    const newUser : User = {
      email: this.email,
      username: this.username,
      password: this.password,
      first_name: this.firstName,
      last_name: this.lastName,
    }

    this.register.emit(newUser);

    // this.password = '';
    // this.confirmPassword = '';
  }
}
