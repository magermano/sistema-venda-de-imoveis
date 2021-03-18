import { Component, OnInit } from '@angular/core';
import { ProprietarioService } from '../proprietario.service';

@Component({
  selector: 'app-proprietario-lista',
  templateUrl: './proprietario-lista.component.html',
  styleUrls: ['./proprietario-lista.component.css']
})
export class ProprietarioListaComponent implements OnInit {
  listaProprietarios: any;

  constructor(private service: ProprietarioService) { }

  ngOnInit(): void {
    this.service.getProprietarios()
      .subscribe(proprietarios => {
        this.listaProprietarios = proprietarios;
    });
  }
  onAtualizaProprietario() {
    this.service.getProprietarios()
      .subscribe(proprietarios => {
        this.listaProprietarios = proprietarios;
    });
  }
}
