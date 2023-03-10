import { BoardService } from './../../services/workspace/board.service';
import { Board } from './../../Interfaces/Board';
import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import {
  MatDialog,
  MAT_DIALOG_DATA,
  MatDialogRef,
} from '@angular/material/dialog';
import { BoardDialogComponent } from '../board-dialog/board-dialog.component';

@Component({
  selector: 'app-board-list',
  templateUrl: './board-list.component.html',
  styleUrls: ['./board-list.component.css'],
})
export class BoardListComponent implements OnInit {
  boards!: Board[];
  name!: string;
  // array bgColor with the same length as the array boards
  bgColor!: string[];
  // new Array(this.boards.length).fill('aliceblue');

  constructor(public dialog: MatDialog, private boardService: BoardService) {}

  ngOnInit(): void {
    this.boardService.getBoards().subscribe(
      (data) => {
        this.boards = data;
        this.bgColor = new Array(this.boards.length).fill('aliceblue');
      },
      (error) => {
        console.log(error);
      }
    );
  }

  openDialog(): void {
    const dialogRef = this.dialog.open(BoardDialogComponent, {
      data: { name: this.name },
    });
    dialogRef.afterClosed().subscribe((result) => {
      console.log('The dialog was closed');
      this.name = result;
      if (this.name) {
        const boardToBeCreated: Board = {
          title: this.name,
          color: '#ffffff',
        };
        this.boardService.createBoard(boardToBeCreated).subscribe(
          (board) => {
            alert('Board created successfully');
            this.boards.push(boardToBeCreated);
            this.bgColor.push('aliceblue');
          },
          (error) => {
            console.log(error);
            alert('Error creating board');
          }
        );
      }
    });
  }

  edit(id: number | undefined) {
    console.log('edit board with id: ' + id);
  }

  delete(id: number | undefined) {
    console.log('delete board with id: ' + id);
  }

  changeBgColor(i: number) {
    this.bgColor = this.bgColor.map((color, index) =>
      index === i ? 'royalblue' : 'aliceblue'
    );
    console.log(this.bgColor);
  }
}
