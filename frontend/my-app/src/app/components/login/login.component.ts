import { User } from './../../Interfaces/User';
import { Component, OnInit } from '@angular/core';
import { UserServiceService } from '../../services/user-service.service';
import { UiService } from './../../services/ui.service';
import { Router } from '@angular/router';
import { LocalStorageService } from '../../services/local-storage.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
})
export class LoginComponent implements OnInit {
  loading: boolean = false;

  constructor(
    private userService: UserServiceService,
    private localStorageService: LocalStorageService,
    private uiService: UiService,
    private router: Router
  ) {}

  ngOnInit(): void {
    if (this.localStorageService.get('token')) {
      this.router.navigate(['/boards']);
    }
  }

  signIn(user: User) {
    this.loading = true;
    this.userService.signIn(user).subscribe(
      (data) => {
        this.loading = false;
        console.log(data);
        alert(`Welcome ${user.username}!`);
        this.localStorageService.set('token', data.token);
        this.uiService.changeIsLoggedIn();
        this.router.navigate(['/boards']);
      },
      (error) => {
        this.loading = false;
        console.log('error: ', error);
        alert('Wrong Username Password');
        this.router.navigate(['/login']);
      }
    );
  }
}
