import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Params, Router } from '@angular/router';
import { ImovelService } from '../imovel.service';

@Component({
  selector: 'app-imovel-detalhe',
  templateUrl: './imovel-detalhe.component.html',
  styleUrls: ['./imovel-detalhe.component.css']
})
export class ImovelDetalheComponent implements OnInit {
  isExclusao = false;
  imovel: any;
  id = this.route.snapshot.params['id'];
  mensagemErro = '';

  constructor(private service: ImovelService,
              private route: ActivatedRoute,
              private router: Router) { }

  ngOnInit(): void {
  this.service.getByID(this.id)
      .subscribe(imovel => {
        this.imovel = imovel;
      });
  this.route.params
      .subscribe((params: Params) => {
        this.id = params['id'];
        this.service.getByID(this.id)
      .subscribe(imovel => {
        this.imovel = imovel;
      });
      });
  }

  onDelete() {
    this.mensagemErro = '';
    this.service.delete(this.id).subscribe(imovel => {
      console.log(imovel);
      this.router.navigate(['imoveis']);
    },
      error => {
      this.mensagemErro = error.name;
      });
  }

  onEdit() {
    this.router.navigate(['imoveis', 'edit', this.id]);
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
