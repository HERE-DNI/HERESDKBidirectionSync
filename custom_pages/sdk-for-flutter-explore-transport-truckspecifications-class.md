---
title: "TruckSpecifications class"
slug: "sdk-for-flutter-explore-transport-truckspecifications-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TruckSpecifications-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="transport/TruckSpecifications-class.html#constructors">Constructors</a></li>
<li><a href="transport/TruckSpecifications/TruckSpecifications.html">TruckSpecifications</a></li>
<li><a href="transport/TruckSpecifications/TruckSpecifications.withDefaults.html">withDefaults</a></li>
<li class="section-title">
<a href="transport/TruckSpecifications-class.html#instance-properties">Properties</a>
</li>
<li><a href="transport/TruckSpecifications/axleCount.html">axleCount</a></li>
<li><a href="transport/TruckSpecifications/currentWeightInKilograms.html">currentWeightInKilograms</a></li>
<li><a href="transport/TruckSpecifications/grossWeightInKilograms.html">grossWeightInKilograms</a></li>
<li><a href="transport/TruckSpecifications/hashCode.html">hashCode</a></li>
<li><a href="transport/TruckSpecifications/heightInCentimeters.html">heightInCentimeters</a></li>
<li><a href="transport/TruckSpecifications/isTruckLight.html">isTruckLight</a></li>
<li><a href="transport/TruckSpecifications/lengthInCentimeters.html">lengthInCentimeters</a></li>
<li><a href="transport/TruckSpecifications/payloadCapacityInKilograms.html">payloadCapacityInKilograms</a></li>
<li class="inherited"><a href="transport/TruckSpecifications/runtimeType.html">runtimeType</a></li>
<li><a href="transport/TruckSpecifications/trailerAxleCount.html">trailerAxleCount</a></li>
<li><a href="transport/TruckSpecifications/trailerCount.html">trailerCount</a></li>
<li><a href="transport/TruckSpecifications/truckType.html">truckType</a></li>
<li><a href="transport/TruckSpecifications/weightPerAxleGroup.html">weightPerAxleGroup</a></li>
<li><a href="transport/TruckSpecifications/weightPerAxleInKilograms.html">weightPerAxleInKilograms</a></li>
<li><a href="transport/TruckSpecifications/widthInCentimeters.html">widthInCentimeters</a></li>
<li class="section-title inherited"><a href="transport/TruckSpecifications-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="transport/TruckSpecifications/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="transport/TruckSpecifications/toString.html">toString</a></li>
<li class="section-title"><a href="transport/TruckSpecifications-class.html#operators">Operators</a></li>
<li><a href="transport/TruckSpecifications/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-transport-transport-library</li>
<li class="self-crumb">TruckSpecifications class</li>
</ol>
<div class="self-name">TruckSpecifications</div>
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
<div class="main-content" data-above-sidebar="transport/transport-library-sidebar.html" data-below-sidebar="transport/TruckSpecifications-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>TruckSpecifications class</h1></div>
<section class="desc markdown">
<p>Truck specifications contain vehicle related attributes.</p>
<p>Examples: Dimensions, weight, axle count.
Only the fields that are set are considered for restriction handling.</p>
</section>
<section>
<dl class="dl-horizontal">
<dt>Annotations</dt>
<dd>
<ul class="annotation-list clazz-relationships">
<li>@Deprecated("Will be removed in v4.28.0. Use `TransportSpecification` instead.")</li>
</ul>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="TruckSpecifications">
/sdk-for-flutter-explore-transport-truckspecifications-truckspecifications([int? grossWeightInKilograms = null, int? currentWeightInKilograms = null, int? weightPerAxleInKilograms = null, /sdk-for-flutter-explore-transport-weightperaxlegroup-class? weightPerAxleGroup = null, int? heightInCentimeters = null, int? widthInCentimeters = null, int? lengthInCentimeters = null, int? axleCount = null, int? trailerCount = null, /sdk-for-flutter-explore-transport-trucktype truckType = TruckType.straight, bool isTruckLight = false, int? payloadCapacityInKilograms = null, int? trailerAxleCount = null])
</dt>
<dd>
          Creates a new instance.
        </dd>
<dt class="callable" id="TruckSpecifications.withDefaults">
/sdk-for-flutter-explore-transport-truckspecifications-truckspecifications-withdefaults()
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
/sdk-for-flutter-explore-transport-truckspecifications-axlecount
↔ int?
</dt>
<dd>
  Defines total number of axles in the vehicle. The provided value must be greater than or
equal to 2. By default, it is not set.
Route calculation: When not set, possible axle count restrictions will not be
taken into consideration.
Rendering <code>sdk.mapview.TruckProfile</code>: When set, truck restriction icons for an axle count
greater than /sdk-for-flutter-explore-transport-truckspecifications-axlecount will not be displayed.
When specifying /sdk-for-flutter-explore-transport-truckspecifications-traileraxlecount, then /sdk-for-flutter-explore-transport-truckspecifications-axlecount is required and must be greater than /sdk-for-flutter-explore-transport-truckspecifications-traileraxlecount.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="currentWeightInKilograms">
/sdk-for-flutter-explore-transport-truckspecifications-currentweightinkilograms
↔ int?
</dt>
<dd>
  Current truck weight, including trailers and shipped goods currently loaded, specified in
kilograms. The provided value must be greater than or equal to 0. If unspecified,
it will default to /sdk-for-flutter-explore-transport-truckspecifications-grossweightinkilograms. By default, it is not set.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="grossWeightInKilograms">
/sdk-for-flutter-explore-transport-truckspecifications-grossweightinkilograms
↔ int?
</dt>
<dd>
  Gross truck weight, including trailers and shipped goods when loaded at capacity, specified in
kilograms. The provided value must be greater than or equal to 0. If unspecified,
it will default to /sdk-for-flutter-explore-transport-truckspecifications-currentweightinkilograms. By default, it is not set.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-explore-transport-truckspecifications-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="heightInCentimeters">
/sdk-for-flutter-explore-transport-truckspecifications-heightincentimeters
↔ int?
</dt>
<dd>
  Truck height in centimeters. The provided value must be in the range [0, 5000].
By default, it is not set.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isTruckLight">
/sdk-for-flutter-explore-transport-truckspecifications-istrucklight
↔ bool
</dt>
<dd>
  A flag indicating whether the truck is light enough to be classified more as a car than a truck in Japan.
The flag should not be set to <code>true</code> in other countries than Japan. The flag defaults to <code>false</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="lengthInCentimeters">
/sdk-for-flutter-explore-transport-truckspecifications-lengthincentimeters
↔ int?
</dt>
<dd>
  Truck length in centimeters. The provided value must be in the range [0, 30000].
By default, it is not set.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="payloadCapacityInKilograms">
/sdk-for-flutter-explore-transport-truckspecifications-payloadcapacityinkilograms
↔ int?
</dt>
<dd>
  Allowed payload capacity, including trailers, specified in kilograms. The provided value
must be greater then or equal to 0. By default, it is not set.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-transport-truckspecifications-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="trailerAxleCount">
/sdk-for-flutter-explore-transport-truckspecifications-traileraxlecount
↔ int?
</dt>
<dd>
  Defines total number of axles across all the trailers attached to the vehicle.
This number is included in /sdk-for-flutter-explore-transport-truckspecifications-axlecount, hence /sdk-for-flutter-explore-transport-truckspecifications-traileraxlecount must be less than /sdk-for-flutter-explore-transport-truckspecifications-axlecount
and greater than or equal to 1. /sdk-for-flutter-explore-transport-truckspecifications-axlecount and /sdk-for-flutter-explore-transport-truckspecifications-trailercount are required to specify /sdk-for-flutter-explore-transport-truckspecifications-traileraxlecount.
By default, it is not set.
Note: This parameter is currently used only for the calculation of tolls in regions where it is applicable.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="trailerCount">
/sdk-for-flutter-explore-transport-truckspecifications-trailercount
↔ int?
</dt>
<dd>
  Defines number of trailers attached to the vehicle. The provided value must be in the range
[0, 255]. By default, it is not set.
When specifying /sdk-for-flutter-explore-transport-truckspecifications-traileraxlecount, then /sdk-for-flutter-explore-transport-truckspecifications-trailercount is required and must be greater than 0.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="truckType">
/sdk-for-flutter-explore-transport-truckspecifications-trucktype
↔ /sdk-for-flutter-explore-transport-trucktype
</dt>
<dd>
  Defines the type of truck. By default, it is /sdk-for-flutter-explore-transport-trucktype.
Rendering <code>sdk.mapview.TruckProfile</code>: /sdk-for-flutter-explore-transport-truckspecifications-trucktype is ignored and has no effect.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="weightPerAxleGroup">
/sdk-for-flutter-explore-transport-truckspecifications-weightperaxlegroup
↔ /sdk-for-flutter-explore-transport-weightperaxlegroup-class?
</dt>
<dd>
  Allows specification of axle weights in a more fine-grained way than <code>weight_per_axle_in_kilograms</code>.
This is relevant in countries with signs and regulations that specify different limits for different axle groups, like the USA and Sweden.
By default is not set.
<strong>Note:</strong> <code>weight_per_axle_in_kilograms</code> and <code>weight_per_axle_group</code> are incompatible.
When available for your edition, if both attributes are set, during online RoutingEngine an <code>sdk.routing.RoutingError.INVALID_PARAMETER</code> error is generated.
Otherwise, when offline RoutingEngine is in place, both parameters are evaluated and the maximum value between them will be used.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="weightPerAxleInKilograms">
/sdk-for-flutter-explore-transport-truckspecifications-weightperaxleinkilograms
↔ int?
</dt>
<dd>
  Heaviest weight per axle, regardless of axle type or axle group.
It is evaluated against all axle weight restrictions, including single axle and tandem axle weight restrictions.
The provided value must be greater or equal to 0.
By default, it is not set.
<strong>Note:</strong> <code>weight_per_axle_in_kilograms</code> and <code>weight_per_axle_group</code> are incompatible.
When available for your edition, if both attributes are set, during online RoutingEngine an <code>sdk.routing.RoutingError.INVALID_PARAMETER</code> error is generated.
Otherwise, when offline RoutingEngine is in place, both parameters are evaluated and the maximum value between them will be used.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="widthInCentimeters">
/sdk-for-flutter-explore-transport-truckspecifications-widthincentimeters
↔ int?
</dt>
<dd>
  Truck width in centimeters. The provided value must be in the range [0, 5000].
By default, it is not set.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-explore-transport-truckspecifications-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-transport-truckspecifications-tostring(<wbr/>)
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
/sdk-for-flutter-explore-transport-truckspecifications-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">TruckSpecifications class</li>
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
