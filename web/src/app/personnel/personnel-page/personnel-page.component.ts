import { Component } from '@angular/core';
import { Person } from '../../core/models/person.model'
import { PersonView } from '../shared/personview.model';

@Component({
  selector: 'sc-personnel-page',
  templateUrl: './personnel-page.component.html',
  styleUrls: ['./personnel-page.component.css']
})
export class PersonnelPageComponent {
  persons: PersonView[];
  assigned_orgs: string[];
  quals: string[];
  qual_options: string[];
  isEditable: boolean[];

  constructor() {
    const person_dtos: Person[] = [
      {
        id: 1,
        name: "Keeler, Joshua",
        assigned_org: "",
        quals: ["Operations Supervisor"]
      },
      {
        id: 2,
        name: "Van Epps, Lucas",
        assigned_org: "O",
        quals: ["RSU Controller", "RSU Observer"]
      }
    ]

    this.quals = [
      'Operations Supervisor', 'SOF', 'RSU Controller', 'RSU Observer', 'IPC Pilot', 'FPC Pilot', 'FCF Pilot', 'PIT IP', 'SEFE'
    ];

    this.qual_options = ['', 'X']

    this.persons = person_dtos.map(person_dto => {
      const mapped_quals = new Map(this.quals.map(qual => {
        let val = '';

        if (person_dto.quals.includes(qual))
          val = 'X';

        return [qual, val] 
      }));


      const person_view: PersonView = {
        id: person_dto.id,
        name: person_dto.name,
        assigned_org: person_dto.assigned_org,
        quals: mapped_quals
      };

      console.log(person_view.quals);

      return person_view;
    });

    this.assigned_orgs = [
      ' ', 'M', 'N', 'O', 'P', 'X'
    ];

    this.isEditable = this.persons.map(() => {
      return false;
    })
  }

  onEdit(row: number) {
    this.isEditable[row] = true;
  }

  onSave(row: number) {
    this.isEditable[row] = false;
    console.log('Updating: ' + this.persons[row].name);
    console.log(this.persons[row]);

    /*console.log(data);
    const httpRequest = new XMLHttpRequest();
    httpRequest.onreadystatechange = () => {
        if (httpRequest.readyState === XMLHttpRequest.DONE) {
            if (httpRequest.status === 200) {
                console.log("Data saved");
            }
        }
    };

    httpRequest.open('POST', '/personnel/' + data.person_id);
    httpRequest.setRequestHeader('Content-Type', 'application/json');

    const csrfToken = Cookies.get('csrftoken');
    httpRequest.setRequestHeader('X-CSRFToken', csrfToken);

    httpRequest.send(JSON.stringify(data));*/
  }
}