import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Board } from '../../Interfaces/Board';

const httpOptions = {
  headers: new HttpHeaders({}),
};

@Injectable({
  providedIn: 'root',
})
export class BoardService {
  private apiURL = 'http://37.32.13.83:8000/workspace/board';

  constructor(private http: HttpClient) {}

  createBoard(board: Board): Observable<any> {
    const url = `${this.apiURL}/create`;
    let token = `token ${localStorage.getItem('token')}`;
    httpOptions.headers = httpOptions.headers.set('Authorization', token);

    return this.http.post(url, board, httpOptions);
  }

  getBoards(): Observable<any> {
    const url = `${this.apiURL}/list`;
    let token = `token ${localStorage.getItem('token')}`;
    httpOptions.headers = httpOptions.headers.set('Authorization', token);

    return this.http.get(url, httpOptions);
  }

  deleteBoard(id: number): Observable<any> {
    const url = `${this.apiURL}/delete/${id}`;
    let token = `token ${localStorage.getItem('token')}`;
    httpOptions.headers = httpOptions.headers.set('Authorization', token);

    return this.http.delete(url, httpOptions);
  }

  updateBoard(board: Board): Observable<any> {
    const url = `${this.apiURL}/update/${board.id}`;
    let token = `token ${localStorage.getItem('token')}`;
    httpOptions.headers = httpOptions.headers.set('Authorization', token);

    let newBoard = {
      new_title: board.title,
      new_color: '#ffffff',
    };
    return this.http.put(url, newBoard, httpOptions);
  }
}
