import { Card } from './Card';
import { List } from './List';
import { User } from './User';
export interface Board {
  id?: number;
  title: string;
  description: string;
  owner: User;
  members?: User[];
  lists?: List[];
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
    lists: [
      {
        id: 1,
        name: 'ToDo',
        description: 'Things to do',
        board: 1,
        cards: [
          {
            id: 1,
            name: 'Card 1',
            description: 'This is the first card',
            assigned: 1,
            list: 1,
            due_date: new Date(),
          },
          {
            id: 2,
            name: 'Card 2',
            description: 'This is the second card',
            assigned: 2,
            list: 1,
            due_date: new Date(),
          },
        ],
      },
      {
        id: 2,
        name: 'Doing',
        description: 'Things doing',
        board: 1,
        cards: [
          {
            id: 4,
            name: 'Card 4',
            description: 'This is the fourth card',
            assigned: 1,
            list: 2,
            due_date: new Date(),
          },
        ],
      },
      {
        id: 3,
        name: 'Done',
        description: 'Things done',
        board: 1,
        cards: [],
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
    lists: [
      {
        id: 4,
        name: 'ToDo',
        description: 'Things to do',
        board: 2,
        cards: [],
      },
      {
        id: 5,
        name: 'Doing',
        description: 'Things doing',
        board: 2,
        cards: [],
      },
      {
        id: 6,
        name: 'Done',
        description: 'Things done',
        board: 2,
        cards: [
          {
            id: 3,
            name: 'Card 3',
            description: 'This is the third card',
            assigned: 1,
            list: 6,
            due_date: new Date(),
          },
        ],
      },
    ],
  },
];
