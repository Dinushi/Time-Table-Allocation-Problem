# Time-Table-Allocation-Problem
A constraint satisfaction problem (CSP) to develop a timetable for a semester.


**Modeling the problem as a constraint satisfaction problem**

***Variables*** –The subjects we want to assign to a time slot

***Domains*** – The time slots each subject is possible to allocate and rooms

***Constraints***
          - A subject can be assigned to only one of its possible time slots.
          - Two compulsory subjects cannot be in the same time slot.
          - optional subjects may be allocated to same slot with another subject.
          - Two subjects who are assigned to same slot cannot be assigned to same room.

