import { User } from './../../Interfaces/User';
import { Component, OnInit } from '@angular/core';
import { UserServiceService } from '../../services/user-service.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
})
export class LoginComponent implements OnInit {
  constructor(
    private userService: UserServiceService,
    private router: Router
  ) {}

  ngOnInit(): void {}

  signIn(user: User) {
    this.userService.signIn(user).subscribe(
      (data) => {
        console.log(data);
        this.userService.userLoggedIn = user;
        // this.router.navigate(['/boards']);
      },
      (error) => {
        console.log('error: ', error);
        console.log(this.userService.userLoggedIn == null);
      }
    );
  }
}
