import { UserServiceService } from './../../services/user-service.service';
import { LocalStorageService } from './../../services/local-storage.service';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { UiService } from './../../services/ui.service';

@Component({
  selector: 'app-logout',
  templateUrl: './logout.component.html',
  styleUrls: ['./logout.component.css'],
})
export class LogoutComponent implements OnInit {
  constructor(
    private localStorageService: LocalStorageService,
    private userService: UserServiceService,
    private uiService: UiService,
    private router: Router
  ) {}

  ngOnInit(): void {
    if (this.uiService.isLoggedIn === false) {
      this.router.navigate(['/login']);
      return;
    }
    this.userService.logout().subscribe(
      (data) => {
        console.log(data);
        this.localStorageService.remove('token');
        alert('You have been logged out!');
        this.uiService.changeIsLoggedIn();
        this.router.navigate(['/']);
      },
      (error) => {
        console.log('error: ', error);
        alert('Something went wrong!');
        this.router.navigate(['/boards']);
      }
    );
  }
}
