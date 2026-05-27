---
title: "Constructors"
slug: "sdk-for-flutter-explore-transport-vehiclespecification-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- VehicleSpecification-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="transport/VehicleSpecification-class.html#constructors">Constructors</a></li>
<li><a href="transport/VehicleSpecification/VehicleSpecification.html">VehicleSpecification</a></li>
<li class="section-title">
<a href="transport/VehicleSpecification-class.html#instance-properties">Properties</a>
</li>
<li><a href="transport/VehicleSpecification/axleCount.html">axleCount</a></li>
<li><a href="transport/VehicleSpecification/currentWeightInKilograms.html">currentWeightInKilograms</a></li>
<li><a href="transport/VehicleSpecification/emptyWeightInKilograms.html">emptyWeightInKilograms</a></li>
<li><a href="transport/VehicleSpecification/engineSizeInCubicCentimeters.html">engineSizeInCubicCentimeters</a></li>
<li><a href="transport/VehicleSpecification/grossWeightInKilograms.html">grossWeightInKilograms</a></li>
<li><a href="transport/VehicleSpecification/hashCode.html">hashCode</a></li>
<li><a href="transport/VehicleSpecification/hazardousMaterials.html">hazardousMaterials</a></li>
<li><a href="transport/VehicleSpecification/heightInCentimeters.html">heightInCentimeters</a></li>
<li><a href="transport/VehicleSpecification/isCommercial.html">isCommercial</a></li>
<li><a href="transport/VehicleSpecification/isTruckLight.html">isTruckLight</a></li>
<li><a href="transport/VehicleSpecification/kingpinToRearAxleDistanceInCentimeters.html">kingpinToRearAxleDistanceInCentimeters</a></li>
<li><a href="transport/VehicleSpecification/lastCharacterOfLicensePlate.html">lastCharacterOfLicensePlate</a></li>
<li><a href="transport/VehicleSpecification/lengthInCentimeters.html">lengthInCentimeters</a></li>
<li><a href="transport/VehicleSpecification/occupancy.html">occupancy</a></li>
<li><a href="transport/VehicleSpecification/payloadCapacityInKilograms.html">payloadCapacityInKilograms</a></li>
<li class="inherited"><a href="transport/VehicleSpecification/runtimeType.html">runtimeType</a></li>
<li><a href="transport/VehicleSpecification/tiresCount.html">tiresCount</a></li>
<li><a href="transport/VehicleSpecification/trailerAxleCount.html">trailerAxleCount</a></li>
<li><a href="transport/VehicleSpecification/trailerCount.html">trailerCount</a></li>
<li><a href="transport/VehicleSpecification/truckCategory.html">truckCategory</a></li>
<li><a class="deprecated" href="transport/VehicleSpecification/truckType.html">truckType</a></li>
<li><a href="transport/VehicleSpecification/tunnelCategory.html">tunnelCategory</a></li>
<li><a href="transport/VehicleSpecification/weightPerAxleGroup.html">weightPerAxleGroup</a></li>
<li><a href="transport/VehicleSpecification/weightPerAxleInKilograms.html">weightPerAxleInKilograms</a></li>
<li><a href="transport/VehicleSpecification/widthInCentimeters.html">widthInCentimeters</a></li>
<li class="section-title inherited"><a href="transport/VehicleSpecification-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="transport/VehicleSpecification/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="transport/VehicleSpecification/toString.html">toString</a></li>
<li class="section-title"><a href="transport/VehicleSpecification-class.html#operators">Operators</a></li>
<li><a href="transport/VehicleSpecification/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../transport/transport-library.html">/sdk-for-flutter-explore-transport-transport-library</a></li>
<li class="self-crumb">VehicleSpecification class</li>
</ol>
<div class="self-name">VehicleSpecification</div>
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
<div class="main-content" data-above-sidebar="transport/transport-library-sidebar.html" data-below-sidebar="transport/VehicleSpecification-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>VehicleSpecification class</h1></div>
<section class="desc markdown">
<p>Contains vehicle related attributes.</p>
<p>Examples: Dimensions, weight, axle count.
Only the fields that are set are considered for restriction handling.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="VehicleSpecification">
<a href="../transport/VehicleSpecification/VehicleSpecification.html">/sdk-for-flutter-explore-transport-vehiclespecification-vehiclespecification</a>()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="axleCount">
<a href="../transport/VehicleSpecification/axleCount.html">/sdk-for-flutter-explore-transport-vehiclespecification-axlecount</a>
↔ int?
</dt>
<dd>
  Defines total number of axles in the vehicle. The provided value must be greater than or equal to 2.
By default, it is not set.
Route calculation: When not set, possible axle count restrictions will not be taken into consideration.
Rendering: When set, truck restriction icons for an axle count greater than <a href="../transport/VehicleSpecification/axleCount.html">/sdk-for-flutter-explore-transport-vehiclespecification-axlecount</a> will not be displayed.
When specifying <a href="../transport/VehicleSpecification/trailerAxleCount.html">/sdk-for-flutter-explore-transport-vehiclespecification-traileraxlecount</a>, then <a href="../transport/VehicleSpecification/axleCount.html">/sdk-for-flutter-explore-transport-vehiclespecification-axlecount</a> is required and must be greater than <a href="../transport/VehicleSpecification/trailerAxleCount.html">/sdk-for-flutter-explore-transport-vehiclespecification-traileraxlecount</a>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="currentWeightInKilograms">
<a href="../transport/VehicleSpecification/currentWeightInKilograms.html">/sdk-for-flutter-explore-transport-vehiclespecification-currentweightinkilograms</a>
↔ int?
</dt>
<dd>
  Current truck weight, including trailers and shipped goods currently loaded, specified in
kilograms. The provided value must be greater than or equal to 0. If unspecified,
it will default to <a href="../transport/VehicleSpecification/grossWeightInKilograms.html">/sdk-for-flutter-explore-transport-vehiclespecification-grossweightinkilograms</a>.
By default, it is not set.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="emptyWeightInKilograms">
<a href="../transport/VehicleSpecification/emptyWeightInKilograms.html">/sdk-for-flutter-explore-transport-vehiclespecification-emptyweightinkilograms</a>
↔ int?
</dt>
<dd>
  Empty weight of the vehicle without any load, excluding trailers, specified in kilograms.
The provided value must be greater than or equal to 0.
By default, it is not set.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="engineSizeInCubicCentimeters">
<a href="../transport/VehicleSpecification/engineSizeInCubicCentimeters.html">/sdk-for-flutter-explore-transport-vehiclespecification-enginesizeincubiccentimeters</a>
↔ int?
</dt>
<dd>
  Engine size of the scooter in cubic centimeters. Shouldn't be less than 1 or greater than 65535.
Default value is <code>null</code>, which means the scooter route calculation ignores all engine size limits on the
road.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="grossWeightInKilograms">
<a href="../transport/VehicleSpecification/grossWeightInKilograms.html">/sdk-for-flutter-explore-transport-vehiclespecification-grossweightinkilograms</a>
↔ int?
</dt>
<dd>
  Gross truck weight, including trailers and shipped goods when loaded at capacity, specified in
kilograms. The provided value must be greater than or equal to 0. If unspecified,
it will default to <a href="../transport/VehicleSpecification/currentWeightInKilograms.html">/sdk-for-flutter-explore-transport-vehiclespecification-currentweightinkilograms</a>.
By default, it is not set.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
<a href="../transport/VehicleSpecification/hashCode.html">/sdk-for-flutter-explore-transport-vehiclespecification-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="hazardousMaterials">
<a href="../transport/VehicleSpecification/hazardousMaterials.html">/sdk-for-flutter-explore-transport-vehiclespecification-hazardousmaterials</a>
↔ List&lt;<wbr/><a href="../transport/HazardousMaterial.html">/sdk-for-flutter-explore-transport-hazardousmaterial</a>&gt;
</dt>
<dd>
  Specifies a list of hazardous materials shipped in the vehicle.
Refer to <a href="../transport/HazardousMaterial.html">/sdk-for-flutter-explore-transport-hazardousmaterial</a> for the available options.
By default, it is an empty list.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="heightInCentimeters">
<a href="../transport/VehicleSpecification/heightInCentimeters.html">/sdk-for-flutter-explore-transport-vehiclespecification-heightincentimeters</a>
↔ int?
</dt>
<dd>
  Vehicle height in centimeters. The provided value must be in the range [0, 5000].
By default, it is not set.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isCommercial">
<a href="../transport/VehicleSpecification/isCommercial.html">/sdk-for-flutter-explore-transport-vehiclespecification-iscommercial</a>
↔ bool
</dt>
<dd>
  Specifies whether the vehicle is a commercial or a non-commercial vehicle.
Defaults to <code>false</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isTruckLight">
<a href="../transport/VehicleSpecification/isTruckLight.html">/sdk-for-flutter-explore-transport-vehiclespecification-istrucklight</a>
↔ bool
</dt>
<dd>
  A flag indicating whether the truck is light enough to be classified more as a car than a truck in Japan.
The flag should not be set to <code>true</code> in other countries than Japan.
Defaults to <code>false</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="kingpinToRearAxleDistanceInCentimeters">
<a href="../transport/VehicleSpecification/kingpinToRearAxleDistanceInCentimeters.html">/sdk-for-flutter-explore-transport-vehiclespecification-kingpintorearaxledistanceincentimeters</a>
↔ int?
</dt>
<dd>
  Defines the kingpin to rear axle distance, in centimeters.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="lastCharacterOfLicensePlate">
<a href="../transport/VehicleSpecification/lastCharacterOfLicensePlate.html">/sdk-for-flutter-explore-transport-vehiclespecification-lastcharacteroflicenseplate</a>
↔ String?
</dt>
<dd>
  Last character of license plate in String format. This value can be used to
evaluate restrictions in environmental zones.
By default, it is not set.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="lengthInCentimeters">
<a href="../transport/VehicleSpecification/lengthInCentimeters.html">/sdk-for-flutter-explore-transport-vehiclespecification-lengthincentimeters</a>
↔ int?
</dt>
<dd>
  Vehicle length in centimeters. The provided value must be in the range [0, 30000].
By default, it is not set.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="occupancy">
<a href="../transport/VehicleSpecification/occupancy.html">/sdk-for-flutter-explore-transport-vehiclespecification-occupancy</a>
↔ int?
</dt>
<dd>
  Specifies the number of occupants in the vehicle, including driver,
can affect the vehicle's ability to use HOV/carpool restricted lanes.
Should not be less than 1 or greater than 255.
By default, it is not set.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="payloadCapacityInKilograms">
<a href="../transport/VehicleSpecification/payloadCapacityInKilograms.html">/sdk-for-flutter-explore-transport-vehiclespecification-payloadcapacityinkilograms</a>
↔ int?
</dt>
<dd>
  Allowed payload capacity, including trailers, specified in kilograms. The provided value
must be greater then or equal to 0.
By default, it is not set.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../transport/VehicleSpecification/runtimeType.html">/sdk-for-flutter-explore-transport-vehiclespecification-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="tiresCount">
<a href="../transport/VehicleSpecification/tiresCount.html">/sdk-for-flutter-explore-transport-vehiclespecification-tirescount</a>
↔ int?
</dt>
<dd>
  The total number of tires the vehicle has, i.e., the tires on the base vehicle and any attached trailers.
By default, it is not set.
Otherwise it is guaranteed to be in the range [1, 255].
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="trailerAxleCount">
<a href="../transport/VehicleSpecification/trailerAxleCount.html">/sdk-for-flutter-explore-transport-vehiclespecification-traileraxlecount</a>
↔ int?
</dt>
<dd>
  Defines total number of axles across all the trailers attached to the vehicle.
This number is included in <a href="../transport/VehicleSpecification/axleCount.html">/sdk-for-flutter-explore-transport-vehiclespecification-axlecount</a>, hence <a href="../transport/VehicleSpecification/trailerAxleCount.html">/sdk-for-flutter-explore-transport-vehiclespecification-traileraxlecount</a> must be less than <a href="../transport/VehicleSpecification/axleCount.html">/sdk-for-flutter-explore-transport-vehiclespecification-axlecount</a>
and greater than or equal to 1. <a href="../transport/VehicleSpecification/axleCount.html">/sdk-for-flutter-explore-transport-vehiclespecification-axlecount</a> and <a href="../transport/VehicleSpecification/trailerCount.html">/sdk-for-flutter-explore-transport-vehiclespecification-trailercount</a> are required to specify <a href="../transport/VehicleSpecification/trailerAxleCount.html">/sdk-for-flutter-explore-transport-vehiclespecification-traileraxlecount</a>.
By default, it is not set.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="trailerCount">
<a href="../transport/VehicleSpecification/trailerCount.html">/sdk-for-flutter-explore-transport-vehiclespecification-trailercount</a>
↔ int?
</dt>
<dd>
  Defines number of trailers attached to the vehicle. The provided value must be in the range [0, 255].
By default, it is not set.
When specifying <a href="../transport/VehicleSpecification/trailerAxleCount.html">/sdk-for-flutter-explore-transport-vehiclespecification-traileraxlecount</a>, then <a href="../transport/VehicleSpecification/trailerCount.html">/sdk-for-flutter-explore-transport-vehiclespecification-trailercount</a> is required and must be greater than 0.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="truckCategory">
<a href="../transport/VehicleSpecification/truckCategory.html">/sdk-for-flutter-explore-transport-vehiclespecification-truckcategory</a>
↔ <a href="../transport/TruckCategory.html">/sdk-for-flutter-explore-transport-truckcategory</a>?
</dt>
<dd>
  Defines the truck category.
By default, it is not set.
Rendering: <a href="../transport/VehicleSpecification/truckCategory.html">/sdk-for-flutter-explore-transport-vehiclespecification-truckcategory</a> is ignored and has no effect.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="truckType">
<a class="deprecated" href="../transport/VehicleSpecification/truckType.html">/sdk-for-flutter-explore-transport-vehiclespecification-trucktype</a>
↔ <a class="deprecated" href="../transport/TruckType.html">/sdk-for-flutter-explore-transport-trucktype</a>
</dt>
<dd>
  Will be replaced with <code>truckCategory</code> when the <code>TruckSpecification</code> will be replaced by <code>VehicleSpecification</code>.
Defines the type of truck.
Defaults to <a href="../transport/TruckType.html">/sdk-for-flutter-explore-transport-trucktype</a>.
Rendering <code>sdk.mapview.TruckProfile</code>: <a class="deprecated" href="../transport/VehicleSpecification/truckType.html">/sdk-for-flutter-explore-transport-vehiclespecification-trucktype</a> is ignored and has no effect.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="tunnelCategory">
<a href="../transport/VehicleSpecification/tunnelCategory.html">/sdk-for-flutter-explore-transport-vehiclespecification-tunnelcategory</a>
↔ <a href="../transport/TunnelCategory.html">/sdk-for-flutter-explore-transport-tunnelcategory</a>?
</dt>
<dd>
  Specifies the tunnel categories to restrict certain route links.
The route will pass only through tunnels of a less strict category.
Refer to <a href="../transport/TunnelCategory.html">/sdk-for-flutter-explore-transport-tunnelcategory</a> for the available options.
By default, it is not set.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="weightPerAxleGroup">
<a href="../transport/VehicleSpecification/weightPerAxleGroup.html">/sdk-for-flutter-explore-transport-vehiclespecification-weightperaxlegroup</a>
↔ <a href="../transport/WeightPerAxleGroup-class.html">/sdk-for-flutter-explore-transport-weightperaxlegroup-class</a>?
</dt>
<dd>
  Allows specification of axle weights in a more fine-grained way than <a href="../transport/VehicleSpecification/weightPerAxleInKilograms.html">/sdk-for-flutter-explore-transport-vehiclespecification-weightperaxleinkilograms</a>.
This is relevant in countries with signs and regulations that specify different limits for different axle
groups, like the USA and Sweden.
By default is not set.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="weightPerAxleInKilograms">
<a href="../transport/VehicleSpecification/weightPerAxleInKilograms.html">/sdk-for-flutter-explore-transport-vehiclespecification-weightperaxleinkilograms</a>
↔ int?
</dt>
<dd>
  Heaviest weight per axle, regardless of axle type or axle group.
It is evaluated against all axle weight restrictions, including single axle and tandem axle weight restrictions.
The provided value must be greater or equal to 0.
By default, it is not set.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="widthInCentimeters">
<a href="../transport/VehicleSpecification/widthInCentimeters.html">/sdk-for-flutter-explore-transport-vehiclespecification-widthincentimeters</a>
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
<a href="../transport/VehicleSpecification/noSuchMethod.html">/sdk-for-flutter-explore-transport-vehiclespecification-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../transport/VehicleSpecification/toString.html">/sdk-for-flutter-explore-transport-vehiclespecification-tostring</a>(<wbr/>)
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
<a href="../transport/VehicleSpecification/operator_equals.html">/sdk-for-flutter-explore-transport-vehiclespecification-operator-equals</a>(<wbr/>Object other)
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
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../transport/transport-library.html">/sdk-for-flutter-explore-transport-transport-library</a></li>
<li class="self-crumb">VehicleSpecification class</li>
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
</HTMLBlock>
