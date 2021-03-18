import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ProprietarioEditComponent } from './proprietario-edit.component';

describe('ProprietarioEditComponent', () => {
  let component: ProprietarioEditComponent;
  let fixture: ComponentFixture<ProprietarioEditComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ProprietarioEditComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ProprietarioEditComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
