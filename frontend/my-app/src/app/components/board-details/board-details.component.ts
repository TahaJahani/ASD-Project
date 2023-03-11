import { List } from './../../Interfaces/List';
import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { BoardService } from 'src/app/services/workspace/board.service';
import { Board } from '../../Interfaces/Board';
import { ListService } from 'src/app/services/workspace/list.service';
import {
  MatDialog,
  MAT_DIALOG_DATA,
  MatDialogRef,
} from '@angular/material/dialog';
import { ListDialogComponent } from '../list-dialog/list-dialog.component';

@Component({
  selector: 'app-board-details',
  templateUrl: './board-details.component.html',
  styleUrls: ['./board-details.component.css'],
})
export class BoardDetailsComponent implements OnInit {
  board: Board | undefined;
  lists: List[] | undefined;
  name!: string;

  @Output() boardChange = new EventEmitter<any>();

  // constructor
  constructor(
    private route: ActivatedRoute,
    private dialog: MatDialog,
    private boardService: BoardService,
    private listService: ListService
  ) {}

  ngOnInit(): void {
    this.route.params.subscribe((routeParams) => {
      this.boardService.getBoards().subscribe((data) => {
        this.board = data.find(
          (board: Board) => board.id === Number(routeParams['id'])
        );
        this.listService.getLists(this.board?.id!).subscribe(
          (data) => {
            this.lists = data;
          },
          (error) => {
            console.log(error);
          }
        );
      });
    });
  }

  openDialog(): void {
    const dialogRef = this.dialog.open(ListDialogComponent, {
      data: { name: this.name },
    });
    dialogRef.afterClosed().subscribe((result) => {
      console.log('The dialog was closed');
      this.name = result;
      if (this.name) {
        const listToBeCreated: List = {
          title: this.name,
          board_id: this.board?.id!,
        };
        this.listService.createList(listToBeCreated).subscribe(
          (board) => {
            alert('List created successfully');
            this.lists?.push(listToBeCreated);
          },
          (error) => {
            console.log(error);
            alert('Error creating board');
          }
        );
      }
    });
  }
}
