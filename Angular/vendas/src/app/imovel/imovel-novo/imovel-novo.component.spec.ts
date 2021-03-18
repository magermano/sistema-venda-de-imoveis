import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ImovelNovoComponent } from './imovel-novo.component';

describe('ImovelNovoComponent', () => {
  let component: ImovelNovoComponent;
  let fixture: ComponentFixture<ImovelNovoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ImovelNovoComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ImovelNovoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
