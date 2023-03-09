import { UserServiceService } from './../../services/user-service.service';
import { User } from './../../Interfaces/User';
import { Component, OnInit, Input, ViewEncapsulation } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css'],
  // encapsulation: ViewEncapsulation.None,
})
export class ProfileComponent implements OnInit {
  hide = true;
  user!: User;

  first_name: string = '';
  last_name: string = '';
  email: string = '';
  password: string = '';
  confirm_password: string = '';

  emailPattern = new RegExp('^[a-z0-9._%+-]+@[a-z0-9.-]+.[a-z]{2,4}$');

  constructor(private userService: UserServiceService) {}

  ngOnInit(): void {
    this.userService.getMe().subscribe((data) => {
      console.log(data);
      this.user = data;
      this.first_name = this.user.first_name!;
      this.last_name = this.user.last_name!;
      this.email = this.user.email!;
    });
  }

  onSubmit() {
    console.log('onSubmit() called');
    if (this.email != '') {
      if (!this.emailPattern.test(this.email)) {
        alert('Invalid email address');
        return;
      }
    }
    if (this.password !== this.confirm_password) {
      alert('Password and Confirm Password do not match');
      return;
    }

    let updatedUser: User;
    if (this.password == '') {
      updatedUser = {
        first_name: this.first_name,
        last_name: this.last_name,
        email: this.email,
      };
    } else {
      updatedUser = {
        first_name: this.first_name,
        last_name: this.last_name,
        email: this.email,
        password: this.password,
      };
    }

    this.userService.updateUser(updatedUser).subscribe(
      (data) => {
        alert('Profile updated successfully');
      },
      (error) => {
        alert('Error updating profile');
      }
    );
  }
}
