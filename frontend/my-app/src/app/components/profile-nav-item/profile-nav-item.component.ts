import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-profile-nav-item',
  templateUrl: './profile-nav-item.component.html',
  styleUrls: ['./profile-nav-item.component.css'],
})
export class ProfileNavItemComponent implements OnInit {
  @Input() username: string = 'username';

  constructor() {}

  ngOnInit(): void {}
}
