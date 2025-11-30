# An wave-function based quantum emulator on FPGA

Tuan Hai Vu, Vu Trung Duong Le, Hoai Luan Pham, Quoc Chuong Nguyen, Yasuhiko Nakashima

https://arxiv.org/abs/2411.04471

There are two value folders in this repo:
- Qsun: a wave-function based simulator, it's very simple. For any gate action, we looping through all elements on state-vector
- hardware (FPGA Qsun): the corresponding hardware accelerator for Qsun, design on ZCU102, the public codes are only the interface.
The detail design can be viewed in the paper.

## Plan for additions:
- Use the Qsun package to build some classic quantum circuits: Deutsch-Josza, Shor's algorithm, Simon's algorithm.
- If those can be done easily enough, see about engineering some means of building generic circuitry: maybe something interactive, or search for some way to upload files to Qsun?
- Also going to compare scalability and application support of Qsun against other big-name simulators