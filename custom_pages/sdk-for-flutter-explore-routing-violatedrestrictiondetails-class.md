---
title: "Constructors"
slug: "sdk-for-flutter-explore-routing-violatedrestrictiondetails-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- ViolatedRestrictionDetails-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="routing/ViolatedRestrictionDetails-class.html#constructors">Constructors</a></li>
<li><a href="routing/ViolatedRestrictionDetails/ViolatedRestrictionDetails.html">ViolatedRestrictionDetails</a></li>
<li class="section-title">
<a href="routing/ViolatedRestrictionDetails-class.html#instance-properties">Properties</a>
</li>
<li><a href="routing/ViolatedRestrictionDetails/forbiddenAxleCount.html">forbiddenAxleCount</a></li>
<li><a href="routing/ViolatedRestrictionDetails/forbiddenHazardousGoods.html">forbiddenHazardousGoods</a></li>
<li><a href="routing/ViolatedRestrictionDetails/forbiddenTrailerCount.html">forbiddenTrailerCount</a></li>
<li><a href="routing/ViolatedRestrictionDetails/forbiddenTruckCategory.html">forbiddenTruckCategory</a></li>
<li><a href="routing/ViolatedRestrictionDetails/forbiddenTruckRoadTypes.html">forbiddenTruckRoadTypes</a></li>
<li><a class="deprecated" href="routing/ViolatedRestrictionDetails/forbiddenTruckType.html">forbiddenTruckType</a></li>
<li><a href="routing/ViolatedRestrictionDetails/hashCode.html">hashCode</a></li>
<li><a href="routing/ViolatedRestrictionDetails/maxHeightInCentimeters.html">maxHeightInCentimeters</a></li>
<li><a href="routing/ViolatedRestrictionDetails/maxKingpinToRearAxleDistanceInCentimeters.html">maxKingpinToRearAxleDistanceInCentimeters</a></li>
<li><a href="routing/ViolatedRestrictionDetails/maxLengthInCentimeters.html">maxLengthInCentimeters</a></li>
<li><a href="routing/ViolatedRestrictionDetails/maxNumberOfTires.html">maxNumberOfTires</a></li>
<li><a href="routing/ViolatedRestrictionDetails/maxPayloadCapacityInKilograms.html">maxPayloadCapacityInKilograms</a></li>
<li><a href="routing/ViolatedRestrictionDetails/maxTunnelCategory.html">maxTunnelCategory</a></li>
<li><a href="routing/ViolatedRestrictionDetails/maxWeight.html">maxWeight</a></li>
<li><a href="routing/ViolatedRestrictionDetails/maxWeightPerAxleGroupInKilograms.html">maxWeightPerAxleGroupInKilograms</a></li>
<li><a href="routing/ViolatedRestrictionDetails/maxWeightPerAxleInKilograms.html">maxWeightPerAxleInKilograms</a></li>
<li><a href="routing/ViolatedRestrictionDetails/maxWidthInCentimeters.html">maxWidthInCentimeters</a></li>
<li><a href="routing/ViolatedRestrictionDetails/routingZoneReference.html">routingZoneReference</a></li>
<li class="inherited"><a href="routing/ViolatedRestrictionDetails/runtimeType.html">runtimeType</a></li>
<li><a href="routing/ViolatedRestrictionDetails/timeRule.html">timeRule</a></li>
<li class="section-title inherited"><a href="routing/ViolatedRestrictionDetails-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="routing/ViolatedRestrictionDetails/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="routing/ViolatedRestrictionDetails/toString.html">toString</a></li>
<li class="section-title"><a href="routing/ViolatedRestrictionDetails-class.html#operators">Operators</a></li>
<li><a href="routing/ViolatedRestrictionDetails/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li class="self-crumb">ViolatedRestrictionDetails class</li>
</ol>
<div class="self-name">ViolatedRestrictionDetails</div>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/ViolatedRestrictionDetails-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>ViolatedRestrictionDetails class</h1></div>
<section class="desc markdown">
<p>Optional restriction details, contains additional information depending on the specific violation, zero or more member might be set.</p>
<p>For example, if the vehicle violates the maximum allowed height during the trip, then the member <code>max_height_in_centimeters</code> will
be set with the maximum allowed height value.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="ViolatedRestrictionDetails">
<a href="../routing/ViolatedRestrictionDetails/ViolatedRestrictionDetails.html">/sdk-for-flutter-explore-routing-violatedrestrictiondetails-violatedrestrictiondetails</a>()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="forbiddenAxleCount">
<a href="../routing/ViolatedRestrictionDetails/forbiddenAxleCount.html">/sdk-for-flutter-explore-routing-violatedrestrictiondetails-forbiddenaxlecount</a>
↔ <a href="../core/IntegerRange-class.html">/sdk-for-flutter-explore-core-integerrange-class</a>?
</dt>
<dd>
  The restriction to trucks with axles number within specified range during the trip.
This property will be set if the <a href="../transport/VehicleSpecification/axleCount.html">/sdk-for-flutter-explore-transport-vehiclespecification-axlecount</a>
is within this range.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="forbiddenHazardousGoods">
<a href="../routing/ViolatedRestrictionDetails/forbiddenHazardousGoods.html">/sdk-for-flutter-explore-routing-violatedrestrictiondetails-forbiddenhazardousgoods</a>
↔ List&lt;<wbr/><a href="../transport/HazardousMaterial.html">/sdk-for-flutter-explore-transport-hazardousmaterial</a>&gt;
</dt>
<dd>
  There are two lists for our trip: Hazardous goods restrictions applied during the trip, and the list used
for the route calculation provided using <a href="../transport/VehicleSpecification/hazardousMaterials.html">/sdk-for-flutter-explore-transport-vehiclespecification-hazardousmaterials</a> from
<a href="../transport/TransportSpecification/vehicleSpecification.html">/sdk-for-flutter-explore-transport-transportspecification-vehiclespecification</a> from <a href="../routing/RoutingOptions/transportSpecification.html">/sdk-for-flutter-explore-routing-routingoptions-transportspecification</a>.
This property is the intersection of the two lists.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="forbiddenTrailerCount">
<a href="../routing/ViolatedRestrictionDetails/forbiddenTrailerCount.html">/sdk-for-flutter-explore-routing-violatedrestrictiondetails-forbiddentrailercount</a>
↔ <a href="../core/IntegerRange-class.html">/sdk-for-flutter-explore-core-integerrange-class</a>?
</dt>
<dd>
  Constrains the restriction to trucks with number of trailer within specified range during the trip.
This property will be set if the <a href="../transport/VehicleSpecification/trailerCount.html">/sdk-for-flutter-explore-transport-vehiclespecification-trailercount</a>
is within this range.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="forbiddenTruckCategory">
<a href="../routing/ViolatedRestrictionDetails/forbiddenTruckCategory.html">/sdk-for-flutter-explore-routing-violatedrestrictiondetails-forbiddentruckcategory</a>
↔ <a href="../transport/TruckCategory.html">/sdk-for-flutter-explore-transport-truckcategory</a>?
</dt>
<dd>
  This property will be set if a restriction applies to the value of <a href="../transport/TruckCategory.html">/sdk-for-flutter-explore-transport-truckcategory</a>
parameter used for route calculation.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="forbiddenTruckRoadTypes">
<a href="../routing/ViolatedRestrictionDetails/forbiddenTruckRoadTypes.html">/sdk-for-flutter-explore-routing-violatedrestrictiondetails-forbiddentruckroadtypes</a>
↔ List&lt;<wbr/><a href="../transport/TruckRoadType.html">/sdk-for-flutter-explore-transport-truckroadtype</a>&gt;
</dt>
<dd>
  Contains violated restrictions for truck road types.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="forbiddenTruckType">
<a class="deprecated" href="../routing/ViolatedRestrictionDetails/forbiddenTruckType.html">/sdk-for-flutter-explore-routing-violatedrestrictiondetails-forbiddentrucktype</a>
↔ <a class="deprecated" href="../transport/TruckType.html">/sdk-for-flutter-explore-transport-trucktype</a>?
</dt>
<dd>
  This property will be set if a restriction applies to the value of <a class="deprecated" href="../transport/TruckType.html">/sdk-for-flutter-explore-transport-trucktype</a>
parameter used for route calculation.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
<a href="../routing/ViolatedRestrictionDetails/hashCode.html">/sdk-for-flutter-explore-routing-violatedrestrictiondetails-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="maxHeightInCentimeters">
<a href="../routing/ViolatedRestrictionDetails/maxHeightInCentimeters.html">/sdk-for-flutter-explore-routing-violatedrestrictiondetails-maxheightincentimeters</a>
↔ int?
</dt>
<dd>
  Max permitted height during the trip, in centimeters.
This property will be set if the <a href="../transport/VehicleSpecification/heightInCentimeters.html">/sdk-for-flutter-explore-transport-vehiclespecification-heightincentimeters</a>
exceeds this value.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maxKingpinToRearAxleDistanceInCentimeters">
<a href="../routing/ViolatedRestrictionDetails/maxKingpinToRearAxleDistanceInCentimeters.html">/sdk-for-flutter-explore-routing-violatedrestrictiondetails-maxkingpintorearaxledistanceincentimeters</a>
↔ int?
</dt>
<dd>
  Contains the maximum permitted distance from kingpin to the rear axle in centimeters.
This property will be set if the
<a href="../transport/VehicleSpecification/kingpinToRearAxleDistanceInCentimeters.html">/sdk-for-flutter-explore-transport-vehiclespecification-kingpintorearaxledistanceincentimeters</a>
exceeds the specified value.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maxLengthInCentimeters">
<a href="../routing/ViolatedRestrictionDetails/maxLengthInCentimeters.html">/sdk-for-flutter-explore-routing-violatedrestrictiondetails-maxlengthincentimeters</a>
↔ int?
</dt>
<dd>
  Max permitted length during the trip, in centimeters.
This property will be set if the <a href="../transport/VehicleSpecification/lengthInCentimeters.html">/sdk-for-flutter-explore-transport-vehiclespecification-lengthincentimeters</a>
exceeds this value.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maxNumberOfTires">
<a href="../routing/ViolatedRestrictionDetails/maxNumberOfTires.html">/sdk-for-flutter-explore-routing-violatedrestrictiondetails-maxnumberoftires</a>
↔ int?
</dt>
<dd>
  Contains the maximum permitted number of tires.
This property will be set if the <a href="../transport/VehicleSpecification/tiresCount.html">/sdk-for-flutter-explore-transport-vehiclespecification-tirescount</a> exceeds the specified value.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maxPayloadCapacityInKilograms">
<a href="../routing/ViolatedRestrictionDetails/maxPayloadCapacityInKilograms.html">/sdk-for-flutter-explore-routing-violatedrestrictiondetails-maxpayloadcapacityinkilograms</a>
↔ int?
</dt>
<dd>
  Max permitted payload capacity during the trip, in kilograms.
This property will be set if the <a href="../transport/VehicleSpecification/payloadCapacityInKilograms.html">/sdk-for-flutter-explore-transport-vehiclespecification-payloadcapacityinkilograms</a>
exceeds this value.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maxTunnelCategory">
<a href="../routing/ViolatedRestrictionDetails/maxTunnelCategory.html">/sdk-for-flutter-explore-routing-violatedrestrictiondetails-maxtunnelcategory</a>
↔ <a href="../transport/TunnelCategory.html">/sdk-for-flutter-explore-transport-tunnelcategory</a>?
</dt>
<dd>
  Tunnel category to restrict transport of specific goods during the trip.
This property will be set if the <a href="../transport/VehicleSpecification/tunnelCategory.html">/sdk-for-flutter-explore-transport-vehiclespecification-tunnelcategory</a> from
<a href="../transport/TransportSpecification/vehicleSpecification.html">/sdk-for-flutter-explore-transport-transportspecification-vehiclespecification</a> from <a href="../routing/RoutingOptions/transportSpecification.html">/sdk-for-flutter-explore-routing-routingoptions-transportspecification</a>
exceeds this value.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maxWeight">
<a href="../routing/ViolatedRestrictionDetails/maxWeight.html">/sdk-for-flutter-explore-routing-violatedrestrictiondetails-maxweight</a>
↔ <a href="../routing/VehicleRestrictionMaxWeight-class.html">/sdk-for-flutter-explore-routing-vehiclerestrictionmaxweight-class</a>?
</dt>
<dd>
  Max permitted weight during the trip, in kilograms, along with the specific type of maximum permitted weight restriction.
This property will be set if the <a href="../transport/VehicleSpecification/grossWeightInKilograms.html">/sdk-for-flutter-explore-transport-vehiclespecification-grossweightinkilograms</a>
parameter used for route calculation exceeds this value.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maxWeightPerAxleGroupInKilograms">
<a href="../routing/ViolatedRestrictionDetails/maxWeightPerAxleGroupInKilograms.html">/sdk-for-flutter-explore-routing-violatedrestrictiondetails-maxweightperaxlegroupinkilograms</a>
↔ <a href="../routing/MaxAxleGroupWeight-class.html">/sdk-for-flutter-explore-routing-maxaxlegroupweight-class</a>?
</dt>
<dd>
  Max permitted weight per axle group during the trip, in kilograms.
This property will be set if the <a href="../transport/VehicleSpecification/weightPerAxleGroup.html">/sdk-for-flutter-explore-transport-vehiclespecification-weightperaxlegroup</a>
exceeds this value.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maxWeightPerAxleInKilograms">
<a href="../routing/ViolatedRestrictionDetails/maxWeightPerAxleInKilograms.html">/sdk-for-flutter-explore-routing-violatedrestrictiondetails-maxweightperaxleinkilograms</a>
↔ int?
</dt>
<dd>
  Max permitted weight per axle during the trip, in kilograms.
This property will be set if the <a href="../transport/VehicleSpecification/weightPerAxleInKilograms.html">/sdk-for-flutter-explore-transport-vehiclespecification-weightperaxleinkilograms</a>
exceeds this value.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maxWidthInCentimeters">
<a href="../routing/ViolatedRestrictionDetails/maxWidthInCentimeters.html">/sdk-for-flutter-explore-routing-violatedrestrictiondetails-maxwidthincentimeters</a>
↔ int?
</dt>
<dd>
  Max permitted width during the trip, in centimeters.
This property will be set if the <a href="../transport/VehicleSpecification/widthInCentimeters.html">/sdk-for-flutter-explore-transport-vehiclespecification-widthincentimeters</a>
exceeds this value.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="routingZoneReference">
<a href="../routing/ViolatedRestrictionDetails/routingZoneReference.html">/sdk-for-flutter-explore-routing-violatedrestrictiondetails-routingzonereference</a>
↔ String?
</dt>
<dd>
  Contains the restricted routing zone reference
This property will be set if the <a href="../routing/AvoidanceOptions/zoneCategories.html">/sdk-for-flutter-explore-routing-avoidanceoptions-zonecategories</a> is not empty
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../routing/ViolatedRestrictionDetails/runtimeType.html">/sdk-for-flutter-explore-routing-violatedrestrictiondetails-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="timeRule">
<a href="../routing/ViolatedRestrictionDetails/timeRule.html">/sdk-for-flutter-explore-routing-violatedrestrictiondetails-timerule</a>
↔ <a href="../core/TimeRule-class.html">/sdk-for-flutter-explore-core-timerule-class</a>?
</dt>
<dd>
  Time intervals during which restrictions are enforced.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
<a href="../routing/ViolatedRestrictionDetails/noSuchMethod.html">/sdk-for-flutter-explore-routing-violatedrestrictiondetails-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../routing/ViolatedRestrictionDetails/toString.html">/sdk-for-flutter-explore-routing-violatedrestrictiondetails-tostring</a>(<wbr/>)
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
<a href="../routing/ViolatedRestrictionDetails/operator_equals.html">/sdk-for-flutter-explore-routing-violatedrestrictiondetails-operator-equals</a>(<wbr/>Object other)
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
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li class="self-crumb">ViolatedRestrictionDetails class</li>
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
</div></div>
</div>
</HTMLBlock>
