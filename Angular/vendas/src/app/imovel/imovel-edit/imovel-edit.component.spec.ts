import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ImovelEditComponent } from './imovel-edit.component';

describe('ImovelEditComponent', () => {
  let component: ImovelEditComponent;
  let fixture: ComponentFixture<ImovelEditComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ImovelEditComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ImovelEditComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
