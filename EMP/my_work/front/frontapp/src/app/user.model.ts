export class Admin {
    constructor(
      public name: string = '',
      public email: string = '',
      public password: string = '',
      public dept: string = '',
      public address: string = '',
      public gender: string = '',
      public dob: string = '',
      public phone: string = '',
      public posting: string = ''
    ) {}
  }
  
  export class Employee {
    constructor(
        public emp_name?:string,
        public email?:string,
        public password?:string,
        public dept ?:string,
        public address?:string,
        public gender?:string,
        public dob?:string,
        public phone?:string,
        public posting?:string,
        public emp_mag_id:number=1
    ){}
    
  }
  export class Manager {
    constructor(
        public mag_name:string= '',
        public email:string= '',
        public password:string= '',
        public dept :string= '',
        public address:string= '',
        public gender:string= '',
        public dob:string= '',
        public phone:string= '',
        public posting:string= '',
    ){}
    
  }
  