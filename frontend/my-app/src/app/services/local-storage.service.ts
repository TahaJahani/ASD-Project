import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class LocalStorageService {
  constructor() {}

  set(key: string, value: string) {
    localStorage.setItem(key, value);
  }

  get(key: string): string {
    let value = localStorage.getItem(key);
    return value == null ? '' : value;
  }

  remove(key: string) {
    localStorage.removeItem(key);
  }
}
