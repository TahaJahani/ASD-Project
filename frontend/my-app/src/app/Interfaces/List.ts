import { Card } from './Card';

export interface List {
  id?: number;
  title?: string;
  description?: string;
  board_id?: number;
  cards?: Card[];
}
