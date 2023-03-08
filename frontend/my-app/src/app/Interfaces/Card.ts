import { User } from './User';

export interface Card {
  id?: number;
  name: string;
  description?: string;
  assigned?: number;
  list: number;
  comments?: number[];
  labels?: number[];
  due_date: Date;
}
