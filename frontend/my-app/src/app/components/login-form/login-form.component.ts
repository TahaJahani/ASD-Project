import { Component, OnInit, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-login-form',
  templateUrl: './login-form.component.html',
  styleUrls: ['./login-form.component.css']
})
export class LoginFormComponent implements OnInit {
  @Output() login : EventEmitter<any> = new EventEmitter();

  username: string = '';
  password: string = '';

  constructor() { }

  ngOnInit(): void {
  }

  onSubmit(): void {
    if (this.username === '' || this.password === '') {
      alert('Please fill in all fields');
      return;
    }

    alert('received username: ' + this.username + ' and password: ' + this.password + '');
    // this.login.emit({username: this.username, password: this.password});
  }

}
