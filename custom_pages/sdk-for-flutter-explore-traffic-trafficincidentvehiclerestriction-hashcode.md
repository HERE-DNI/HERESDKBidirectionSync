---
title: "Implementation"
slug: "sdk-for-flutter-explore-traffic-trafficincidentvehiclerestriction-hashcode"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- hashCode.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../traffic/traffic-library.html">/sdk-for-flutter-explore-traffic-traffic-library</a></li>
<li><a href="../../traffic/TrafficIncidentVehicleRestriction-class.html">/sdk-for-flutter-explore-traffic-trafficincidentvehiclerestriction-class</a></li>
<li class="self-crumb">hashCode property</li>
</ol>
<div class="self-name">hashCode</div>
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
<div class="main-content" data-above-sidebar="traffic/TrafficIncidentVehicleRestriction-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>hashCode property</h1></div>
<section id="getter">
<section class="multi-line-signature">
<div>
<ol class="annotation-list">
<li>@override</li>
</ol>
</div>
int
hashCode
</section>
<section class="desc markdown">
<p>The hash code for this object.</p>
<p>A hash code is a single integer which represents the state of the object
that affects <a href="../../traffic/TrafficIncidentVehicleRestriction/operator_equals.html">/sdk-for-flutter-explore-traffic-trafficincidentvehiclerestriction-operator-equals</a> comparisons.</p>
<p>All objects have hash codes.
The default hash code implemented by <code>Object</code>
represents only the identity of the object,
the same way as the default <a href="../../traffic/TrafficIncidentVehicleRestriction/operator_equals.html">/sdk-for-flutter-explore-traffic-trafficincidentvehiclerestriction-operator-equals</a> implementation only considers objects
equal if they are identical (see <code>identityHashCode</code>).</p>
<p>If <a href="../../traffic/TrafficIncidentVehicleRestriction/operator_equals.html">/sdk-for-flutter-explore-traffic-trafficincidentvehiclerestriction-operator-equals</a> is overridden to use the object state instead,
the hash code must also be changed to represent that state,
otherwise the object cannot be used in hash based data structures
like the default <code>Set</code> and <code>Map</code> implementations.</p>
<p>Hash codes must be the same for objects that are equal to each other
according to <a href="../../traffic/TrafficIncidentVehicleRestriction/operator_equals.html">/sdk-for-flutter-explore-traffic-trafficincidentvehiclerestriction-operator-equals</a>.
The hash code of an object should only change if the object changes
in a way that affects equality.
There are no further requirements for the hash codes.
They need not be consistent between executions of the same program
and there are no distribution guarantees.</p>
<p>Objects that are not equal are allowed to have the same hash code.
It is even technically allowed that all instances have the same hash code,
but if clashes happen too often,
it may reduce the efficiency of hash-based data structures
like <code>HashSet</code> or <code>HashMap</code>.</p>
<p>If a subclass overrides <a href="../../traffic/TrafficIncidentVehicleRestriction/hashCode.html">/sdk-for-flutter-explore-traffic-trafficincidentvehiclerestriction-hashcode</a>, it should override the
<a href="../../traffic/TrafficIncidentVehicleRestriction/operator_equals.html">/sdk-for-flutter-explore-traffic-trafficincidentvehiclerestriction-operator-equals</a> operator as well to maintain consistency.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">@override
int get hashCode {
  int result = 7;
  result = 31 * result + isRestrictedAlways.hashCode;
  result = 31 * result + isDieselFuelRestricted.hashCode;
  result = 31 * result + isPetrolFuelRestricted.hashCode;
  result = 31 * result + isLpgFuelRestricted.hashCode;
  result = 31 * result + isCaravanRestricted.hashCode;
  result = 31 * result + isTrailerRestricted.hashCode;
  result = 31 * result + isDrivingWithoutSnowChainsRestricted.hashCode;
  result = 31 * result + isDrivingWithoutWinterTyresRestricted.hashCode;
  result = 31 * result + isEvenNumberPlateRestricted.hashCode;
  result = 31 * result + isOddNumberPlateRestricted.hashCode;
  result = 31 * result + isThroughTrafficRestricted.hashCode;
  result = 31 * result + isResidentsTrafficRestricted.hashCode;
  result = 31 * result + isDestinationInIncidentAreaRestricted.hashCode;
  result = 31 * result + isEuro3EmissionStandardRestricted.hashCode;
  result = 31 * result + isEuro4EmissionStandardRestricted.hashCode;
  result = 31 * result + isEuro5EmissionStandardRestricted.hashCode;
  result = 31 * result + restrictedIfGrossWeightMoreThanInKilograms.hashCode;
  result = 31 * result + restrictedIfGrossWeightLessThanInKilograms.hashCode;
  result = 31 * result + restrictedIfAxleWeightMoreThanInKilograms.hashCode;
  result = 31 * result + restrictedIfAxleWeightLessThanInKilograms.hashCode;
  result = 31 * result + restrictedIfLongerThanInCentimeters.hashCode;
  result = 31 * result + restrictedIfShorterThanInCentimeters.hashCode;
  result = 31 * result + restrictedIfHigherThanInCentimeters.hashCode;
  result = 31 * result + restrictedIfLowerThanInCentimeters.hashCode;
  result = 31 * result + restrictedIfWiderThanInCentimeters.hashCode;
  result = 31 * result + restrictedIfNarrowerThanInCentimeters.hashCode;
  result = 31 * result + restrictedIfOccupantsMoreThan.hashCode;
  result = 31 * result + restrictedIfOccupantsFewerThan.hashCode;
  return result;
}</code></pre>
</section>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../traffic/traffic-library.html">/sdk-for-flutter-explore-traffic-traffic-library</a></li>
<li><a href="../../traffic/TrafficIncidentVehicleRestriction-class.html">/sdk-for-flutter-explore-traffic-trafficincidentvehiclerestriction-class</a></li>
<li class="self-crumb">hashCode property</li>
</ol>
<h5>TrafficIncidentVehicleRestriction class</h5>
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
