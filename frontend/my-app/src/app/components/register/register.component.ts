import { LocalStorageService } from './../../services/local-storage.service';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { UserServiceService } from '../../services/user-service.service';
import { User } from '../../Interfaces/User';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css'],
})
export class RegisterComponent implements OnInit {
  loading: boolean = false;

  constructor(
    private localStorageService: LocalStorageService,
    private userService: UserServiceService,
    private router: Router
  ) {}

  ngOnInit(): void {
    if (this.localStorageService.get('token')) {
      this.router.navigate(['/boards']);
    }
  }

  signUp(user: User) {
    this.loading = true;
    this.userService.signUp(user).subscribe(
      (res) => {
        this.loading = false;
        console.log(res);
        alert('User created successfully');
        this.router.navigate(['/login']);
      },
      (err) => {
        this.loading = false;
        console.log(err);
        alert('Error creating user');
      }
    );
  }
}
