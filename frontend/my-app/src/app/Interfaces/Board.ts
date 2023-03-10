import { Card } from './Card';
import { List } from './List';
import { User } from './User';
export interface Board {
  id?: number;
  title?: string;
  color?: string;
  description?: string;
  owner?: User;
  members?: User[];
  lists?: List[];
}
