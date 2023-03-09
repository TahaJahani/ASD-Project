import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-navbar-item',
  templateUrl: './navbar-item.component.html',
  styleUrls: ['./navbar-item.component.css'],
})
export class NavbarItemComponent {
  @Input() text!: string;
  @Input() link!: string;
  @Input() color: string = 'royalblue';

  @Output() itemClicked = new EventEmitter();

  constructor() {}

  onClick() {
    this.itemClicked.emit();
  }
}
