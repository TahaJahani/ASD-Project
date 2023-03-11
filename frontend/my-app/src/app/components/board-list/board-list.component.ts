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
    const dialogRef = this.dialog.open(BoardDialogComponent, {
      data: { name: this.name },
    });
    dialogRef.afterClosed().subscribe((result) => {
      console.log('The dialog was closed');
      this.name = result;
      if (this.name) {
        let lastBoard = this.boards.find((board) => board.id === id);
        const boardToBeEdited: Board = {
          id: id,
          title: this.name,
          color: '#ffffff',
        };
        this.boardService.updateBoard(boardToBeEdited).subscribe(
          (board) => {
            alert('Board edited successfully');
            // replace the last boards with new one that the board title update
            this.boards.forEach((board) => {
              if (board.id === id) {
                board.title = this.name;
              }
            });
            // this.boards = this.boards.filter((board) => board.id !== id);
            // this.boards.push(boardToBeEdited);
            // this.bgColor.push('aliceblue');
          },
          (error) => {
            console.log(error);
            alert('Error editing board');
          }
        );
      }
    });
  }

  delete(id: number | undefined) {
    this.boardService.deleteBoard(id!).subscribe(
      (data) => {
        console.log(data);
        this.boards = this.boards.filter((board) => board.id !== id);
        this.bgColor = this.bgColor.filter((color) => color !== 'royalblue');
      },
      (error) => {
        console.log(error);
      }
    );
  }

  changeBgColor(i: number) {
    this.bgColor = this.bgColor.map((color, index) =>
      index === i ? 'royalblue' : 'aliceblue'
    );
    console.log(this.bgColor);
  }
}
