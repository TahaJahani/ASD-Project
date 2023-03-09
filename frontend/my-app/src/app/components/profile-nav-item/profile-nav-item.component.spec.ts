import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ProfileNavItemComponent } from './profile-nav-item.component';

describe('ProfileNavItemComponent', () => {
  let component: ProfileNavItemComponent;
  let fixture: ComponentFixture<ProfileNavItemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ProfileNavItemComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ProfileNavItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
