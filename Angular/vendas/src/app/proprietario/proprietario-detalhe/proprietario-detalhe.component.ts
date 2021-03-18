import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Params, Router } from '@angular/router';
import { ProprietarioService } from '../proprietario.service';

@Component({
  selector: 'app-proprietario-detalhe',
  templateUrl: './proprietario-detalhe.component.html',
  styleUrls: ['./proprietario-detalhe.component.css']
})
export class ProprietarioDetalheComponent implements OnInit {
  isExclusao = false;
  proprietario: any;
  id = this.route.snapshot.params['id'];
  mensagemErro = '';

  constructor(private service: ProprietarioService,
              private route: ActivatedRoute,
              private router: Router) { }

  ngOnInit(): void {
  this.service.getProprietarioByID(this.id)
      .subscribe(proprietario => {
        this.proprietario = proprietario;
      });
  this.route.params
      .subscribe((params: Params) => {
        this.id = params['id'];
        this.service.getProprietarioByID(this.id)
      .subscribe(proprietario => {
        this.proprietario = proprietario;
      });
      });
  }

  onDelete() {
    this.mensagemErro = '';
    this.service.deleteProprietario(this.id).subscribe(proprietario => {
      console.log(proprietario);
      this.router.navigate(['proprietarios']);
    },
      error => {
      this.mensagemErro = error.name;
      });
  }

  onEdit() {
    this.router.navigate(['proprietarios', 'edit', this.id]);
  }

  onPerguntar() {
    this.isExclusao = true;
  }

  onRetornar() {
    this.isExclusao = false;
  }

  onClearError() {
    this.mensagemErro = '';
  }
}
