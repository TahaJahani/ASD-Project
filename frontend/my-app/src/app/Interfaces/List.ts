import { Card } from './Card';

export interface List {
  id?: number;
  name: string;
  description: string;
  board: number;
  cards?: Card[];
}
