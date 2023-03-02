import { Card } from './Card';
import { User } from './User';
export interface Board {
    id?: number;
    title: string;
    description: string;
    color_red?: number;
    color_green?: number;
    color_blue?: number;
    owner: User;
    members?: User[];
    cards?: Card[];
}