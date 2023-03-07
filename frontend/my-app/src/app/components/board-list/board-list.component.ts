import { dummyData, Board } from './../../Interfaces/Board';
import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-board-list',
  templateUrl: './board-list.component.html',
  styleUrls: ['./board-list.component.css'],
})
export class BoardListComponent implements OnInit {
  boards: Board[] = dummyData;
  // array bgColor with the same length as the array boards
  bgColor: string[] = new Array(this.boards.length).fill('aliceblue');

  constructor() {}

  ngOnInit(): void {}

  changeBgColor(i: number) {
    this.bgColor = this.bgColor.map((color, index) =>
      index === i ? 'royalblue' : 'aliceblue'
    );
    console.log(this.bgColor);
  }
}
