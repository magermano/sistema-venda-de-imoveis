import { Component, OnInit } from '@angular/core';
import { ImovelService } from '../imovel.service';

@Component({
  selector: 'app-imovel-lista',
  templateUrl: './imovel-lista.component.html',
  styleUrls: ['./imovel-lista.component.css']
})
export class ImovelListaComponent implements OnInit {
  listaImoveis: any;

  constructor(private service: ImovelService) { }

  ngOnInit(): void {
    this.service.getAll()
      .subscribe(imoveis => {
        this.listaImoveis = imoveis;
    });
  }
  onAtualizaImovel() {
    this.service.getAll()
      .subscribe(imoveis => {
        this.listaImoveis = imoveis;
    });
  }
}
