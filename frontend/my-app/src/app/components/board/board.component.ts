import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { Board } from '../../Interfaces/Board';

@Component({
  selector: 'app-board',
  templateUrl: './board.component.html',
  styleUrls: ['./board.component.css']
})
export class BoardComponent implements OnInit {
  @Input() board !: Board;

  constructor() { }

  ngOnInit() {
  }

  GetLuminance() {
    let r: number = Number(this.board.color_red) * 0.2126;
    let g: number = Number(this.board.color_green) * 0.7152;
    let b: number = Number(this.board.color_blue) * 0.0722;
    let luminance: number = r + g + b;
    let textColor: string = luminance > 127 ? 'black' : 'white';
    return textColor;
  }
  
  
}
