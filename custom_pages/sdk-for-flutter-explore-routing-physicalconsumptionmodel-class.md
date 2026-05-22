---
title: "Untitled"
slug: "sdk-for-flutter-explore-routing-physicalconsumptionmodel-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- PhysicalConsumptionModel-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-routing-routing-library</li>
<li class="self-crumb">PhysicalConsumptionModel class</li>
</ol>
<div class="self-name">PhysicalConsumptionModel</div>
<form class="search navbar-right" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-box" placeholder="Loading search..." type="text"/>
</form>
<div class="toggle" id="theme-button" title="Toggle brightness">
<label for="theme">
<input id="theme" type="checkbox" value="light-theme"/>

        dark_mode
      

        light_mode
      
</label>
</div>
</header>
<main>
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/PhysicalConsumptionModel-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>PhysicalConsumptionModel class</h1></div>
<section class="desc markdown">
<p>Defines the physical consumption model for electric vehicles,
using vehicle-specific parameters to calculate energy consumption along a route.</p>
<p><strong>Note:</strong> /sdk-for-flutter-explore-transport-vehiclespecification-currentweightinkilograms must be set.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="PhysicalConsumptionModel">
/sdk-for-flutter-explore-routing-physicalconsumptionmodel-physicalconsumptionmodel()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="airDragCoefficient">
/sdk-for-flutter-explore-routing-physicalconsumptionmodel-airdragcoefficient
↔ double
</dt>
<dd>
  The drag coefficient of an vehicle defines the way the vehicle is expected to pass through the surrounding air.
More streamlined vehicles are more aerodynamic and therefore have smaller drag coefficient.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="auxiliaryPowerConsumptionInWatts">
/sdk-for-flutter-explore-routing-physicalconsumptionmodel-auxiliarypowerconsumptioninwatts
↔ double
</dt>
<dd>
  Power (in W) consumed by the vehicle's auxiliary systems (for example, air conditioning, lights).
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="driveTrainEfficiency">
/sdk-for-flutter-explore-routing-physicalconsumptionmodel-drivetrainefficiency
↔ double
</dt>
<dd>
  The proportion of the energy drawn from the battery that is used to move the vehicle.
(This is to factor in energy losses through heat in the motors, for example.)
Supported range from 0 to 1
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="frontalAreaInSquareMeters">
/sdk-for-flutter-explore-routing-physicalconsumptionmodel-frontalareainsquaremeters
↔ double
</dt>
<dd>
  Frontal area represents the total cross section area of the vehicle as viewed from the front, specified in square meters.
Physical consumption model is using this value in combination with <code>airDragCoefficient</code> to calculate the consumption caused by air resistance.
As fallback /sdk-for-flutter-explore-transport-vehiclespecification-widthincentimeters and /sdk-for-flutter-explore-transport-vehiclespecification-heightincentimeters are used.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-explore-routing-physicalconsumptionmodel-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="recuperationEfficiency">
/sdk-for-flutter-explore-routing-physicalconsumptionmodel-recuperationefficiency
↔ double
</dt>
<dd>
  The proportion of the energy gained when braking or going downhill that can be recuperated and restored as battery charge.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="rollingResistanceCoefficient">
/sdk-for-flutter-explore-routing-physicalconsumptionmodel-rollingresistancecoefficient
↔ double
</dt>
<dd>
  Rolling resistance refers to the resistance experienced by your vehicle tire as it rolls over a surface.
The main causes of this resistance are tire deformation, wing drag, and friction with the ground.
The coefficient of rolling resistance is a numerical value indicating the severity of this factor.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-routing-physicalconsumptionmodel-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-explore-routing-physicalconsumptionmodel-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-routing-physicalconsumptionmodel-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable" id="operator ==">
/sdk-for-flutter-explore-routing-physicalconsumptionmodel-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd>
  The equality operator.
  

</dd>
</dl>
</section>
</div> 
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">

<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-routing-routing-library</li>
<li class="self-crumb">PhysicalConsumptionModel class</li>
</ol>
<h5>routing library</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>



</div>
`
}</HTMLBlock>
