---
title: Resumen de ostep.org
date: 2022-03-20T22:15:35+00:00
tags: [fiuba, technical, cheatsheet]
---

# 5. Intrlude Process API

- `fork()`: returns 0 in the child and a pid in the parent
- `exec()` y amigos: reemplaza el proceso actual por otro. Nunca retorna.
- `wait()`: espera a un child process
- Esta API permite lanzar procesos con sus fp (eg stdi/o/e) modificados o algunas diferencias por el estilo.
- signals caught with `signal()` pueden ser enviadas a distintos procesos

# 6. Mechanism: Limited Direct Execution
## Problem 1: Restricted oerations
- limitación: user mode vs kernel mode (hardware supported)
- traps: hardware supported 
	- trap table: configured on boot. event -> kernel code address
	- trap instruction:
		1. push registers into per process kernel stack
		2. switch to kernel mode
		3. pass control to os
	- return-from-trap instruction 
## Problem 2: Switching between processes
- Cooperative approach: wait for traps (inseguro: loops infinitos!)
- Non-cooperative approach: timers set by the kernel on boot. Causan timer interrupts
- trap desde syscall es distinta a timer interrupt
- context switch: trap from A, return-from-trap  into B.

# 7. Scheduling: Introduction
- Round robin/time slicing: cambiar de proceso lo más frecuentemente posible
- SCTF (Shortest Time-to-Completion First) /SJF (Shortest Job First): Correr el más corto primero
- RR maximiza responsiveness, y maximiza average turnaround time. SCTF/SJF al contrario

# 8. Scheduling:  The Multi-Level Feedback Queue
- Rules of MLFQ:
	- **Rule 1:** If Priority(A) > Priority(B), A runs (B doesn’t).
	- **Rule 2:** If Priority(A) = Priority(B), A & B run in RR using the time slice (quantum length) of the given queue.
	- **Rule 3:** When a job enters the system, it is placed at the highest priority (the topmost queue).
	- **Rule 4:** Once a job uses up its time allotment at a given level (regardless of how many times it has given up the CPU), its priority is reduced (i.e., it moves down one queue).
	- **Rule 5:** After some time period S, move all the jobs in the system to the topmost queue.
- Starved job: permanece con poca prioridad

# 9. Scheduling: Proportional Share
- objetivo: asignar % cpu a cada proceso
- Lotería con 100 tickets repartidos de forma proporcional, sacás nro cada time slice
  - ticket currency: cada user tiene un cierto nro de tickets y se pueden convertir al nro de tickets global del sistema
  - ticket tranfer: un proceso da tickets a otro
  - ticket inflation: un proceso se da más/menos tickets a sí mismo. Sólo se puede usar si los procesos pueden confiarse entre sí
- más time slices -> más fairness
- stride scheduling: 
  - stride = N / tickets del proceso
  - cada slice:
    - proceso = el de menor pass
    - correr proceso
    - pass[proceso]+=stride[proceso]
  - stateful (problema introducir procesos)
  - proporción de ejecución exacta (fairness)
- Linux Completely Fair Scheduler:
  -
