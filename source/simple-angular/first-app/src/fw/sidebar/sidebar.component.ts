import { Component,OnInit } from '@angular/core';

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.css']
})
export class SidebarComponent implements OnInit {
  menu:string[] =[];
  constructor(){}
  

  ngOnInit(){
    this.menu=["google","amazon","yahoo"];
  }
}
