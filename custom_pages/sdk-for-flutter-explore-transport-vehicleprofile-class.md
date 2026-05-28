---
title: "VehicleProfile class"
slug: "sdk-for-flutter-explore-transport-vehicleprofile-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- VehicleProfile-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="transport/VehicleProfile-class.html#constructors">Constructors</a></li>
<li><a href="transport/VehicleProfile/VehicleProfile.html">VehicleProfile</a></li>
<li class="section-title">
<a href="transport/VehicleProfile-class.html#instance-properties">Properties</a>
</li>
<li><a href="transport/VehicleProfile/axleCount.html">axleCount</a></li>
<li><a href="transport/VehicleProfile/grossWeightInKilograms.html">grossWeightInKilograms</a></li>
<li><a href="transport/VehicleProfile/hashCode.html">hashCode</a></li>
<li><a href="transport/VehicleProfile/hazardousMaterials.html">hazardousMaterials</a></li>
<li><a href="transport/VehicleProfile/heightInCentimeters.html">heightInCentimeters</a></li>
<li><a href="transport/VehicleProfile/lengthInCentimeters.html">lengthInCentimeters</a></li>
<li class="inherited"><a href="transport/VehicleProfile/runtimeType.html">runtimeType</a></li>
<li><a href="transport/VehicleProfile/trailerCount.html">trailerCount</a></li>
<li><a href="transport/VehicleProfile/truckCategory.html">truckCategory</a></li>
<li><a href="transport/VehicleProfile/tunnelCategory.html">tunnelCategory</a></li>
<li><a href="transport/VehicleProfile/vehicleType.html">vehicleType</a></li>
<li><a href="transport/VehicleProfile/weightPerAxleInKilograms.html">weightPerAxleInKilograms</a></li>
<li><a href="transport/VehicleProfile/widthInCentimeters.html">widthInCentimeters</a></li>
<li class="section-title inherited"><a href="transport/VehicleProfile-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="transport/VehicleProfile/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="transport/VehicleProfile/toString.html">toString</a></li>
<li class="section-title"><a href="transport/VehicleProfile-class.html#operators">Operators</a></li>
<li><a href="transport/VehicleProfile/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-transport-transport-library</li>
<li class="self-crumb">VehicleProfile class</li>
</ol>
<div class="self-name">VehicleProfile</div>
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
<div class="main-content" data-above-sidebar="transport/transport-library-sidebar.html" data-below-sidebar="transport/VehicleProfile-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>VehicleProfile class</h1></div>
<section class="desc markdown">
<p>A vehicle profile describes the vehicle being used with the HSDK.</p>
<p>The profile is planned to be used as single source of information describing the vehicle.</p>
<p>Current modules that use this profile:</p>
<ul>
<li>Navigation: Tracking mode for truck related vehicle restrictions.</li>
</ul>
<p><strong>Note:</strong> This is a beta release of this vehicle profile, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases or even become unsupported, without a
deprecation process.</p>
</section>
<section>
<dl class="dl-horizontal">
<dt>Annotations</dt>
<dd>
<ul class="annotation-list clazz-relationships">
<li>@Deprecated("Will be removed in v4.28.0. Use `sdk.transport.TransportSpecification` instead.")</li>
</ul>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="VehicleProfile">
/sdk-for-flutter-explore-transport-vehicleprofile-vehicleprofile(/sdk-for-flutter-explore-transport-vehicletype vehicleType)
</dt>
<dd>
          Creates a new instance.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="axleCount">
/sdk-for-flutter-explore-transport-vehicleprofile-axlecount
↔ int?
</dt>
<dd>
  Defines total number of axles in the vehicle. The provided value must be greater than or
equal to 2. When not set, possible axle count restrictions will not be taken into
consideration for route calculation. By default, it is not set.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="grossWeightInKilograms">
/sdk-for-flutter-explore-transport-vehicleprofile-grossweightinkilograms
↔ int?
</dt>
<dd>
  Vehicle weight including trailers and shipped goods in kilograms.
By default, it is not set.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-explore-transport-vehicleprofile-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="hazardousMaterials">
/sdk-for-flutter-explore-transport-vehicleprofile-hazardousmaterials
↔ List&lt;<wbr/>/sdk-for-flutter-explore-transport-hazardousmaterial&gt;
</dt>
<dd>
  Specifies a list of hazardous materials shipped in the vehicle.
Refer to /sdk-for-flutter-explore-transport-hazardousmaterial for the available options.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="heightInCentimeters">
/sdk-for-flutter-explore-transport-vehicleprofile-heightincentimeters
↔ int?
</dt>
<dd>
  Vehicle height in centimeters. The provided value must be in the range [0, 5000].
By default, it is not set.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="lengthInCentimeters">
/sdk-for-flutter-explore-transport-vehicleprofile-lengthincentimeters
↔ int?
</dt>
<dd>
  Vehicle length in centimeters. The provided value must be in the range [0, 30000].
By default, it is not set.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-transport-vehicleprofile-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="trailerCount">
/sdk-for-flutter-explore-transport-vehicleprofile-trailercount
↔ int
</dt>
<dd>
  Defines number of trailers attached to the vehicle. The provided value must be in the range
[0, 255]. When not set, possible trailer count restrictions will not be taken into consideration
for route calculation. By default, it is 0.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="truckCategory">
/sdk-for-flutter-explore-transport-vehicleprofile-truckcategory
↔ /sdk-for-flutter-explore-transport-truckcategory?
</dt>
<dd>
  Defines the truck category.
Only used when the /sdk-for-flutter-explore-transport-vehicleprofile-vehicletype is /sdk-for-flutter-explore-transport-vehicletype
By default, it is not set.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="tunnelCategory">
/sdk-for-flutter-explore-transport-vehicleprofile-tunnelcategory
↔ /sdk-for-flutter-explore-transport-tunnelcategory?
</dt>
<dd>
  Specifies the tunnel categories to restrict certain route links.
The route will pass only through tunnels of a less strict category.
Refer to /sdk-for-flutter-explore-transport-tunnelcategory for the available options.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="vehicleType">
/sdk-for-flutter-explore-transport-vehicleprofile-vehicletype
↔ /sdk-for-flutter-explore-transport-vehicletype
</dt>
<dd>
  Defines the vehicle type.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="weightPerAxleInKilograms">
/sdk-for-flutter-explore-transport-vehicleprofile-weightperaxleinkilograms
↔ int?
</dt>
<dd>
  Vehicle weight per axle in kilograms. The provided value must be greater or equal to 0.
When not set, possible weight per axle restrictions will not be taken into
consideration for route calculation. By default, it is not set.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="widthInCentimeters">
/sdk-for-flutter-explore-transport-vehicleprofile-widthincentimeters
↔ int?
</dt>
<dd>
  Vehicle width in centimeters. The provided value must be in the range [0, 5000].
By default, it is not set.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-explore-transport-vehicleprofile-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-transport-vehicleprofile-tostring(<wbr/>)
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
/sdk-for-flutter-explore-transport-vehicleprofile-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-explore-transport-transport-library</li>
<li class="self-crumb">VehicleProfile class</li>
</ol>
<h5>transport library</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>
</div></div>
</div>
`
}</HTMLBlock>
