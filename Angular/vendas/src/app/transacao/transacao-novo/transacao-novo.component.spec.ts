import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TransacaoNovoComponent } from './transacao-novo.component';

describe('TransacaoNovoComponent', () => {
  let component: TransacaoNovoComponent;
  let fixture: ComponentFixture<TransacaoNovoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TransacaoNovoComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TransacaoNovoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
