import { UiService } from './../../services/ui.service';
import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css'],
})
export class NavbarComponent implements OnInit {
  isLoggedIn: boolean = this.uiService.isLoggedIn;
  subscription: Subscription;

  constructor(private uiService: UiService) {
    this.subscription = this.uiService
      .getIsLoggedIn()
      .subscribe((isLoggedIn) => (this.isLoggedIn = isLoggedIn));
  }

  ngOnInit(): void {}
}
