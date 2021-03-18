import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-cliente',
  templateUrl: './cliente.component.html',
  styleUrls: ['./cliente.component.css']
})

export class ClienteComponent implements OnInit {

  constructor(private router: Router,
              private route: ActivatedRoute) {}

  ngOnInit(){
  }

  onNovoCliente() {
    this.router.navigate(['novo'], {relativeTo: this.route});
  }
}
