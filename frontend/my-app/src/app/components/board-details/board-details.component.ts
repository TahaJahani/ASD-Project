import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { BoardService } from 'src/app/services/workspace/board.service';
import { Board } from '../../Interfaces/Board';

@Component({
  selector: 'app-board-details',
  templateUrl: './board-details.component.html',
  styleUrls: ['./board-details.component.css'],
})
export class BoardDetailsComponent implements OnInit {
  board: Board | undefined;

  @Output() boardChange = new EventEmitter<any>();

  // constructor
  constructor(
    private route: ActivatedRoute,
    private boardService: BoardService
  ) {}

  ngOnInit(): void {
    this.route.params.subscribe((routeParams) => {
      this.boardService.getBoards().subscribe((data) => {
        this.board = data.find(
          (board: Board) => board.id === Number(routeParams['id'])
        );
        // this.board = dummyData.find(
        //   (board) => board.id === Number(routeParams['id'])
        // );
      });
    });
  }
}
