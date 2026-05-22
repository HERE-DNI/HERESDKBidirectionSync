---
title: "Untitled"
slug: "sdk-for-flutter-navigate-routing-violatedrestrictiondetails-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ViolatedRestrictionDetails-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
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
/sdk-for-flutter-navigate-routing-violatedrestrictiondetails-violatedrestrictiondetails()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="forbiddenAxleCount">
/sdk-for-flutter-navigate-routing-violatedrestrictiondetails-forbiddenaxlecount
↔ /sdk-for-flutter-navigate-core-integerrange-class?
</dt>
<dd>
  The restriction to trucks with axles number within specified range during the trip.
This property will be set if the /sdk-for-flutter-navigate-transport-vehiclespecification-axlecount
is within this range.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="forbiddenHazardousGoods">
/sdk-for-flutter-navigate-routing-violatedrestrictiondetails-forbiddenhazardousgoods
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-transport-hazardousmaterial&gt;
</dt>
<dd>
  There are two lists for our trip: Hazardous goods restrictions applied during the trip, and the list used
for the route calculation provided using /sdk-for-flutter-navigate-transport-vehiclespecification-hazardousmaterials from
/sdk-for-flutter-navigate-transport-transportspecification-vehiclespecification from /sdk-for-flutter-navigate-routing-routingoptions-transportspecification.
This property is the intersection of the two lists.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="forbiddenTrailerCount">
/sdk-for-flutter-navigate-routing-violatedrestrictiondetails-forbiddentrailercount
↔ /sdk-for-flutter-navigate-core-integerrange-class?
</dt>
<dd>
  Constrains the restriction to trucks with number of trailer within specified range during the trip.
This property will be set if the /sdk-for-flutter-navigate-transport-vehiclespecification-trailercount
is within this range.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="forbiddenTruckCategory">
/sdk-for-flutter-navigate-routing-violatedrestrictiondetails-forbiddentruckcategory
↔ /sdk-for-flutter-navigate-transport-truckcategory?
</dt>
<dd>
  This property will be set if a restriction applies to the value of /sdk-for-flutter-navigate-transport-truckcategory
parameter used for route calculation.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="forbiddenTruckRoadTypes">
/sdk-for-flutter-navigate-routing-violatedrestrictiondetails-forbiddentruckroadtypes
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-transport-truckroadtype&gt;
</dt>
<dd>
  Contains violated restrictions for truck road types.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="forbiddenTruckType">
/sdk-for-flutter-navigate-routing-violatedrestrictiondetails-forbiddentrucktype
↔ /sdk-for-flutter-navigate-transport-trucktype?
</dt>
<dd>
  This property will be set if a restriction applies to the value of /sdk-for-flutter-navigate-transport-trucktype
parameter used for route calculation.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-routing-violatedrestrictiondetails-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="maxHeightInCentimeters">
/sdk-for-flutter-navigate-routing-violatedrestrictiondetails-maxheightincentimeters
↔ int?
</dt>
<dd>
  Max permitted height during the trip, in centimeters.
This property will be set if the /sdk-for-flutter-navigate-transport-vehiclespecification-heightincentimeters
exceeds this value.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maxKingpinToRearAxleDistanceInCentimeters">
/sdk-for-flutter-navigate-routing-violatedrestrictiondetails-maxkingpintorearaxledistanceincentimeters
↔ int?
</dt>
<dd>
  Contains the maximum permitted distance from kingpin to the rear axle in centimeters.
This property will be set if the
/sdk-for-flutter-navigate-transport-vehiclespecification-kingpintorearaxledistanceincentimeters
exceeds the specified value.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maxLengthInCentimeters">
/sdk-for-flutter-navigate-routing-violatedrestrictiondetails-maxlengthincentimeters
↔ int?
</dt>
<dd>
  Max permitted length during the trip, in centimeters.
This property will be set if the /sdk-for-flutter-navigate-transport-vehiclespecification-lengthincentimeters
exceeds this value.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maxNumberOfTires">
/sdk-for-flutter-navigate-routing-violatedrestrictiondetails-maxnumberoftires
↔ int?
</dt>
<dd>
  Contains the maximum permitted number of tires.
This property will be set if the /sdk-for-flutter-navigate-transport-vehiclespecification-tirescount exceeds the specified value.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maxPayloadCapacityInKilograms">
/sdk-for-flutter-navigate-routing-violatedrestrictiondetails-maxpayloadcapacityinkilograms
↔ int?
</dt>
<dd>
  Max permitted payload capacity during the trip, in kilograms.
This property will be set if the /sdk-for-flutter-navigate-transport-vehiclespecification-payloadcapacityinkilograms
exceeds this value.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maxTunnelCategory">
/sdk-for-flutter-navigate-routing-violatedrestrictiondetails-maxtunnelcategory
↔ /sdk-for-flutter-navigate-transport-tunnelcategory?
</dt>
<dd>
  Tunnel category to restrict transport of specific goods during the trip.
This property will be set if the /sdk-for-flutter-navigate-transport-vehiclespecification-tunnelcategory from
/sdk-for-flutter-navigate-transport-transportspecification-vehiclespecification from /sdk-for-flutter-navigate-routing-routingoptions-transportspecification
exceeds this value.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maxWeight">
/sdk-for-flutter-navigate-routing-violatedrestrictiondetails-maxweight
↔ /sdk-for-flutter-navigate-routing-vehiclerestrictionmaxweight-class?
</dt>
<dd>
  Max permitted weight during the trip, in kilograms, along with the specific type of maximum permitted weight restriction.
This property will be set if the /sdk-for-flutter-navigate-transport-vehiclespecification-grossweightinkilograms
parameter used for route calculation exceeds this value.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maxWeightPerAxleGroupInKilograms">
/sdk-for-flutter-navigate-routing-violatedrestrictiondetails-maxweightperaxlegroupinkilograms
↔ /sdk-for-flutter-navigate-routing-maxaxlegroupweight-class?
</dt>
<dd>
  Max permitted weight per axle group during the trip, in kilograms.
This property will be set if the /sdk-for-flutter-navigate-transport-vehiclespecification-weightperaxlegroup
exceeds this value.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maxWeightPerAxleInKilograms">
/sdk-for-flutter-navigate-routing-violatedrestrictiondetails-maxweightperaxleinkilograms
↔ int?
</dt>
<dd>
  Max permitted weight per axle during the trip, in kilograms.
This property will be set if the /sdk-for-flutter-navigate-transport-vehiclespecification-weightperaxleinkilograms
exceeds this value.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maxWidthInCentimeters">
/sdk-for-flutter-navigate-routing-violatedrestrictiondetails-maxwidthincentimeters
↔ int?
</dt>
<dd>
  Max permitted width during the trip, in centimeters.
This property will be set if the /sdk-for-flutter-navigate-transport-vehiclespecification-widthincentimeters
exceeds this value.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="routingZoneReference">
/sdk-for-flutter-navigate-routing-violatedrestrictiondetails-routingzonereference
↔ String?
</dt>
<dd>
  Contains the restricted routing zone reference
This property will be set if the /sdk-for-flutter-navigate-routing-avoidanceoptions-zonecategories is not empty
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-routing-violatedrestrictiondetails-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="timeRule">
/sdk-for-flutter-navigate-routing-violatedrestrictiondetails-timerule
↔ /sdk-for-flutter-navigate-core-timerule-class?
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
/sdk-for-flutter-navigate-routing-violatedrestrictiondetails-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-routing-violatedrestrictiondetails-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-routing-violatedrestrictiondetails-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
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



</div>
`
}</HTMLBlock>
