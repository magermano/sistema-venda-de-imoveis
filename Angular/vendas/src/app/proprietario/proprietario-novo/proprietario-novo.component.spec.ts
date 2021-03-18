import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ProprietarioNovoComponent } from './proprietario-novo.component';

describe('ProprietarioNovoComponent', () => {
  let component: ProprietarioNovoComponent;
  let fixture: ComponentFixture<ProprietarioNovoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ProprietarioNovoComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ProprietarioNovoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
