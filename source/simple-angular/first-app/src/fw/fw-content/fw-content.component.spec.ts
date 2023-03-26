import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FwContentComponent } from './fw-content.component';

describe('FwContentComponent', () => {
  let component: FwContentComponent;
  let fixture: ComponentFixture<FwContentComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ FwContentComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(FwContentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
