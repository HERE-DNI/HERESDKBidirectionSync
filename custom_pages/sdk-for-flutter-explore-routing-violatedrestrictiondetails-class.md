---
title: "ViolatedRestrictionDetails class"
slug: "sdk-for-flutter-explore-routing-violatedrestrictiondetails-class"
---

<HTMLBlock>{
`
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
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-routing-routing-library</li>
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
/sdk-for-flutter-explore-routing-violatedrestrictiondetails-violatedrestrictiondetails()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="forbiddenAxleCount">
/sdk-for-flutter-explore-routing-violatedrestrictiondetails-forbiddenaxlecount
↔ /sdk-for-flutter-explore-core-integerrange-class?
</dt>
<dd>
  The restriction to trucks with axles number within specified range during the trip.
This property will be set if the /sdk-for-flutter-explore-transport-vehiclespecification-axlecount
is within this range.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="forbiddenHazardousGoods">
/sdk-for-flutter-explore-routing-violatedrestrictiondetails-forbiddenhazardousgoods
↔ List&lt;<wbr/>/sdk-for-flutter-explore-transport-hazardousmaterial&gt;
</dt>
<dd>
  There are two lists for our trip: Hazardous goods restrictions applied during the trip, and the list used
for the route calculation provided using /sdk-for-flutter-explore-transport-vehiclespecification-hazardousmaterials from
/sdk-for-flutter-explore-transport-transportspecification-vehiclespecification from /sdk-for-flutter-explore-routing-routingoptions-transportspecification.
This property is the intersection of the two lists.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="forbiddenTrailerCount">
/sdk-for-flutter-explore-routing-violatedrestrictiondetails-forbiddentrailercount
↔ /sdk-for-flutter-explore-core-integerrange-class?
</dt>
<dd>
  Constrains the restriction to trucks with number of trailer within specified range during the trip.
This property will be set if the /sdk-for-flutter-explore-transport-vehiclespecification-trailercount
is within this range.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="forbiddenTruckCategory">
/sdk-for-flutter-explore-routing-violatedrestrictiondetails-forbiddentruckcategory
↔ /sdk-for-flutter-explore-transport-truckcategory?
</dt>
<dd>
  This property will be set if a restriction applies to the value of /sdk-for-flutter-explore-transport-truckcategory
parameter used for route calculation.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="forbiddenTruckRoadTypes">
/sdk-for-flutter-explore-routing-violatedrestrictiondetails-forbiddentruckroadtypes
↔ List&lt;<wbr/>/sdk-for-flutter-explore-transport-truckroadtype&gt;
</dt>
<dd>
  Contains violated restrictions for truck road types.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="forbiddenTruckType">
/sdk-for-flutter-explore-routing-violatedrestrictiondetails-forbiddentrucktype
↔ /sdk-for-flutter-explore-transport-trucktype?
</dt>
<dd>
  This property will be set if a restriction applies to the value of /sdk-for-flutter-explore-transport-trucktype
parameter used for route calculation.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-explore-routing-violatedrestrictiondetails-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="maxHeightInCentimeters">
/sdk-for-flutter-explore-routing-violatedrestrictiondetails-maxheightincentimeters
↔ int?
</dt>
<dd>
  Max permitted height during the trip, in centimeters.
This property will be set if the /sdk-for-flutter-explore-transport-vehiclespecification-heightincentimeters
exceeds this value.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maxKingpinToRearAxleDistanceInCentimeters">
/sdk-for-flutter-explore-routing-violatedrestrictiondetails-maxkingpintorearaxledistanceincentimeters
↔ int?
</dt>
<dd>
  Contains the maximum permitted distance from kingpin to the rear axle in centimeters.
This property will be set if the
/sdk-for-flutter-explore-transport-vehiclespecification-kingpintorearaxledistanceincentimeters
exceeds the specified value.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maxLengthInCentimeters">
/sdk-for-flutter-explore-routing-violatedrestrictiondetails-maxlengthincentimeters
↔ int?
</dt>
<dd>
  Max permitted length during the trip, in centimeters.
This property will be set if the /sdk-for-flutter-explore-transport-vehiclespecification-lengthincentimeters
exceeds this value.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maxNumberOfTires">
/sdk-for-flutter-explore-routing-violatedrestrictiondetails-maxnumberoftires
↔ int?
</dt>
<dd>
  Contains the maximum permitted number of tires.
This property will be set if the /sdk-for-flutter-explore-transport-vehiclespecification-tirescount exceeds the specified value.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maxPayloadCapacityInKilograms">
/sdk-for-flutter-explore-routing-violatedrestrictiondetails-maxpayloadcapacityinkilograms
↔ int?
</dt>
<dd>
  Max permitted payload capacity during the trip, in kilograms.
This property will be set if the /sdk-for-flutter-explore-transport-vehiclespecification-payloadcapacityinkilograms
exceeds this value.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maxTunnelCategory">
/sdk-for-flutter-explore-routing-violatedrestrictiondetails-maxtunnelcategory
↔ /sdk-for-flutter-explore-transport-tunnelcategory?
</dt>
<dd>
  Tunnel category to restrict transport of specific goods during the trip.
This property will be set if the /sdk-for-flutter-explore-transport-vehiclespecification-tunnelcategory from
/sdk-for-flutter-explore-transport-transportspecification-vehiclespecification from /sdk-for-flutter-explore-routing-routingoptions-transportspecification
exceeds this value.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maxWeight">
/sdk-for-flutter-explore-routing-violatedrestrictiondetails-maxweight
↔ /sdk-for-flutter-explore-routing-vehiclerestrictionmaxweight-class?
</dt>
<dd>
  Max permitted weight during the trip, in kilograms, along with the specific type of maximum permitted weight restriction.
This property will be set if the /sdk-for-flutter-explore-transport-vehiclespecification-grossweightinkilograms
parameter used for route calculation exceeds this value.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maxWeightPerAxleGroupInKilograms">
/sdk-for-flutter-explore-routing-violatedrestrictiondetails-maxweightperaxlegroupinkilograms
↔ /sdk-for-flutter-explore-routing-maxaxlegroupweight-class?
</dt>
<dd>
  Max permitted weight per axle group during the trip, in kilograms.
This property will be set if the /sdk-for-flutter-explore-transport-vehiclespecification-weightperaxlegroup
exceeds this value.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maxWeightPerAxleInKilograms">
/sdk-for-flutter-explore-routing-violatedrestrictiondetails-maxweightperaxleinkilograms
↔ int?
</dt>
<dd>
  Max permitted weight per axle during the trip, in kilograms.
This property will be set if the /sdk-for-flutter-explore-transport-vehiclespecification-weightperaxleinkilograms
exceeds this value.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maxWidthInCentimeters">
/sdk-for-flutter-explore-routing-violatedrestrictiondetails-maxwidthincentimeters
↔ int?
</dt>
<dd>
  Max permitted width during the trip, in centimeters.
This property will be set if the /sdk-for-flutter-explore-transport-vehiclespecification-widthincentimeters
exceeds this value.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="routingZoneReference">
/sdk-for-flutter-explore-routing-violatedrestrictiondetails-routingzonereference
↔ String?
</dt>
<dd>
  Contains the restricted routing zone reference
This property will be set if the /sdk-for-flutter-explore-routing-avoidanceoptions-zonecategories is not empty
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-routing-violatedrestrictiondetails-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="timeRule">
/sdk-for-flutter-explore-routing-violatedrestrictiondetails-timerule
↔ /sdk-for-flutter-explore-core-timerule-class?
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
/sdk-for-flutter-explore-routing-violatedrestrictiondetails-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-routing-violatedrestrictiondetails-tostring(<wbr/>)
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
/sdk-for-flutter-explore-routing-violatedrestrictiondetails-operator-equals(<wbr/>Object other)
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
`
}</HTMLBlock>
