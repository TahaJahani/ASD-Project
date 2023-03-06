import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Board } from '../../Interfaces/Board';
import { dummyData } from '../../Interfaces/Board';

@Component({
  selector: 'app-board-details',
  templateUrl: './board-details.component.html',
  styleUrls: ['./board-details.component.css'],
})
export class BoardDetailsComponent implements OnInit {
  board: Board | undefined;

  @Output() boardChange = new EventEmitter<any>();

  // constructor
  constructor(private route: ActivatedRoute) {}

  ngOnInit(): void {
    this.route.params.subscribe((routeParams) => {
      this.board = dummyData.find(
        (board) => board.id === Number(routeParams['id'])
      );
    });
  }
}
