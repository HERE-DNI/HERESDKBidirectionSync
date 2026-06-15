---
title: "EmpiricalConsumptionModel class"
slug: "sdk-for-flutter-navigate-routing-empiricalconsumptionmodel-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- EmpiricalConsumptionModel-class.html -->


<div>
<h1>EmpiricalConsumptionModel class</h1></div>

<p>This model defines a data-driven energy consumption model for electric vehicles.</p>
<p>It estimates the electrical energy required to traverse a route by combining empirically derived vehicle
parameters with route characteristics such as distance, elevation changes, and driving speed. Rather than
relying on a full physical simulation, this model uses observed consumption behavior to produce realistic
and efficient energy estimates suitable for routing, range prediction, and navigation use cases.</p>
<p>Parameters specific to the electric vehicle are used to calculate energy consumption on a given route.
At minimum, you must provide <a href="sdk-for-flutter-navigate-routing-empiricalconsumptionmodel-ascentconsumptioninwatthourspermeter">EmpiricalConsumptionModel.ascentConsumptionInWattHoursPerMeter</a>,
<a href="sdk-for-flutter-navigate-routing-empiricalconsumptionmodel-descentrecoveryinwatthourspermeter">EmpiricalConsumptionModel.descentRecoveryInWattHoursPerMeter</a> and a
<a href="sdk-for-flutter-navigate-routing-empiricalconsumptionmodel-freeflowspeedtable">EmpiricalConsumptionModel.freeFlowSpeedTable</a>.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>


<h2>Constructors</h2>
<ul><li><a href="sdk-for-flutter-navigate-routing-empiricalconsumptionmodel-empiricalconsumptionmodel">EmpiricalConsumptionModel</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="sdk-for-flutter-navigate-routing-empiricalconsumptionmodel-ascentconsumptioninwatthourspermeter">ascentConsumptionInWattHoursPerMeter</a></li><li><a href="sdk-for-flutter-navigate-routing-empiricalconsumptionmodel-auxiliaryconsumptioninwatthourspersecond">auxiliaryConsumptionInWattHoursPerSecond</a></li><li><a href="sdk-for-flutter-navigate-routing-empiricalconsumptionmodel-descentrecoveryinwatthourspermeter">descentRecoveryInWattHoursPerMeter</a></li><li><a href="sdk-for-flutter-navigate-routing-empiricalconsumptionmodel-freeflowspeedtable">freeFlowSpeedTable</a></li><li><a href="sdk-for-flutter-navigate-routing-empiricalconsumptionmodel-hashcode">hashCode</a></li><li><a href="sdk-for-flutter-navigate-routing-empiricalconsumptionmodel-runtimetype">runtimeType</a></li><li><a href="sdk-for-flutter-navigate-routing-empiricalconsumptionmodel-trafficspeedtable">trafficSpeedTable</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="sdk-for-flutter-navigate-routing-empiricalconsumptionmodel-nosuchmethod">noSuchMethod</a></li><li><a href="sdk-for-flutter-navigate-routing-empiricalconsumptionmodel-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="sdk-for-flutter-navigate-routing-empiricalconsumptionmodel-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>
