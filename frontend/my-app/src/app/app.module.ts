import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { ResolveFn, RouterModule, Routes } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { HttpClientModule, HttpClientJsonpModule } from '@angular/common/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { MatGridListModule } from '@angular/material/grid-list';
import { MatCardModule } from '@angular/material/card';
import { MatListModule } from '@angular/material/list';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatIconModule } from '@angular/material/icon';
import { MatToolbarModule } from '@angular/material/toolbar';

import { AppComponent } from './app.component';
import { NavbarComponent } from './components/navbar/navbar.component';
import { NavbarItemComponent } from './components/navbar-item/navbar-item.component';
import { LoginComponent } from './components/login/login.component';
import { HomepageComponent } from './components/homepage/homepage.component';
import { RegisterComponent } from './components/register/register.component';
import { LoginFormComponent } from './components/login-form/login-form.component';
import { RegisterFormComponent } from './components/register-form/register-form.component';
import { BoardListComponent } from './components/board-list/board-list.component';
import { BoardDetailsComponent } from './components/board-details/board-details.component';

const resolvedBoardTitle: ResolveFn<string> = () =>
  Promise.resolve('Board detail');

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    NavbarItemComponent,
    LoginComponent,
    HomepageComponent,
    RegisterComponent,
    LoginFormComponent,
    RegisterFormComponent,
    BoardListComponent,
    BoardDetailsComponent,
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    HttpClientJsonpModule,
    RouterModule.forRoot([
      {
        path: '',
        title: 'Trel-low',
        component: HomepageComponent,
      },
      {
        path: 'login',
        title: 'trel-login',
        component: LoginComponent,
      },
      {
        path: 'register',
        title: 'tregister',
        component: RegisterComponent,
      },
      {
        path: 'boards',
        title: 'tre-boards',
        component: BoardListComponent,
        children: [
          {
            path: ':id',
            title: resolvedBoardTitle,
            component: BoardDetailsComponent,
          },
        ],
      },
      // { path: 'boards/:id', component: BoardDetailsComponent },
    ]),
    BrowserAnimationsModule,

    MatCardModule,
    MatGridListModule,
    MatListModule,
    MatSidenavModule,
    MatIconModule,
    MatToolbarModule,
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
