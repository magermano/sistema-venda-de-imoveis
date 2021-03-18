import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TransacaoDetalheComponent } from './transacao-detalhe.component';

describe('TransacaoDetalheComponent', () => {
  let component: TransacaoDetalheComponent;
  let fixture: ComponentFixture<TransacaoDetalheComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TransacaoDetalheComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TransacaoDetalheComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
