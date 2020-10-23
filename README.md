<!-- Prpject Title and Logo -->
<br />
<p align="center">
    <img src="images/Logo_Image.png" alt="Logo" width="100" height="100">
  </a>

  <h3 align="center">PK Toolbox</h3>

  <p align="center">
    A Pharmokinetic Model and Visualisation Toolbox!
    <br />
    <a href="https://pk-toolbox.readthedocs.io"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/oj-tooth/PK-Toolbox">View Demo</a>
    ·
    <a href="https://github.com/oj-tooth/PK-Toolbox/issues">Report Issue</a>
    ·
  </p>
</p>

<!-- Table of Contents -->
## Table of Contents

* [About the PK Toolbox](#about-the-pk-toolbox)
  * [Background](#background)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
  * [Example](#example)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)

<!-- About the PK Toolbox -->
## About The PK Toolbox

**T**he PK Toolbox is a Python library dedicated to the simulation and visualisation of Pharmokinetic (PK) models. 

Users are able to utilise the PK Toolbox user interface to:

* model the body with peripheral compartments
* utilise either *intravenous bolus* or *subcutaneous* dosing protocols
* specify the dose and duration of dosing
* compare multiple PK model ouputs

### Background

PK models are used to describe how a specific chemical (drug) is absorbed, distributed and excreted in the body. Modelling ensures that a drug achieves the required efficacy while minimising adverse events by sustaining a concentration within a defined therapeutic window. 

Multi-compartmental PK models, in which the body is divided into one or more interacting compartments, are the most commonly used. Below we present the structure of the two PK models available in the PK Toolbox: 

<p align="center">
    <img src="images/IVB.png" alt="Logo" width="350" height="300"> 
    <img src="images/SC.png" alt="Logo" width="350" height="300"> 
 </a>
<p

**Parameter List**

For *intravenous bolus* dosing protocol:
* Dose(t) - Dose function (ng hr<sup>-1</sup>) 
* V<sub>c</sub> - Volume of central compartment (mL)
* q<sub>c</sub> - Concentration of drug in central compartment (ng)
* V<sub>pn</sub> - Volume of peripheral compartment 1 (mL)
* q<sub>n</sub> - Concentration of drug in peripheral compartment 1 (ng)
* Q<sub>pn</sub> - Transition between central compartment and peripheral compartment 1 (mL hr<sup>-1</sup>)
* CL - Clearance rate from the central compartment (mL hr<sup>-1</sup>) 

Additional paramers for *subcutaneous* dosing protocol:
* q<sub>0</sub> - Concentration of drug in dosage compartment (ng)
* k<sub>a</sub> - Absorption rate to central compartment (hr<sup>-1</sup>)

<!-- Getting Started -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

List prerequiste software.
* software name
```sh
installation code
```

### Installation

1. Instruction
2. Instruction with code snippet
```sh
installation code
```
3. Instruction


<!-- Usage -->
## Usage

The PK Toolbox is structured as follows:

<p align="center">
    <img src="images/PK_Toolbox_Scheme.png" width="400" height="200"> 
 </a>
<p

* Users run the run_PK.py file.
    * A PK Toolbox Console window is opened, allowing users to specify one or more PK models for configuration.

* The run_PK.py file calls modules:
    1. model.py : Creates model class objects for each of the user defined PK models.
    2. solve_model.py : Solves models defined by model.py using scipy.integrate.solv_imp.
    3. plotting.py : Creates plot comparing model solutions from solve_model.py. 
    
For further details on each of the modules included in the PK Toolbox view our [docs](https://pk-toolbox.readthedocs.io).

## Example

Provide complete use case example.
<!-- _For more examples, please refer to the [Documentation](URL)_ -->


<!-- License -->
## License

Distributed under the MIT License. Add link to license file when complete.



<!-- Contact -->
## Contact
PK_T
Update collaborators. 
<!-- Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com -->

Project Link: [https://github.com/oj-tooth/PK-Toolbox](https://github.com/oj-tooth/PK-Toolbox)



<!-- Acknowledgements -->
## Acknowledgements

Include bullet point list.
Adapted from available template: 
https://github.com/othneildrew/Best-README-Template/blob/master/README.md
