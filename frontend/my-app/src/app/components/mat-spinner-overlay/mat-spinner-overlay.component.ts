import { ProgressSpinnerMode } from '@angular/material/progress-spinner';
import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-mat-spinner-overlay',
  templateUrl: './mat-spinner-overlay.component.html',
  styleUrls: ['./mat-spinner-overlay.component.css'],
})
export class MatSpinnerOverlayComponent implements OnInit {
  constructor() {}

  @Input() value: number = 250;
  @Input() diameter: number = 200;
  @Input() mode: ProgressSpinnerMode = 'indeterminate';
  @Input() strokeWidth: number = 10;
  @Input() overlay: boolean = false;
  @Input() color: string = 'primary';

  @Input() message: string = 'Loading...';

  ngOnInit() {}
}
