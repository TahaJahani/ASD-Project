import { Card } from './Card';
import { User } from './User';
export interface Board {
  id?: number;
  title: string;
  description: string;
  owner: User;
  members?: User[];
  cards?: Card[];
}

export const dummyData: Board[] = [
  {
    id: 1,
    title: 'Board 1',
    description: 'This is the first board',
    owner: {
      id: 1,
      username: 'user1',
      email: '',
      first_name: 'user1firstname',
      last_name: 'user1lastname',
    },
    members: [
      {
        id: 1,
        username: 'user1',
        email: '',
        first_name: 'user1firstname',
        last_name: 'user1lastname',
      },
      {
        id: 2,
        username: 'user2',
        email: '',
        first_name: 'user2firstname',
        last_name: 'user2lastname',
      },
    ],
    cards: [
      {
        id: 1,
        name: 'Card 1',
        description: 'This is the first card',
        assigned: {
          id: 1,
          username: 'user1',
          email: '',
          first_name: 'user1firstname',
          last_name: 'user1lastname',
        },
        board: 1,
        due_date: new Date(),
      },
      {
        id: 2,
        name: 'Card 2',
        description: 'This is the second card',
        assigned: {
          id: 2,
          username: 'user2',
          email: '',
          first_name: 'user2firstname',
          last_name: 'user2lastname',
        },
        board: 1,
        due_date: new Date(),
      },
    ],
  },
  {
    id: 2,
    title: 'Board 2',
    description:
      'This is the second board and it is so dummy and no use is for it',
    owner: {
      id: 2,
      username: 'user2',
      email: '',
      first_name: 'user2firstname',
      last_name: 'user2lastname',
    },
    members: [
      {
        id: 2,
        username: 'user2',
        email: '',
        first_name: 'user2firstname',
        last_name: 'user2lastname',
      },
      {
        id: 3,
        username: 'user3',
        email: '',
        first_name: 'user3firstname',
        last_name: 'user3lastname',
      },
    ],
    cards: [
      {
        id: 3,
        name: 'Card 3',
        description: 'This is the third card',
        assigned: {
          id: 3,
          username: 'user3',
          email: '',
          first_name: 'user3firstname',
          last_name: 'user3lastname',
        },
        board: 2,
        due_date: new Date(),
      },
    ],
  },
];
